---
UID: NF:storport.StorPortAllocateHostMemoryBuffer
title: StorPortAllocateHostMemoryBuffer function
author: windows-driver-content
description: This function allocates one or more ranges of physically contiguous memory to be used as a Host Memory Buffer (HMB).
old-location: storage\storportallocatehostmemorybuffer.htm
old-project: storage
ms.assetid: B8413B02-32A6-40AE-9DD2-C25AD2D2D45C
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortAllocateHostMemoryBuffer, StorPortAllocateHostMemoryBuffer routine [Storage Devices], storage.storportallocatehostmemorybuffer, storport/StorPortAllocateHostMemoryBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	storport.h
api_name:
-	StorPortAllocateHostMemoryBuffer
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortAllocateHostMemoryBuffer function
This function allocates one or more ranges of physically contiguous memory
    to be used as a Host Memory Buffer (HMB).  This is memory that the device
    may use directly and exclusively.  The device may use this memory however
    it sees fit, but it must ensure that there is no data loss or data
    corruption in the event of a surprise removal or unexpected power loss.

Depending on the allocation policy, this function may allocate as much as
    the device's preferred size, as little as the device's minimum size, or no
    memory at all.

    This function will attempt to allocate as few physically contiguous address
    ranges as possible, but it may have to use multiple physical address ranges
    to satisfy the desired HMB size.

## Syntax

```
ULONG StorPortAllocateHostMemoryBuffer(
  PVOID            HwDeviceExtension,
  SIZE_T           MinimumBytes,
  SIZE_T           PreferredBytes,
  ULONGLONG        UtilizationBytes,
  ULONG            AlignmentBytes,
  PHYSICAL_ADDRESS LowestAcceptableAddress,
  PHYSICAL_ADDRESS HighestAcceptableAddress,
  PHYSICAL_ADDRESS BoundaryAddressMultiple,
  PACCESS_RANGE    PhysicalAddressRanges,
  PULONG           PhysicalAddressRangeCount
);
```

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension for the host bus adapter (HBA).

`MinimumBytes`

The minimum amount of memory that will be useful to the
        device, in bytes. A value of 0 indicates that any size of memory up to
        the preferred size is acceptable.

`PreferredBytes`

The amount of memory the device prefers, in bytes.  This
        must be a multiple of the page size.

`UtilizationBytes`

The total number of blocks allocated on the device, in
        bytes.

`AlignmentBytes`

The Host Memory Buffer alignment requirement from the device.

`LowestAcceptableAddress`

The lowest physical address that is valid for the allocation. For example, if the device can only reference physical memory in the 8 MB to 16 MB range, this value would be set to 0x800000 (8 MB).

`HighestAcceptableAddress`

The highest physical address that is valid for the allocation. For example, if the device can only reference physical memory below 16 MB, this value would be set to 0xFFFFFF (16 MB - 1).

`BoundaryAddressMultiple`

The physical address multiple that this allocation must not cross.

<div class="alert"><b>Note</b>  This parameter is currently not used and must be set to 0.</div>
<div> </div>

`PhysicalAddressRanges`

An array of physical address ranges that make up
        the Host Memory Buffer.  The caller should provide a pre-allocated array.  <b>StorPortAllocateHostMemoryBuffer</b> will
        fill in the array with one or more physical address ranges.

`PhysicalAddressRangeCount`

The number of entries in <b>PhysicalAddressRanges</b>. This function will update this parameter to indicate how
        many physical address ranges it filled in.


## Return Value

<b>StorPortAllocateHostMemoryBuffer</b> returns one of the following status codes:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The <b>PhysicalAddressRanges</b> array contains one or more valid physical address ranges that represent the host memory buffer.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
This could indicate a minimum value that is greater than a maximum value, a non-page-aligned size, or that <b>PhysicalAddressRanges</b> is empty.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
The host memory buffer could not be allocated.

</td>
</tr>
</table>

## Remarks

The caller should subsequently call <a href="https://msdn.microsoft.com/686D141E-E6EA-4BB6-8556-0ECAC592E8F0">StorPortFreeHostMemoryBuffer</a> when it is
    done with the host memory buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |

## See Also

<a href="https://msdn.microsoft.com/686D141E-E6EA-4BB6-8556-0ECAC592E8F0">StorPortFreeHostMemoryBuffer</a>
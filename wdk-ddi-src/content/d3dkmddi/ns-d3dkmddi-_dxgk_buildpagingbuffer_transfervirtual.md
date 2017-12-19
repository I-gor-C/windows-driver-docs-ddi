---
UID: NS.D3DKMDDI._DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
title: _DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL is used as part of an allocation transfer operation.
old-location: display\dxgk_buildpagingbuffer_transfervirtual.htm
old-project: display
ms.assetid: D4427E44-204F-490C-9EE7-BBC4906E5920
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL, DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# _DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL structure



## -description
<b>DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL</b> is used as part of an allocation transfer operation.



## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL {
  HANDLE                         hAllocation;
  UINT64                         AllocationOffsetInBytes;
  UINT64                         TransferSizeInBytes;
  D3DGPU_VIRTUAL_ADDRESS         SourceVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS         DestinationVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS         SourcePageTable;
  DXGK_MEMORY_TRANSFER_DIRECTION TransferDirection;
  DXGK_TRANSFERVIRTUALFLAGS      Flags;
  D3DGPU_VIRTUAL_ADDRESS         DestinationPageTable;
} DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL;
````


## -struct-fields

### -field hAllocation

Kernel mode driver handle of the transferred allocation content. The handle is returned from <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createallocation.md">DxgkDdiCreateAllocation</a>. The allocation properties are needed to perform special transfers (as swizzle, de-swizzle, etc.).


### -field AllocationOffsetInBytes

The offset in bytes from the start of the allocation being transferred. The offset should not be added to <b>SourceVirtualAddress</b> or <b>DesinationVirtualAddress</b>.


### -field TransferSizeInBytes

The number of bytes to transfer.


### -field SourceVirtualAddress

The virtual address of the source in the context of the paging process. 


### -field DestinationVirtualAddress

The virtual address of the destination in the context of the paging process.


### -field SourcePageTable

The GPU virtual address of the page table that is used to map the <b>SourceVirtualAddress</b> address. 

<div class="alert"><b>Note</b>  The address is valid only when the <b>DXGK_GPUMMUCAPS.LegacyBehaviors.SourcePageTableVaInTransfer</b> cap is set.</div>
<div> </div>

### -field TransferDirection

The <a href="display.dxgk_memory_transfer_direction">DXGK_MEMORY_TRANSFER_DIRECTION</a> structure describing the operation.


### -field Flags

The <a href="display.dxgk_transfervirtualflags">DXGK_TRANSFERVIRTUALFLAGS</a> structure describing the operation.


### -field DestinationPageTable

The GPU virtual address of the page table that  is used to map the <b>DestinationVirtualAddress</b> address. The address is valid only when the <b>DXGK_GPUMMUCAPS.LegacyBehaviors.SourcePageTableVaInTransfer</b> cap is set.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createallocation.md">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="display.dxgk_memory_transfer_direction">DXGK_MEMORY_TRANSFER_DIRECTION</a>
</dt>
<dt>
<a href="display.dxgk_transfervirtualflags">DXGK_TRANSFERVIRTUALFLAGS</a>
</dt>
<dt>
<a href="display.dxgkarg_buildpagingbuffer">DXGKARG_BUILDPAGINGBUFFER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


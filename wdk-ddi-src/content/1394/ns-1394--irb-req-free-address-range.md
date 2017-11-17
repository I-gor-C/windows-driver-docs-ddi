---
UID: NS.1394._IRB_REQ_FREE_ADDRESS_RANGE
title: IRB_REQ_FREE_ADDRESS_RANGE
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 stack to carry out a free address range reqeust.
old-location: ieee\irb_req_free_address_range.htm
ms.assetid: 18C1A210-6C6D-4BA7-AE62-81774DD62C58
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_FREE_ADDRESS_RANGE
req.alt-loc: 1394.h
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
ms.keywords: IRB_REQ_FREE_ADDRESS_RANGE, IRB_REQ_FREE_ADDRESS_RANGE
---

# IRB_REQ_FREE_ADDRESS_RANGE structure



## -description
<p>This structure contains the fields necessary for the 1394 stack to carry out a free address range reqeust.</p>


## -syntax

````
typedef struct _IRB_REQ_FREE_ADDRESS_RANGE {
  ULONG          nAddressesToFree;
  PADDRESS_RANGE p1394AddressRange;
  PHANDLE        pAddressRange;
  PVOID          DeviceExtension;
} IRB_REQ_FREE_ADDRESS_RANGE;
````


## -struct-fields
<dl>

### -field <b>nAddressesToFree</b>

<dd>
<p>Specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff536908">ADDRESS_RANGE</a> structures pointed to by <b>IRB.u.FreeAddressRange.p1394AddressRange</b></p>
</dd>

### -field <b>p1394AddressRange</b>

<dd>
<p>Specifies a pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff536908">ADDRESS_RANGE</a> data structures to be released. These address ranges were returned in a prior successful call to <b>AllocateAddressRange</b>.</p>
</dd>

### -field <b>pAddressRange</b>

<dd>
<p>Points to the handle that was previously received in <b>IRB.u.AllocateAddressRange.hAddressRange</b> in the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff537632">REQUEST_ALLOCATE_ADDRESS_RANGE</a> request.</p>
</dd>

### -field <b>DeviceExtension</b>

<dd>
<p>Points to the device extension associated with the device object. Not setting this member can lead to unexpected behavior when the driver tries to access the allocated address space. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>
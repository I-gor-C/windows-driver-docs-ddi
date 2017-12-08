---
UID: NS.D3DKMDDI._DXGK_PRESENTALLOCATIONINFO
title: _DXGK_PRESENTALLOCATIONINFO
author: windows-driver-content
description: The DXGK_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver.
old-location: display\dxgk_presentallocationinfo.htm
old-project: display
ms.assetid: 8a7f25cf-c08c-4f65-bbf4-ba129d88ff6a
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_PRESENTALLOCATIONINFO, DXGK_PRESENTALLOCATIONINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PRESENTALLOCATIONINFO
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

# _DXGK_PRESENTALLOCATIONINFO structure



## -description
The DXGK_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver.


## -syntax

````
typedef struct _DXGK_PRESENTALLOCATIONINFO {
  HANDLE                 hDeviceSpecificAllocation;
  D3DGPU_VIRTUAL_ADDRESS AllocationVirtualAddress;
  PHYSICAL_ADDRESS       PhysicalAddress;
  WORD                   SegmentId;
  WORD                   PhysicalAdapterIndex;
} DXGK_PRESENTALLOCATIONINFO;
````


## -struct-fields

### -field hDeviceSpecificAllocation

Reserved for system use.

### -field AllocationVirtualAddress

Reserved for system use.

### -field PhysicalAddress

Reserved for system use.

### -field SegmentId

Reserved for system use.

### -field PhysicalAdapterIndex

Reserved for system use.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows 7 and later versions of the Windows operating systems.
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
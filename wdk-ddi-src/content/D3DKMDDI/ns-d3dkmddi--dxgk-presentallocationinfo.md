---
UID: NS.d3dkmddi._DXGK_PRESENTALLOCATIONINFO
title: DXGK_PRESENTALLOCATIONINFO
author: windows-driver-content
description: The DXGK_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver.
old-location: display\dxgk_presentallocationinfo.htm
ms.assetid: 8a7f25cf-c08c-4f65-bbf4-ba129d88ff6a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: DXGK_PRESENTALLOCATIONINFO, DXGK_PRESENTALLOCATIONINFO
req.iface: 
---

# DXGK_PRESENTALLOCATIONINFO structure



## -description
<p>The DXGK_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver.</p>


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
<dl>

### -field <b>hDeviceSpecificAllocation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>AllocationVirtualAddress</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>
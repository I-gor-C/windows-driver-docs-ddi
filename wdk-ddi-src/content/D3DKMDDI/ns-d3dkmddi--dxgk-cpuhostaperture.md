---
UID: NS.d3dkmddi._DXGK_CPUHOSTAPERTURE
title: DXGK_CPUHOSTAPERTURE
author: windows-driver-content
description: DXGK_CPUHOSTAPERTURE describes a memory segment supporting a CPU host aperture.
old-location: display\dxgk_cpuhostaperture.htm
ms.assetid: BBB9D8F6-0EF8-4B34-B79E-8742BB7575D4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CPUHOSTAPERTURE
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
ms.keywords: DXGK_CPUHOSTAPERTURE, DXGK_CPUHOSTAPERTURE
req.iface: 
---

# DXGK_CPUHOSTAPERTURE structure



## -description
<p><b>DXGK_CPUHOSTAPERTURE</b> describes a memory segment supporting a CPU host aperture.</p>


## -syntax

````
typedef struct _DXGK_CPUHOSTAPERTURE {
  UINT64 PhysicalAddress;
  UINT32 SizeInPages;
} DXGK_CPUHOSTAPERTURE;
````


## -struct-fields
<dl>

### -field <b>PhysicalAddress</b>

<dd>
<p>The CPU physical address.</p>
</dd>

### -field <b>SizeInPages</b>

<dd>
<p>The size d3ddiin CPU host pages.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
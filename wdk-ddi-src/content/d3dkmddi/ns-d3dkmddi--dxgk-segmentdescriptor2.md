---
UID: NS.d3dkmddi._DXGK_SEGMENTDESCRIPTOR2
title: DXGK_SEGMENTDESCRIPTOR2
author: windows-driver-content
description: The DXGK_SEGMENTDESCRIPTOR2 structure is reserved for system use. Do not use it in your driver.
old-location: display\dxgk_segmentdescriptor2.htm
old-project: display
ms.assetid: 94eb1c9a-919c-4819-848b-29106e216980
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_SEGMENTDESCRIPTOR2, DXGK_SEGMENTDESCRIPTOR2
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
req.alt-api: DXGK_SEGMENTDESCRIPTOR2
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
req.iface: 
---

# DXGK_SEGMENTDESCRIPTOR2 structure



## -description
<p>The DXGK_SEGMENTDESCRIPTOR2 structure is reserved for system use. Do not use it in your driver.</p>


## -syntax

````
typedef struct _DXGK_SEGMENTDESCRIPTOR2 {
  DXGK_SEGMENTFLAGS2 Flags;
  SIZE_T             Size;
  PMDL               pMdl;
  PHYSICAL_ADDRESS   BaseAddress;
  PHYSICAL_ADDRESS   CpuTranslatedAddress;
} DXGK_SEGMENTDESCRIPTOR2;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>BaseAddress</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>CpuTranslatedAddress</b>

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
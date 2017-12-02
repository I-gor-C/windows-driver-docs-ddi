---
UID: NE.d3d10umddi.D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
title: D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
author: windows-driver-content
description: D3DWDDM2_0DDI_CONTEXTTYPE_FLAG describes the type of context being created for interacting with JPEG hardware.
old-location: display\d3dwddm2_0ddi_contexttype_flag.htm
old-project: display
ms.assetid: F767C051-637A-4912-80B0-36C4DF7E46DD
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
req.alt-loc: D3d10umddi.h
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
req.iface: 
---

# D3DWDDM2_0DDI_CONTEXTTYPE_FLAG enumeration



## -description
<p><b>D3DWDDM2_0DDI_CONTEXTTYPE_FLAG</b> describes the type of context being created for interacting with JPEG hardware.</p>


## -syntax

````
typedef enum _D3DWDDM2_0DDI_CONTEXTTYPE_FLAG { 
  D3DWDDM2_0DDI_CONTEXTTYPE_ALL      = 0x00000000,
  D3DWDDM2_0DDI_CONTEXTTYPE_3D       = 0x00000001,
  D3DWDDM2_0DDI_CONTEXTTYPE_COMPUTE  = 0x00000002,
  D3DWDDM2_0DDI_CONTEXTTYPE_COPY     = 0x00000004,
  D3DWDDM2_0DDI_CONTEXTTYPE_VIDEO    = 0x00000008,
  D3DWDDM2_0DDI_CONTEXTTYPE_IMAGE    = 0x00000010
} D3DWDDM2_0DDI_CONTEXTTYPE_FLAG;
````


## -enum-fields
<dl>

### -field D3DWDDM2_0DDI_CONTEXTTYPE_ALL

<dd>
<p>Indicates that all JPEG contexts should be created.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTEXTTYPE_3D

<dd>
<p>Indicates that a JPEG 3D context should be created.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTEXTTYPE_COMPUTE

<dd>
<p>Indicates that a JPEG compute context should be created.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTEXTTYPE_COPY

<dd>
<p>Indicates that  a JPEG copy context should be created.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTEXTTYPE_VIDEO

<dd>
<p>Indicates that a JPEG video context should be created.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTEXTTYPE_IMAGE

<dd>
<p>Indicates that a JPEG image context should be created.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>
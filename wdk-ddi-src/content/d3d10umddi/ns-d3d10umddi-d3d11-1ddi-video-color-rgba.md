---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_COLOR_RGBA
title: D3D11_1DDI_VIDEO_COLOR_RGBA
author: windows-driver-content
description: Specifies an RGB color value.
old-location: display\d3d11_1ddi_video_color_rgba.htm
old-project: display
ms.assetid: 0d97d6ef-87e6-4ba3-ab4b-aa5b22cb126b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDI_VIDEO_COLOR_RGBA, D3D11_1DDI_VIDEO_COLOR_RGBA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_COLOR_RGBA
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

# D3D11_1DDI_VIDEO_COLOR_RGBA structure



## -description
<p>Specifies an RGB color value.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_COLOR_RGBA {
  float R;
  float G;
  float B;
  float A;
} D3D11_1DDI_VIDEO_COLOR_RGBA;
````


## -struct-fields
<dl>

### -field <b>R</b>

<dd>
<p>The red value.</p>
</dd>

### -field <b>G</b>

<dd>
<p>The green value.</p>
</dd>

### -field <b>B</b>

<dd>
<p>The blue value.</p>
</dd>

### -field <b>A</b>

<dd>
<p>The alpha value. Values range from 0 (transparent) to 1 (opaque).
</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
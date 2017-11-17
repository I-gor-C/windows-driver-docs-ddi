---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_INPUT
title: D3D11_1DDI_VIDEO_INPUT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3d11_1ddi_video_input.htm
ms.assetid: 371f494c-abd2-43c8-ab06-749144762b01
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_INPUT
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
ms.keywords: D3D11_1DDI_VIDEO_INPUT, D3D11_1DDI_VIDEO_INPUT
req.iface: 
---

# D3D11_1DDI_VIDEO_INPUT structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_INPUT {
  BOOL                        Relocate;
  D3D11_1DDI_VIDEODEVICEFUNCS *p11VideoDeviceFuncs;
} D3D11_1DDI_VIDEO_INPUT;
````


## -struct-fields
<dl>

### -field <b>Relocate</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <b>p11VideoDeviceFuncs</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
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
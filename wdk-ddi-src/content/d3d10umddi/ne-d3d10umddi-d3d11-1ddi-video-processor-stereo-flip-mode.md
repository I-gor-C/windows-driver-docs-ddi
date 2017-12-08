---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
title: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
author: windows-driver-content
description: For stereo 3-D video, specifies whether the data in frame 0 or frame 1 is flipped, either horizontally or vertically.
old-location: display\d3d11_1ddi_video_processor_stereo_flip_mode.htm
old-project: display
ms.assetid: b385a0fd-6181-45c3-ba6e-e292e0b10e68
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
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

# D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE enumeration



## -description
<p>For stereo 3-D video, specifies whether the data in frame 0 or frame 1 is flipped, either horizontally or vertically.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE { 
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_NONE    = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0  = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1  = 2
} D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE;
````


## -enum-fields
<dl>

### -field D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_NONE

<dd>
<p>Neither frame is flipped.</p>
</dd>

### -field D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0

<dd>
<p>The data in frame 0 is flipped.</p>
</dd>

### -field D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1

<dd>
<p>The data in frame 1 is flipped.</p>
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
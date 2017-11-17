---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS
title: D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS
author: windows-driver-content
description: Specifies the automatic image processing capabilities of the video processor.
old-location: display\d3d11_1ddi_video_processor_auto_stream_caps.htm
ms.assetid: 00334dec-b84a-49d4-bd09-440eb7a1b79d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS enumeration



## -description
<p>Specifies the automatic image processing capabilities of the video processor.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS { 
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DENOISE              = 0x01,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DERINGING            = 0x02,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_EDGE_ENHANCEMENT     = 0x04,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_COLOR_CORRECTION     = 0x08,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_FLESH_TONE_MAPPING   = 0x10,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_IMAGE_STABILIZATION  = 0x20,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_SUPER_RESOLUTION     = 0x40,
  D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_ANAMORPHIC_SCALING   = 0x80
} D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DENOISE"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_denoise"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DENOISE</b>

<dd>
<p>Denoise.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DERINGING"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_deringing"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DERINGING</b>

<dd>
<p>Deringing.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_EDGE_ENHANCEMENT"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_edge_enhancement"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_EDGE_ENHANCEMENT</b>

<dd>
<p>Edge enhancement.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_COLOR_CORRECTION"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_color_correction"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_COLOR_CORRECTION</b>

<dd>
<p>Color correction.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_FLESH_TONE_MAPPING"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_flesh_tone_mapping"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_FLESH_TONE_MAPPING</b>

<dd>
<p>Flesh-tone mapping.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_IMAGE_STABILIZATION"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_image_stabilization"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_IMAGE_STABILIZATION</b>

<dd>
<p>Image stabilization.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_SUPER_RESOLUTION"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_super_resolution"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_SUPER_RESOLUTION</b>

<dd>
<p>Enhanced image resolution.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_ANAMORPHIC_SCALING"></a><a id="d3d11_1ddi_video_processor_auto_stream_caps_anamorphic_scaling"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_ANAMORPHIC_SCALING</b>

<dd>
<p>Anamorphic scaling.</p>
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
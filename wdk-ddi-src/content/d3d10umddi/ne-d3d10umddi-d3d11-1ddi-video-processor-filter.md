---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_FILTER
title: D3D11_1DDI_VIDEO_PROCESSOR_FILTER
author: windows-driver-content
description: Identifies a video processor filter.
old-location: display\d3d11_1ddi_video_processor_filter.htm
old-project: display
ms.assetid: 189ad1c2-3828-468a-a99d-12d85da6bf63
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_FILTER
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

# D3D11_1DDI_VIDEO_PROCESSOR_FILTER enumeration



## -description
<p>Identifies a video processor filter.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_FILTER { 
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_BRIGHTNESS          = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_CONTRAST            = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_HUE                 = 2,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_SATURATION          = 3,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_NOISE_REDUCTION     = 4,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_EDGE_ENHANCEMENT    = 5,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_ANAMORPHIC_SCALING  = 6,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_STEREO_ADJUSTMENT   = 7
} D3D11_1DDI_VIDEO_PROCESSOR_FILTER;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_BRIGHTNESS"></a><a id="d3d11_1ddi_video_processor_filter_brightness"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_BRIGHTNESS</b>

<dd>
<p>Brightness filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_CONTRAST"></a><a id="d3d11_1ddi_video_processor_filter_contrast"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_CONTRAST</b>

<dd>
<p>Contrast filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_HUE"></a><a id="d3d11_1ddi_video_processor_filter_hue"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_HUE</b>

<dd>
<p>Hue filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_SATURATION"></a><a id="d3d11_1ddi_video_processor_filter_saturation"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_SATURATION</b>

<dd>
<p>Saturation filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_NOISE_REDUCTION"></a><a id="d3d11_1ddi_video_processor_filter_noise_reduction"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_NOISE_REDUCTION</b>

<dd>
<p>Noise reduction filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_EDGE_ENHANCEMENT"></a><a id="d3d11_1ddi_video_processor_filter_edge_enhancement"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_EDGE_ENHANCEMENT</b>

<dd>
<p>Edge enhancement filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_ANAMORPHIC_SCALING"></a><a id="d3d11_1ddi_video_processor_filter_anamorphic_scaling"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_ANAMORPHIC_SCALING</b>

<dd>
<p>Anamorphic scaling filter.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FILTER_STEREO_ADJUSTMENT"></a><a id="d3d11_1ddi_video_processor_filter_stereo_adjustment"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FILTER_STEREO_ADJUSTMENT</b>

<dd>
<p>Stereo adjustment filter. When stereo 3-D video is enabled, this filter adjusts the offset between the left and right views, allowing the user to reduce potential eye strain.</p>
<p>The filter value indicates the amount by which the left and right views are adjusted. A positive value shifts the images away from each other: the left image toward the left, and the right image toward the right. A negative value shifts the images in the opposite directions, closer to each other.</p>
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
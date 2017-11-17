---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE
title: D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE
author: windows-driver-content
description: Defines the range of supported values for an image filter.
old-location: display\d3d11_1ddi_video_processor_filter_range.htm
ms.assetid: 9dc93d92-ccdc-488b-a5dd-a2efe783cbb3
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE
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
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE, D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE structure



## -description
<p>Defines the range of supported values for an image filter.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE {
  int   Minimum;
  int   Maximum;
  int   Default;
  float Multiplier;
} D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE;
````


## -struct-fields
<dl>

### -field <b>Minimum</b>

<dd>
<p>The minimum value of the filter.</p>
</dd>

### -field <b>Maximum</b>

<dd>
<p>The maximum value of the filter.</p>
</dd>

### -field <b>Default</b>

<dd>
<p>The default value of the filter.</p>
</dd>

### -field <b>Multiplier</b>

<dd>
<p>A multiplier. Use the following formula to translate the filter setting into the actual filter value: <i>Actual Value</i> = <i>Set Value</i> Ã— <i>Multiplier</i>.</p>
</dd>
</dl>

## -remarks
<p>The multiplier enables the filter range to have a fractional step value.</p>

<p>For example, a hue filter might have an actual range of [â€“180.0 … +180.0] with a step size of 0.25. The device would report the following range and multiplier:<ul>
<li>Minimum: â€“720</li>
<li>Maximum: +720</li>
<li>Multiplier: 0.25</li>
</ul>
</p>

<p>In this case, a filter value of 2 would be interpreted by the device as 0.50 (or 2 Ã— 0.25).</p>

<p>The device should use a multiplier that can be represented exactly as a base-2 fraction.</p>

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
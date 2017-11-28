---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE
title: D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE
author: windows-driver-content
description: Specifies the rate at which the video processor produces output frames from an input stream.
old-location: display\d3d11_1ddi_video_processor_output_rate.htm
old-project: display
ms.assetid: ff34c208-9b42-4f72-bb2a-43f3bb44fd68
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE
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

# D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE enumeration



## -description
<p>Specifies the rate at which the video processor produces output frames from an input stream.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE { 
  D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_NORMAL  = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_HALF    = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_CUSTOM  = 2
} D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_NORMAL"></a><a id="d3d11_1ddi_video_processor_output_rate_normal"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_NORMAL</b>

<dd>
<p>The output is the normal frame rate.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_HALF"></a><a id="d3d11_1ddi_video_processor_output_rate_half"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_HALF</b>

<dd>
<p>The output is half the frame rate.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_CUSTOM"></a><a id="d3d11_1ddi_video_processor_output_rate_custom"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_CUSTOM</b>

<dd>
<p>The output is a custom frame rate.</p>
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
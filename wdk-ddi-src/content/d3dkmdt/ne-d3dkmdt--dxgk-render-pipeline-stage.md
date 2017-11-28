---
UID: NE.d3dkmdt._DXGK_RENDER_PIPELINE_STAGE
title: DXGK_RENDER_PIPELINE_STAGE
author: windows-driver-content
description: The DXGK_RENDER_PIPELINE_STAGE enumeration describes the render pipeline stage during which the GPU error has occurred.
old-location: display\dxgk_render_pipeline_stage.htm
old-project: display
ms.assetid: A6E6439A-8151-4953-B78A-3141A9EA59F2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_RENDER_PIPELINE_STAGE
req.alt-loc: D3dkmdt.h
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

# DXGK_RENDER_PIPELINE_STAGE enumeration



## -description
<p>The <b>DXGK_RENDER_PIPELINE_STAGE</b> enumeration describes the render pipeline stage during which the GPU error has occurred.</p>


## -syntax

````
typedef enum _DXGK_RENDER_PIPELINE_STAGE { 
  DXGK_RENDER_PIPELINE_STAGE_UNKNOWN          = 0,
  DXGK_RENDER_PIPELINE_STAGE_INPUT_ASSEMBLER  = 1,
  DXGK_RENDER_PIPELINE_STAGE_VERTEX_SHADER    = 2,
  DXGK_RENDER_PIPELINE_STAGE_GEOMETRY_SHADER  = 3,
  DXGK_RENDER_PIPELINE_STAGE_STREAM_OUTPUT    = 4,
  DXGK_RENDER_PIPELINE_STAGE_RASTERIZER       = 5,
  DXGK_RENDER_PIPELINE_STAGE_PIXEL_SHADER     = 6,
  DXGK_RENDER_PIPELINE_STAGE_OUTPUT_MERGER    = 7
} DXGK_RENDER_PIPELINE_STAGE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_UNKNOWN"></a><a id="dxgk_render_pipeline_stage_unknown"></a><b>DXGK_RENDER_PIPELINE_STAGE_UNKNOWN</b>

<dd>
<p>Indicates that the stage where the error occurred is unknown.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_INPUT_ASSEMBLER"></a><a id="dxgk_render_pipeline_stage_input_assembler"></a><b>DXGK_RENDER_PIPELINE_STAGE_INPUT_ASSEMBLER</b>

<dd>
<p>Indicates that the error occurred at the input assembler stage.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_VERTEX_SHADER"></a><a id="dxgk_render_pipeline_stage_vertex_shader"></a><b>DXGK_RENDER_PIPELINE_STAGE_VERTEX_SHADER</b>

<dd>
<p>Indicates that the error occurred at the vertex shader stage.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_GEOMETRY_SHADER"></a><a id="dxgk_render_pipeline_stage_geometry_shader"></a><b>DXGK_RENDER_PIPELINE_STAGE_GEOMETRY_SHADER</b>

<dd>
<p>Indicates that the error occurred at the geometry shader stage.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_STREAM_OUTPUT"></a><a id="dxgk_render_pipeline_stage_stream_output"></a><b>DXGK_RENDER_PIPELINE_STAGE_STREAM_OUTPUT</b>

<dd>
<p>Indicates that the error occurred at the stream output stage.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_RASTERIZER"></a><a id="dxgk_render_pipeline_stage_rasterizer"></a><b>DXGK_RENDER_PIPELINE_STAGE_RASTERIZER</b>

<dd>
<p>Indicates that the error occurred at the rasterizer stage.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_PIXEL_SHADER"></a><a id="dxgk_render_pipeline_stage_pixel_shader"></a><b>DXGK_RENDER_PIPELINE_STAGE_PIXEL_SHADER</b>

<dd>
<p>Indicates that the error occurred at the pixel shader stage.</p>
</dd>

### -field <a id="DXGK_RENDER_PIPELINE_STAGE_OUTPUT_MERGER"></a><a id="dxgk_render_pipeline_stage_output_merger"></a><b>DXGK_RENDER_PIPELINE_STAGE_OUTPUT_MERGER</b>

<dd>
<p>Indicates that the error occurred at the output merger stage.</p>
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
<dt>D3dkmdt.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>
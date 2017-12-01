---
UID: NE.d3dumddi._DXVAHDDDI_STREAM_STATE
title: DXVAHDDDI_STREAM_STATE
author: windows-driver-content
description: The DXVAHDDDI_STREAM_STATE enumeration contains values that identify the stream-state data for a video processor.
old-location: display\dxvahdddi_stream_state.htm
old-project: display
ms.assetid: b84e80a3-5d04-4f8d-b469-c56e27e0ad34
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_STREAM_STATE is supported starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_STREAM_STATE
req.alt-loc: d3dumddi.h
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

# DXVAHDDDI_STREAM_STATE enumeration



## -description
<p>The DXVAHDDDI_STREAM_STATE enumeration contains values that identify the stream-state data for a video processor.</p>


## -syntax

````
typedef enum _DXVAHDDDI_STREAM_STATE { 
  DXVAHDDDI_STREAM_STATE_FRAME_FORMAT               = 1,
  DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE          = 2,
  DXVAHDDDI_STREAM_STATE_OUTPUT_RATE                = 3,
  DXVAHDDDI_STREAM_STATE_SOURCE_RECT                = 4,
  DXVAHDDDI_STREAM_STATE_DESTINATION_RECT           = 5,
  DXVAHDDDI_STREAM_STATE_ALPHA                      = 6,
  DXVAHDDDI_STREAM_STATE_PALETTE                    = 7,
  DXVAHDDDI_STREAM_STATE_LUMA_KEY                   = 8,
  DXVAHDDDI_STREAM_STATE_ASPECT_RATIO               = 9,
  DXVAHDDDI_STREAM_STATE_ROTATION                   = 10,
  DXVAHDDDI_STREAM_STATE_FILTER_BRIGHTNESS          = 100,
  DXVAHDDDI_STREAM_STATE_FILTER_CONTRAST            = 101,
  DXVAHDDDI_STREAM_STATE_FILTER_HUE                 = 102,
  DXVAHDDDI_STREAM_STATE_FILTER_SATURATION          = 103,
  DXVAHDDDI_STREAM_STATE_FILTER_NOISE_REDUCTION     = 104,
  DXVAHDDDI_STREAM_STATE_FILTER_EDGE_ENHANCEMENT    = 105,
  DXVAHDDDI_STREAM_STATE_FILTER_ANAMORPHIC_SCALING  = 106,
  DXVAHDDDI_STREAM_STATE_PRIVATE                    = 1000
} DXVAHDDDI_STREAM_STATE;
````


## -enum-fields
<dl>

### -field <a id="DXVAHDDDI_STREAM_STATE_FRAME_FORMAT"></a><a id="dxvahdddi_stream_state_frame_format"></a><b>DXVAHDDDI_STREAM_STATE_FRAME_FORMAT</b>

<dd>
<p>The stream-state data specifies the frame format of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-frame-format-data.md">DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE"></a><a id="dxvahdddi_stream_state_input_color_space"></a><b>DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE</b>

<dd>
<p>The stream-state data specifies the color space of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-input-color-space-data.md">DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_OUTPUT_RATE"></a><a id="dxvahdddi_stream_state_output_rate"></a><b>DXVAHDDDI_STREAM_STATE_OUTPUT_RATE</b>

<dd>
<p>The stream-state data specifies the output rate of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-output-rate-data.md">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_SOURCE_RECT"></a><a id="dxvahdddi_stream_state_source_rect"></a><b>DXVAHDDDI_STREAM_STATE_SOURCE_RECT</b>

<dd>
<p>The stream-state data specifies the source rectangle of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-source-rect-data.md">DXVAHDDDI_STREAM_STATE_SOURCE_RECT_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_DESTINATION_RECT"></a><a id="dxvahdddi_stream_state_destination_rect"></a><b>DXVAHDDDI_STREAM_STATE_DESTINATION_RECT</b>

<dd>
<p>The stream-state data specifies the destination rectangle in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-destination-rect-data.md">DXVAHDDDI_STREAM_STATE_DESTINATION_RECT_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_ALPHA"></a><a id="dxvahdddi_stream_state_alpha"></a><b>DXVAHDDDI_STREAM_STATE_ALPHA</b>

<dd>
<p>The stream-state data specifies the alpha blend level per-plane in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-alpha-data.md">DXVAHDDDI_STREAM_STATE_ALPHA_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_PALETTE"></a><a id="dxvahdddi_stream_state_palette"></a><b>DXVAHDDDI_STREAM_STATE_PALETTE</b>

<dd>
<p>The stream-state data specifies the palette entries of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-palette-data.md">DXVAHDDDI_STREAM_STATE_PALETTE_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_LUMA_KEY"></a><a id="dxvahdddi_stream_state_luma_key"></a><b>DXVAHDDDI_STREAM_STATE_LUMA_KEY</b>

<dd>
<p>The stream-state data specifies the luma key of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-luma-key-data.md">DXVAHDDDI_STREAM_STATE_LUMA_KEY_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_ASPECT_RATIO"></a><a id="dxvahdddi_stream_state_aspect_ratio"></a><b>DXVAHDDDI_STREAM_STATE_ASPECT_RATIO</b>

<dd>
<p>The stream-state data specifies the aspect ratio of the input in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-aspect-ratio-data.md">DXVAHDDDI_STREAM_STATE_ASPECT_RATIO_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_ROTATION"></a><a id="dxvahdddi_stream_state_rotation"></a><b>DXVAHDDDI_STREAM_STATE_ROTATION</b>

<dd>
<p>The stream-state data specifies the  clockwise rotation of the display output surface in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-rotation-data.md">DXVAHDDDI_STREAM_STATE_ROTATION_DATA</a> structure.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_BRIGHTNESS"></a><a id="dxvahdddi_stream_state_filter_brightness"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_BRIGHTNESS</b>

<dd>
<p>The stream-state data specifies the brightness ProcAmp level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_CONTRAST"></a><a id="dxvahdddi_stream_state_filter_contrast"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_CONTRAST</b>

<dd>
<p>The stream-state data specifies the contrast ProcAmp level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_HUE"></a><a id="dxvahdddi_stream_state_filter_hue"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_HUE</b>

<dd>
<p>The stream-state data specifies the hue ProcAmp level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_SATURATION"></a><a id="dxvahdddi_stream_state_filter_saturation"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_SATURATION</b>

<dd>
<p>The stream-state data specifies the saturation ProcAmp level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_NOISE_REDUCTION"></a><a id="dxvahdddi_stream_state_filter_noise_reduction"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_NOISE_REDUCTION</b>

<dd>
<p>The stream-state data specifies the noise reduction filter level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_EDGE_ENHANCEMENT"></a><a id="dxvahdddi_stream_state_filter_edge_enhancement"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_EDGE_ENHANCEMENT</b>

<dd>
<p>The stream-state data specifies the edge enhancement filter level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_FILTER_ANAMORPHIC_SCALING"></a><a id="dxvahdddi_stream_state_filter_anamorphic_scaling"></a><b>DXVAHDDDI_STREAM_STATE_FILTER_ANAMORPHIC_SCALING</b>

<dd>
<p>The stream-state data specifies the anamorphic scaling level in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a> structure. </p>
</dd>

### -field <a id="DXVAHDDDI_STREAM_STATE_PRIVATE"></a><a id="dxvahdddi_stream_state_private"></a><b>DXVAHDDDI_STREAM_STATE_PRIVATE</b>

<dd>
<p>The stream-state data specifies private parameters in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-private-data.md">DXVAHDDDI_STREAM_STATE_PRIVATE_DATA</a> structure. </p>
</dd>
</dl>

## -remarks
<p>A DXVAHDDDI_STREAM_STATE-typed value is specified in the <b>State</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-dxvahd-setvideoprocessstreamstate.md">D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE</a> structure in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessstreamstate.md">SetVideoProcessStreamState</a> function to set the stream state for a video processor. Stream-state data that corresponds to the supplied DXVAHDDDI_STREAM_STATE-typed value is pointed to by the <b>pData</b> member of D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_STREAM_STATE is supported starting with Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-dxvahd-setvideoprocessstreamstate.md">D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-alpha-data.md">DXVAHDDDI_STREAM_STATE_ALPHA_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-aspect-ratio-data.md">DXVAHDDDI_STREAM_STATE_ASPECT_RATIO_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-destination-rect-data.md">DXVAHDDDI_STREAM_STATE_DESTINATION_RECT_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-filter-data.md">DXVAHDDDI_STREAM_STATE_FILTER_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-frame-format-data.md">DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-input-color-space-data.md">DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-luma-key-data.md">DXVAHDDDI_STREAM_STATE_LUMA_KEY_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-output-rate-data.md">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-palette-data.md">DXVAHDDDI_STREAM_STATE_PALETTE_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-private-data.md">DXVAHDDDI_STREAM_STATE_PRIVATE_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-rotation-data.md">DXVAHDDDI_STREAM_STATE_ROTATION_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-source-rect-data.md">DXVAHDDDI_STREAM_STATE_SOURCE_RECT_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessstreamstate.md">SetVideoProcessStreamState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_STREAM_STATE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

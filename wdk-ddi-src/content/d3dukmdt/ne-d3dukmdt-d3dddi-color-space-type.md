---
UID: NE.d3dukmdt.D3DDDI_COLOR_SPACE_TYPE
title: D3DDDI_COLOR_SPACE_TYPE
author: windows-driver-content
description: Defines stream color space information.
old-location: display\d3dddi_color_space_type.htm
old-project: display
ms.assetid: 0A26F0AC-2D00-4847-96ED-3232A067F7CC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_COLOR_SPACE_TYPE
req.alt-loc: d3dukmdt.h
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

# D3DDDI_COLOR_SPACE_TYPE enumeration



## -description
<p>Defines stream color space information.</p>


## -syntax

````
typedef enum D3DDDI_COLOR_SPACE_TYPE { 
  D3DDDI_COLOR_SPACE_RGB_FULL_G22_NONE_P709            = 0,
  D3DDDI_COLOR_SPACE_RGB_FULL_G10_NONE_P709            = 1,
  D3DDDI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P709          = 2,
  D3DDDI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P2020         = 3,
  D3DDDI_COLOR_SPACE_RESERVED                          = 4,
  D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_NONE_P709_X601     = 5,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P601        = 6,
  D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P601          = 7,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P709        = 8,
  D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P709          = 9,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P2020       = 10,
  D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P2020         = 11,
  D3DDDI_COLOR_SPACE_RGB_FULL_G2084_NONE_P2020         = 12,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G2084_LEFT_P2020     = 13,
  D3DDDI_COLOR_SPACE_RGB_STUDIO_G2084_NONE_P2020       = 14,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_TOPLEFT_P2020    = 15,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G2084_TOPLEFT_P2020  = 16,
  DD3DDDI_COLOR_SPACE_RGB_FULL_G22_NONE_P2020          = 17,
  D3DDDI_COLOR_SPACE_YCBCR_STUDIO_GHLG_TOPLEFT_P2020   = 18,
  DD3DDDI_COLOR_SPACE_YCBCR_FULL_GHLG_TOPLEFT_P2020    = 19,
  D3DDDI_COLOR_SPACE_CUSTOM                            = 0xFFFFFFFF
} D3DDDI_COLOR_SPACE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_COLOR_SPACE_RGB_FULL_G22_NONE_P709"></a><a id="d3dddi_color_space_rgb_full_g22_none_p709"></a><b>D3DDDI_COLOR_SPACE_RGB_FULL_G22_NONE_P709</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Image</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.709</td>
</tr>
</table>
<p> </p>
<p>This is the standard definition for <i>sRGB</i>.
</p>
<p>Note that this is often implemented with a linear segment, but in that case the exponent is corrected to stay aligned with a gamma 2.2 curve. 

</p>
<p>This is usually used with 8 bit and 10 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_RGB_FULL_G10_NONE_P709"></a><a id="d3dddi_color_space_rgb_full_g10_none_p709"></a><b>D3DDDI_COLOR_SPACE_RGB_FULL_G10_NONE_P709</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>1.0</td>
</tr>
<tr>
<td>Costing</td>
<td>Image</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.709</td>
</tr>
</table>
<p> </p>
<p>This is the standard definition for <i>scRGB</i>.

</p>
<p>This is usually used with 16 bit integer, 16 bit floating point, and 32 bit floating point channels.
</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P709"></a><a id="d3dddi_color_space_rgb_studio_g22_none_p709"></a><b>D3DDDI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P709</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Image</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.709</td>
</tr>
</table>
<p> </p>
<p>This is the standard definition for <i>ITU-R Recommendation BT.709</i>.  Note that due to the inclusion of a linear segment, the transfer curve looks similar to a pure exponential gamma of 1.9. 

</p>
<p>This is usually used with 8 bit and 10 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P2020"></a><a id="d3dddi_color_space_rgb_studio_g22_none_p2020"></a><b>D3DDDI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Image</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
<p>This is usually used with 10, 12, or 16 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_RESERVED"></a><a id="d3dddi_color_space_reserved"></a><b>D3DDDI_COLOR_SPACE_RESERVED</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_NONE_P709_X601"></a><a id="d3dddi_color_space_ycbcr_full_g22_none_p709_x601"></a><b>D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_NONE_P709_X601</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Image</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.709</td>
</tr>
<tr>
<td>Transfer Matrix</td>
<td>BT.601</td>
</tr>
</table>
<p> </p>
<p>This definition is commonly used for <i>JPG</i>.

</p>
<p>This is usually used with 8, 10, 12, or 16 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P601"></a><a id="d3dddi_color_space_ycbcr_studio_g22_left_p601"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P601</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Video</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.601</td>
</tr>
</table>
<p> </p>
<p>This definition is commonly used for <i>MPEG2</i>.

</p>
<p>This is usually used with 8, 10, 12, or 16 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P601"></a><a id="d3dddi_color_space_ycbcr_full_g22_left_p601"></a><b>D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P601</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Video</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.601</td>
</tr>
</table>
<p> </p>
<p>This is sometimes used for <i>H.264</i> camera capture.

</p>
<p>This is usually used with 8, 10, 12, or 16 bit color channels.
</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P709"></a><a id="d3dddi_color_space_ycbcr_studio_g22_left_p709"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P709</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Video</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.709</td>
</tr>
</table>
<p> </p>
<p>This definition is commonly used for <i>H.264</i> and <i>HEVC</i>.

</p>
<p>This is usually used with 8, 10, 12, or 16 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P709"></a><a id="d3dddi_color_space_ycbcr_full_g22_left_p709"></a><b>D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P709</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Video</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.709</td>
</tr>
</table>
<p> </p>
<p>This is sometimes used for <i>H.264</i> camera capture.

</p>
<p>This is usually used with 8, 10, 12, or 16 bit color channels.
</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P2020"></a><a id="d3dddi_color_space_ycbcr_studio_g22_left_p2020"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Video</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
<p>This definition may be used by <i>HEVC</i>.

</p>
<p>This is usually used with 10, 12, or 16 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P2020"></a><a id="d3dddi_color_space_ycbcr_full_g22_left_p2020"></a><b>D3DDDI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Video</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
<p>This is usually used with 10, 12, or 16 bit color channels.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_RGB_FULL_G2084_NONE_P2020"></a><a id="d3dddi_color_space_rgb_full_g2084_none_p2020"></a><b>D3DDDI_COLOR_SPACE_RGB_FULL_G2084_NONE_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2084</td>
</tr>
<tr>
<td>Costing</td>
<td>Center</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G2084_LEFT_P2020"></a><a id="d3dddi_color_space_ycbcr_studio_g2084_left_p2020"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G2084_LEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2084</td>
</tr>
<tr>
<td>Costing</td>
<td>Left</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_RGB_STUDIO_G2084_NONE_P2020"></a><a id="d3dddi_color_space_rgb_studio_g2084_none_p2020"></a><b>D3DDDI_COLOR_SPACE_RGB_STUDIO_G2084_NONE_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2084</td>
</tr>
<tr>
<td>Costing</td>
<td>Center</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_TOPLEFT_P2020"></a><a id="d3dddi_color_space_ycbcr_studio_g22_topleft_p2020"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G22_TOPLEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>Top Left</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G2084_TOPLEFT_P2020"></a><a id="d3dddi_color_space_ycbcr_studio_g2084_topleft_p2020"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_G2084_TOPLEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>2084</td>
</tr>
<tr>
<td>Costing</td>
<td>Top Left</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="DD3DDDI_COLOR_SPACE_RGB_FULL_G22_NONE_P2020"></a><a id="dd3dddi_color_space_rgb_full_g22_none_p2020"></a><b>DD3DDDI_COLOR_SPACE_RGB_FULL_G22_NONE_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>RGB</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>2.2</td>
</tr>
<tr>
<td>Costing</td>
<td>None</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_YCBCR_STUDIO_GHLG_TOPLEFT_P2020"></a><a id="d3dddi_color_space_ycbcr_studio_ghlg_topleft_p2020"></a><b>D3DDDI_COLOR_SPACE_YCBCR_STUDIO_GHLG_TOPLEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>16-235</td>
</tr>
<tr>
<td>Gamma</td>
<td>HLG</td>
</tr>
<tr>
<td>Costing</td>
<td>Top Left</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
<p>This colorspace can be used as an input to the video processor DDIs, but will never be used to scan out.</p>
</dd>

### -field <a id="DD3DDDI_COLOR_SPACE_YCBCR_FULL_GHLG_TOPLEFT_P2020"></a><a id="dd3dddi_color_space_ycbcr_full_ghlg_topleft_p2020"></a><b>DD3DDDI_COLOR_SPACE_YCBCR_FULL_GHLG_TOPLEFT_P2020</b>

<dd>
<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>
<tr>
<td>Colorspace</td>
<td>YCbCr</td>
</tr>
<tr>
<td>Range</td>
<td>0-255</td>
</tr>
<tr>
<td>Gamma</td>
<td>HLG</td>
</tr>
<tr>
<td>Costing</td>
<td>Top Left</td>
</tr>
<tr>
<td>Primaries</td>
<td>BT.2020</td>
</tr>
</table>
<p> </p>
<p>This colorspace can be used as an input to the video processor DDIs, but will never be used to scan out.</p>
</dd>

### -field <a id="D3DDDI_COLOR_SPACE_CUSTOM"></a><a id="d3dddi_color_space_custom"></a><b>D3DDDI_COLOR_SPACE_CUSTOM</b>

<dd>
<p>A custom color definition is used. </p>
</dd>
</dl>

## -remarks
<p>
<p>The following color parameters are defined:</p>
</p>

<p>The following color parameters are defined:</p><dl>
<dt><a id="Colorspace"></a><a id="colorspace"></a><a id="COLORSPACE"></a>Colorspace</dt>
<dd>
<p>Defines the color space of the color channel data. </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>RGB</td>
<td>_RGB_</td>
<td>The red/green/blue color space color channel.</td>
</tr>
<tr>
<td>YCbCr</td>
<td>_YCBCR_</td>
<td>Three channel color model which splits luma (brightness) from chroma (color). YUV technically refers to analog signals and YCbCr to digital, but they are used interchangeably. </td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Range"></a><a id="range"></a><a id="RANGE"></a>Range</dt>
<dd>
<p>Indicates which integer range corresponds to the floating point [0..1] range of the data. For video, integer YCbCr data with ranges of [16..235] &amp; [8..247] are usually mapped to normalized YCbCr with a ranges of [0..1] &amp; [-0.5..0.5].   </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>0-255</td>
<td>_FULL_</td>
<td>PC desktop content and images.</td>
</tr>
<tr>
<td>16-235</td>
<td>_STUDIO_</td>
<td>Often used in video.</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Gamma"></a><a id="gamma"></a><a id="GAMMA"></a>Gamma</dt>
<dd>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>1.0</td>
<td>_G10_</td>
<td>Linear light levels.</td>
</tr>
<tr>
<td>2.2</td>
<td>_G22_</td>
<td>Commonly used for sRGB and BT.709 (linear segment + 2.222).</td>
</tr>
<tr>
<td>2.6</td>
<td>_G26_</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Costing"></a><a id="costing"></a><a id="COSTING"></a>Costing</dt>
<dd>
<p>Cositing indicates a horizontal or vertical shift of the chrominance channels relative to the luminance channel.   </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>Image</td>
<td>_NONE_</td>
<td>MPEG1, JPG</td>
</tr>
<tr>
<td>Video</td>
<td>_LEFT_</td>
<td>MPEG2, MPEG4</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Primaries"></a><a id="primaries"></a><a id="PRIMARIES"></a>Primaries</dt>
<dd>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>BT.601</td>
<td>_P601</td>
<td>Standard defining digital encoding of SDTV video.</td>
</tr>
<tr>
<td>BT.709</td>
<td>_P709</td>
<td>Standard defining digital encoding of HDTV video.</td>
</tr>
<tr>
<td>BT.2020</td>
<td>_P2020</td>
<td>Standard defining ultra-high definition television (UHDTV).</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Transfer_Matrix"></a><a id="transfer_matrix"></a><a id="TRANSFER_MATRIX"></a>Transfer Matrix</dt>
<dd>
<p>In most cases, the transfer matrix can be determined from the primaries. For some cases it must be explicitly specified as described below: </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>BT.601</td>
<td>_X601</td>
<td>Standard defining digital encoding of SDTV video.</td>
</tr>
<tr>
<td>BT.709</td>
<td>_X709</td>
<td>Standard defining digital encoding of HDTV video.</td>
</tr>
<tr>
<td>BT.2020</td>
<td>_X2020</td>
<td>Standard defining ultra-high definition television (UHDTV).</td>
</tr>
</table>
<p> </p>
</dd>
</dl><p>Defines the color space of the color channel data. </p>

<p> </p>

<p>Indicates which integer range corresponds to the floating point [0..1] range of the data. For video, integer YCbCr data with ranges of [16..235] &amp; [8..247] are usually mapped to normalized YCbCr with a ranges of [0..1] &amp; [-0.5..0.5].   </p>

<p> </p>

<p> </p>

<p>Cositing indicates a horizontal or vertical shift of the chrominance channels relative to the luminance channel.   </p>

<p> </p>

<p> </p>

<p>In most cases, the transfer matrix can be determined from the primaries. For some cases it must be explicitly specified as described below: </p>

<p> </p>

<p>Subsampling and the layout of the color channels are inferred from the surface format.</p>

<p>
<p>The following color parameters are defined:</p>
</p>

<p>The following color parameters are defined:</p><dl>
<dt><a id="Colorspace"></a><a id="colorspace"></a><a id="COLORSPACE"></a>Colorspace</dt>
<dd>
<p>Defines the color space of the color channel data. </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>RGB</td>
<td>_RGB_</td>
<td>The red/green/blue color space color channel.</td>
</tr>
<tr>
<td>YCbCr</td>
<td>_YCBCR_</td>
<td>Three channel color model which splits luma (brightness) from chroma (color). YUV technically refers to analog signals and YCbCr to digital, but they are used interchangeably. </td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Range"></a><a id="range"></a><a id="RANGE"></a>Range</dt>
<dd>
<p>Indicates which integer range corresponds to the floating point [0..1] range of the data. For video, integer YCbCr data with ranges of [16..235] &amp; [8..247] are usually mapped to normalized YCbCr with a ranges of [0..1] &amp; [-0.5..0.5].   </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>0-255</td>
<td>_FULL_</td>
<td>PC desktop content and images.</td>
</tr>
<tr>
<td>16-235</td>
<td>_STUDIO_</td>
<td>Often used in video.</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Gamma"></a><a id="gamma"></a><a id="GAMMA"></a>Gamma</dt>
<dd>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>1.0</td>
<td>_G10_</td>
<td>Linear light levels.</td>
</tr>
<tr>
<td>2.2</td>
<td>_G22_</td>
<td>Commonly used for sRGB and BT.709 (linear segment + 2.222).</td>
</tr>
<tr>
<td>2.6</td>
<td>_G26_</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Costing"></a><a id="costing"></a><a id="COSTING"></a>Costing</dt>
<dd>
<p>Cositing indicates a horizontal or vertical shift of the chrominance channels relative to the luminance channel.   </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>Image</td>
<td>_NONE_</td>
<td>MPEG1, JPG</td>
</tr>
<tr>
<td>Video</td>
<td>_LEFT_</td>
<td>MPEG2, MPEG4</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Primaries"></a><a id="primaries"></a><a id="PRIMARIES"></a>Primaries</dt>
<dd>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>BT.601</td>
<td>_P601</td>
<td>Standard defining digital encoding of SDTV video.</td>
</tr>
<tr>
<td>BT.709</td>
<td>_P709</td>
<td>Standard defining digital encoding of HDTV video.</td>
</tr>
<tr>
<td>BT.2020</td>
<td>_P2020</td>
<td>Standard defining ultra-high definition television (UHDTV).</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Transfer_Matrix"></a><a id="transfer_matrix"></a><a id="TRANSFER_MATRIX"></a>Transfer Matrix</dt>
<dd>
<p>In most cases, the transfer matrix can be determined from the primaries. For some cases it must be explicitly specified as described below: </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>BT.601</td>
<td>_X601</td>
<td>Standard defining digital encoding of SDTV video.</td>
</tr>
<tr>
<td>BT.709</td>
<td>_X709</td>
<td>Standard defining digital encoding of HDTV video.</td>
</tr>
<tr>
<td>BT.2020</td>
<td>_X2020</td>
<td>Standard defining ultra-high definition television (UHDTV).</td>
</tr>
</table>
<p> </p>
</dd>
</dl><p>Defines the color space of the color channel data. </p>

<p> </p>

<p>Indicates which integer range corresponds to the floating point [0..1] range of the data. For video, integer YCbCr data with ranges of [16..235] &amp; [8..247] are usually mapped to normalized YCbCr with a ranges of [0..1] &amp; [-0.5..0.5].   </p>

<p> </p>

<p> </p>

<p>Cositing indicates a horizontal or vertical shift of the chrominance channels relative to the luminance channel.   </p>

<p> </p>

<p> </p>

<p>In most cases, the transfer matrix can be determined from the primaries. For some cases it must be explicitly specified as described below: </p>

<p> </p>

<p>Subsampling and the layout of the color channels are inferred from the surface format.</p>

<p>
<p>The following color parameters are defined:</p>
</p>

<p>The following color parameters are defined:</p><dl>
<dt><a id="Colorspace"></a><a id="colorspace"></a><a id="COLORSPACE"></a>Colorspace</dt>
<dd>
<p>Defines the color space of the color channel data. </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>RGB</td>
<td>_RGB_</td>
<td>The red/green/blue color space color channel.</td>
</tr>
<tr>
<td>YCbCr</td>
<td>_YCBCR_</td>
<td>Three channel color model which splits luma (brightness) from chroma (color). YUV technically refers to analog signals and YCbCr to digital, but they are used interchangeably. </td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Range"></a><a id="range"></a><a id="RANGE"></a>Range</dt>
<dd>
<p>Indicates which integer range corresponds to the floating point [0..1] range of the data. For video, integer YCbCr data with ranges of [16..235] &amp; [8..247] are usually mapped to normalized YCbCr with a ranges of [0..1] &amp; [-0.5..0.5].   </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>0-255</td>
<td>_FULL_</td>
<td>PC desktop content and images.</td>
</tr>
<tr>
<td>16-235</td>
<td>_STUDIO_</td>
<td>Often used in video.</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Gamma"></a><a id="gamma"></a><a id="GAMMA"></a>Gamma</dt>
<dd>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>1.0</td>
<td>_G10_</td>
<td>Linear light levels.</td>
</tr>
<tr>
<td>2.2</td>
<td>_G22_</td>
<td>Commonly used for sRGB and BT.709 (linear segment + 2.222).</td>
</tr>
<tr>
<td>2.6</td>
<td>_G26_</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Costing"></a><a id="costing"></a><a id="COSTING"></a>Costing</dt>
<dd>
<p>Cositing indicates a horizontal or vertical shift of the chrominance channels relative to the luminance channel.   </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>Image</td>
<td>_NONE_</td>
<td>MPEG1, JPG</td>
</tr>
<tr>
<td>Video</td>
<td>_LEFT_</td>
<td>MPEG2, MPEG4</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Primaries"></a><a id="primaries"></a><a id="PRIMARIES"></a>Primaries</dt>
<dd>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>BT.601</td>
<td>_P601</td>
<td>Standard defining digital encoding of SDTV video.</td>
</tr>
<tr>
<td>BT.709</td>
<td>_P709</td>
<td>Standard defining digital encoding of HDTV video.</td>
</tr>
<tr>
<td>BT.2020</td>
<td>_P2020</td>
<td>Standard defining ultra-high definition television (UHDTV).</td>
</tr>
</table>
<p> </p>
</dd>
<dt><a id="Transfer_Matrix"></a><a id="transfer_matrix"></a><a id="TRANSFER_MATRIX"></a>Transfer Matrix</dt>
<dd>
<p>In most cases, the transfer matrix can be determined from the primaries. For some cases it must be explicitly specified as described below: </p>
<table>
<tr>
<th>Defined values</th>
<th>Notation in color space enumeration</th>
<th>Comments</th>
</tr>
<tr>
<td>BT.601</td>
<td>_X601</td>
<td>Standard defining digital encoding of SDTV video.</td>
</tr>
<tr>
<td>BT.709</td>
<td>_X709</td>
<td>Standard defining digital encoding of HDTV video.</td>
</tr>
<tr>
<td>BT.2020</td>
<td>_X2020</td>
<td>Standard defining ultra-high definition television (UHDTV).</td>
</tr>
</table>
<p> </p>
</dd>
</dl><p>Defines the color space of the color channel data. </p>

<p> </p>

<p>Indicates which integer range corresponds to the floating point [0..1] range of the data. For video, integer YCbCr data with ranges of [16..235] &amp; [8..247] are usually mapped to normalized YCbCr with a ranges of [0..1] &amp; [-0.5..0.5].   </p>

<p> </p>

<p> </p>

<p>Cositing indicates a horizontal or vertical shift of the chrominance channels relative to the luminance channel.   </p>

<p> </p>

<p> </p>

<p>In most cases, the transfer matrix can be determined from the primaries. For some cases it must be explicitly specified as described below: </p>

<p> </p>

<p>Subsampling and the layout of the color channels are inferred from the surface format.</p>

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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS
title: D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS
author: windows-driver-content
description: Defines capabilities related to input formats for a Microsoft Direct3D 11 video processor.
old-location: display\d3d11_1ddi_video_processor_format_caps.htm
ms.assetid: b0f36d4c-cf95-4d85-a2c8-267df618e0aa
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS
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

# D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS enumeration



## -description
<p>Defines capabilities related to input formats for a Microsoft Direct3D 11 video processor.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS { 
  D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_INTERLACED      = 0x1,
  D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_PROCAMP         = 0x2,
  D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_LUMA_KEY        = 0x4,
  D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED  = 0x8
} D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_INTERLACED"></a><a id="d3d11_1ddi_video_processor_format_caps_rgb_interlaced"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_INTERLACED</b>

<dd>
<p>The video processor can deinterlace an input stream that contains interlaced RGB video.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_PROCAMP"></a><a id="d3d11_1ddi_video_processor_format_caps_rgb_procamp"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_PROCAMP</b>

<dd>
<p>The video processor can perform color adjustment on RGB video.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_LUMA_KEY"></a><a id="d3d11_1ddi_video_processor_format_caps_rgb_luma_key"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_LUMA_KEY</b>

<dd>
<p>The video processor can perform luma keying on RGB video.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED"></a><a id="d3d11_1ddi_video_processor_format_caps_palette_interlaced"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED</b>

<dd>
<p>The video processor can deinterlace input streams with palettized color formats.</p>
</dd>
</dl>

## -remarks
<p>These flags define video processing capabilities that usually are not needed, and that video devices are therefore not required to support.</p>

<p>The first three flags relate to RGB support for functions that are normally applied to YCbCr video: deinterlacing, color adjustment, and luma keying. A device that supports these functions for YCbCr is not required to support them for RGB input. Supporting RGB input for these functions is an additional capability, reflected by these constants. Note that the driver might convert the input to another color space, perform the indicated function, and then convert the result back to RGB</p>

<p>Similarly, a device that supports deinterlacing is not required to support deinterlacing of palettized formats. This capability is indicated by the <b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED</b>  enumeration value.</p>

<p>These flags define video processing capabilities that usually are not needed, and that video devices are therefore not required to support.</p>

<p>The first three flags relate to RGB support for functions that are normally applied to YCbCr video: deinterlacing, color adjustment, and luma keying. A device that supports these functions for YCbCr is not required to support them for RGB input. Supporting RGB input for these functions is an additional capability, reflected by these constants. Note that the driver might convert the input to another color space, perform the indicated function, and then convert the result back to RGB</p>

<p>Similarly, a device that supports deinterlacing is not required to support deinterlacing of palettized formats. This capability is indicated by the <b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED</b>  enumeration value.</p>

<p>These flags define video processing capabilities that usually are not needed, and that video devices are therefore not required to support.</p>

<p>The first three flags relate to RGB support for functions that are normally applied to YCbCr video: deinterlacing, color adjustment, and luma keying. A device that supports these functions for YCbCr is not required to support them for RGB input. Supporting RGB input for these functions is an additional capability, reflected by these constants. Note that the driver might convert the input to another color space, perform the indicated function, and then convert the result back to RGB</p>

<p>Similarly, a device that supports deinterlacing is not required to support deinterlacing of palettized formats. This capability is indicated by the <b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED</b>  enumeration value.</p>

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
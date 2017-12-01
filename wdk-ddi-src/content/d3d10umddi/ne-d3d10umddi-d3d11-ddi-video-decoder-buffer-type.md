---
UID: NE.d3d10umddi.D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE
title: D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE
author: windows-driver-content
description: Contains values that indicate the buffer type used by the video decoder.
old-location: display\d3d11_ddi_video_decoder_buffer_type.htm
old-project: display
ms.assetid: 71d624ba-bac6-4055-a772-fe2280a9ee16
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
req.alt-api: D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE
req.alt-loc: d3d10umddi.h
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

# D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE enumeration



## -description
<p>Contains values that indicate the  buffer type used by the video decoder.</p>


## -syntax

````
typedef enum D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE { 
  D3D11_1DDI_VIDEO_DECODER_BUFFER_UNKNOWN                      = 0,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_PICTURE_PARAMETERS           = 1,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_MACROBLOCK_CONTROL           = 2,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_RESIDUAL_DIFFERENCE          = 3,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_DEBLOCKING_CONTROL           = 4,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_INVERSE_QUANTIZATION_MATRIX  = 5,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_SLICE_CONTROL                = 6,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_BITSTREAM                    = 7,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_MOTION_VECTOR                = 8,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_FILM_GRAIN                   = 9
} D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_UNKNOWN"></a><a id="d3d11_1ddi_video_decoder_buffer_unknown"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_UNKNOWN</b>

<dd>
<p>An unknown buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_PICTURE_PARAMETERS"></a><a id="d3d11_1ddi_video_decoder_buffer_picture_parameters"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_PICTURE_PARAMETERS</b>

<dd>
<p>Picture parameters decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_MACROBLOCK_CONTROL"></a><a id="d3d11_1ddi_video_decoder_buffer_macroblock_control"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_MACROBLOCK_CONTROL</b>

<dd>
<p>Macroblock control command decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_RESIDUAL_DIFFERENCE"></a><a id="d3d11_1ddi_video_decoder_buffer_residual_difference"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_RESIDUAL_DIFFERENCE</b>

<dd>
<p>Residual block difference decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_DEBLOCKING_CONTROL"></a><a id="d3d11_1ddi_video_decoder_buffer_deblocking_control"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_DEBLOCKING_CONTROL</b>

<dd>
<p>Deblocking filter control command decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_INVERSE_QUANTIZATION_MATRIX"></a><a id="d3d11_1ddi_video_decoder_buffer_inverse_quantization_matrix"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_INVERSE_QUANTIZATION_MATRIX</b>

<dd>
<p>Inverse-quantization matrix decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_SLICE_CONTROL"></a><a id="d3d11_1ddi_video_decoder_buffer_slice_control"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_SLICE_CONTROL</b>

<dd>
<p>Slice-control decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_BITSTREAM"></a><a id="d3d11_1ddi_video_decoder_buffer_bitstream"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_BITSTREAM</b>

<dd>
<p>Bitstream data decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_MOTION_VECTOR"></a><a id="d3d11_1ddi_video_decoder_buffer_motion_vector"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_MOTION_VECTOR</b>

<dd>
<p>Motion-vector decode compressed buffer format.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_DECODER_BUFFER_FILM_GRAIN"></a><a id="d3d11_1ddi_video_decoder_buffer_film_grain"></a><b>D3D11_1DDI_VIDEO_DECODER_BUFFER_FILM_GRAIN</b>

<dd>
<p>Film-grain decode compressed buffer format.</p>
</dd>
</dl>

## -remarks
<p>Note that the <b>D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</b> and <b>D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE</b> enumerations are defined as the same type.</p>

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

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createresource.md">D3D11DDIARG_CREATERESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NC.d3d10umddi.PFND3D10DDI_CHECKFORMATSUPPORT
title: PFND3D10DDI_CHECKFORMATSUPPORT
author: windows-driver-content
description: Retrieves the capabilities that the device has with the specified format.
old-location: display\checkformatsupport.htm
old-project: display
ms.assetid: 463ab1e5-08b1-45a1-b7d8-bdfacb3d4bdb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CheckFormatSupport
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

# PFND3D10DDI_CHECKFORMATSUPPORT callback



## -description
<p>Retrieves the capabilities that the device has with the specified format.</p>


## -prototype

````
PFND3D10DDI_CHECKFORMATSUPPORT CheckFormatSupport;

VOID APIENTRY CheckFormatSupport(
  _In_  D3D10DDI_HDEVICE hDevice,
  _In_  DXGI_FORMAT      Format,
  _Out_ UINT             *pFormatCaps
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>Format</i> [in]

<dd>
<p> A -typed value of type <a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a> indicates the pixel format to retrieve capabilities for. </p>
</dd>

### -param <i>pFormatCaps</i> [out]

<dd>
<p>A pointer to a variable that receives a valid bitwise <b>OR</b> of the following values that indicate the capabilities.</p>
<dl class="indent">

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_SHADER_SAMPLE"></a><a id="d3d10_ddi_format_support_shader_sample"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_SHADER_SAMPLE"></a><a id="d3d10_ddi_format_support_shader_sample"></a><b>D3D10_DDI_FORMAT_SUPPORT_SHADER_SAMPLE</b> (0x00000001)</p>


<dd>
<p>The format can be sampled with any filter in shaders.</p>
</dd>

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_RENDERTARGET"></a><a id="d3d10_ddi_format_support_rendertarget"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_RENDERTARGET"></a><a id="d3d10_ddi_format_support_rendertarget"></a><b>D3D10_DDI_FORMAT_SUPPORT_RENDERTARGET</b> (0x00000002)</p>


<dd>
<p>The format can be a render target.</p>
</dd>

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_BLENDABLE"></a><a id="d3d10_ddi_format_support_blendable"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_BLENDABLE"></a><a id="d3d10_ddi_format_support_blendable"></a><b>D3D10_DDI_FORMAT_SUPPORT_BLENDABLE</b> (0x00000004)</p>


<dd>
<p>The format is blendable. (You can set this value only if the format can be a render target.)</p>
</dd>

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET"></a><a id="d3d10_ddi_format_support_multisample_rendertarget"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET"></a><a id="d3d10_ddi_format_support_multisample_rendertarget"></a><b>D3D10_DDI_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET</b> (0x00000008)</p>


<dd>
<p>The format can be a render target with a sample count that is greater than one.</p>
</dd>

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_MULTISAMPLE_LOAD"></a><a id="d3d10_ddi_format_support_multisample_load"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_MULTISAMPLE_LOAD"></a><a id="d3d10_ddi_format_support_multisample_load"></a><b>D3D10_DDI_FORMAT_SUPPORT_MULTISAMPLE_LOAD</b> (0x00000010)</p>


<dd>
<p>The format can be used for reading individual samples from multiple-sample resources.</p>
</dd>

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_NOT_SUPPORTED"></a><a id="d3d10_ddi_format_support_not_supported"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_NOT_SUPPORTED"></a><a id="d3d10_ddi_format_support_not_supported"></a><b>D3D10_DDI_FORMAT_SUPPORT_NOT_SUPPORTED</b> (0x80000000)</p>


<dd>
<p>The display device does not support the format at all. This value is currently only valid for the <b>DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM</b>  format. If the driver sets this value, the driver must not set any of the other values.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_DECODER_OUTPUT"></a><a id="d3d11_1ddi_format_support_decoder_output"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_DECODER_OUTPUT"></a><a id="d3d11_1ddi_format_support_decoder_output"></a><b>D3D11_1DDI_FORMAT_SUPPORT_DECODER_OUTPUT</b> (0x00000020)</p>


<dd>
<p>The format can be supported as a decode output resource.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_VIDEO_PROCESSOR_OUTPUT"></a><a id="d3d11_1ddi_format_support_video_processor_output"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_VIDEO_PROCESSOR_OUTPUT"></a><a id="d3d11_1ddi_format_support_video_processor_output"></a><b>D3D11_1DDI_FORMAT_SUPPORT_VIDEO_PROCESSOR_OUTPUT</b> (0x00000040)</p>


<dd>
<p>The format can be a video processor output resource.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_VIDEO_PROCESSOR_INPUT"></a><a id="d3d11_1ddi_format_support_video_processor_input"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_VIDEO_PROCESSOR_INPUT"></a><a id="d3d11_1ddi_format_support_video_processor_input"></a><b>D3D11_1DDI_FORMAT_SUPPORT_VIDEO_PROCESSOR_INPUT</b> (0x00000080)</p>


<dd>
<p>The format can be a video processor input resource.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_VERTEX_BUFFER"></a><a id="d3d11_1ddi_format_support_vertex_buffer"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_VERTEX_BUFFER"></a><a id="d3d11_1ddi_format_support_vertex_buffer"></a><b>D3D11_1DDI_FORMAT_SUPPORT_VERTEX_BUFFER</b> (0x00000100)</p>


<dd>
<p>The format can be a vertex buffer.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_UAV_WRITES"></a><a id="d3d11_1ddi_format_support_uav_writes"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_UAV_WRITES"></a><a id="d3d11_1ddi_format_support_uav_writes"></a><b>D3D11_1DDI_FORMAT_SUPPORT_UAV_WRITES</b> (0x00000200)</p>


<dd>
<p>The format can be written through an unordered access view (UAV) append buffer.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_BUFFER"></a><a id="d3d11_1ddi_format_support_buffer"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_BUFFER"></a><a id="d3d11_1ddi_format_support_buffer"></a><b>D3D11_1DDI_FORMAT_SUPPORT_BUFFER</b> (0x00000400)</p>


<dd>
<p>The format can be used in a typed Buffer view.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_CAPTURE"></a><a id="d3d11_1ddi_format_support_capture"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_CAPTURE"></a><a id="d3d11_1ddi_format_support_capture"></a><b>D3D11_1DDI_FORMAT_SUPPORT_CAPTURE</b> (0x00000800)</p>


<dd>
<p>The format can be supported as an output to the video capture engine.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_VIDEO_ENCODER"></a><a id="d3d11_1ddi_format_support_video_encoder"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_VIDEO_ENCODER"></a><a id="d3d11_1ddi_format_support_video_encoder"></a><b>D3D11_1DDI_FORMAT_SUPPORT_VIDEO_ENCODER</b> (0x00001000)</p>


<dd>
<p>The format can be supported as an input to a hardware-encode Media Foundation Transform (MFT).</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_OUTPUT_MERGER_LOGIC_OP"></a><a id="d3d11_1ddi_format_support_output_merger_logic_op"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_OUTPUT_MERGER_LOGIC_OP"></a><a id="d3d11_1ddi_format_support_output_merger_logic_op"></a><b>D3D11_1DDI_FORMAT_SUPPORT_OUTPUT_MERGER_LOGIC_OP</b> (0x00002000)</p>


<dd>
<p>The format supports shader logic operations.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_SHADER_GATHER"></a><a id="d3d11_1ddi_format_support_shader_gather"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_SHADER_GATHER"></a><a id="d3d11_1ddi_format_support_shader_gather"></a><b>D3D11_1DDI_FORMAT_SUPPORT_SHADER_GATHER</b> (0x00004000)</p>


<dd>
<p>The format supports "Shader gather4" resource attributes.</p>
<p>Available starting with Windows 8.</p>
</dd>

### -param <a id="D3D11_1DDI_FORMAT_SUPPORT_MULTIPLANE_OVERLAY"></a><a id="d3d11_1ddi_format_support_multiplane_overlay"></a><p><a id="D3D11_1DDI_FORMAT_SUPPORT_MULTIPLANE_OVERLAY"></a><a id="d3d11_1ddi_format_support_multiplane_overlay"></a><b>D3D11_1DDI_FORMAT_SUPPORT_MULTIPLANE_OVERLAY</b> (0x00008000)</p>


<dd>
<p>The format supports multiplane overlays.</p>
<p>Available starting with Windows 8. However, multiplane overlays are supported only in WDDM 1.3 and later drivers, which were introduced with Windows 8.1.</p>
</dd>

### -param <a id="D3DWDDM1_3DDI_FORMAT_SUPPORT_TILED"></a><a id="d3dwddm1_3ddi_format_support_tiled"></a><p><a id="D3DWDDM1_3DDI_FORMAT_SUPPORT_TILED"></a><a id="d3dwddm1_3ddi_format_support_tiled"></a><b>D3DWDDM1_3DDI_FORMAT_SUPPORT_TILED</b> (0x00010000)</p>


<dd>
<p>The format supports use in a tiled resource of type <b>D3D10DDIRESOURCE_TEXTURE1D</b>, <b>D3D10DDIRESOURCE_TEXTURE2D</b>, or <b>D3D10DDIRESOURCE_TEXTURECUBE</b>.</p>
<p>Available starting with Windows 8.1, and supported only by WDDM 1.3 and later drivers.</p>
</dd>

### -param <a id="D3D10_DDI_FORMAT_SUPPORT_NOT_SUPPORTED"></a><a id="d3d10_ddi_format_support_not_supported"></a><p><a id="D3D10_DDI_FORMAT_SUPPORT_NOT_SUPPORTED"></a><a id="d3d10_ddi_format_support_not_supported"></a><b>D3D10_DDI_FORMAT_SUPPORT_NOT_SUPPORTED</b> (0x80000000)</p>


<dd>
<p>The format is not supported at all. This value is valid only for the following formats:</p>
<dl>
<dd><b>DXGI_FORMAT_A8P8</b></dd>
<dd><b>DXGI_FORMAT_AI44</b></dd>
<dd><b>DXGI_FORMAT_AYUV</b></dd>
<dd><b>DXGI_FORMAT_IA44</b></dd>
<dd><b>DXGI_FORMAT_NV11</b></dd>
<dd><b>DXGI_FORMAT_P010

</b></dd>
<dd><b>DXGI_FORMAT_P016</b></dd>
<dd><b>DXGI_FORMAT_P8

</b></dd>
<dd><b>DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM</b></dd>
<dd><b>DXGI_FORMAT_Y210</b></dd>
<dd><b>DXGI_FORMAT_Y216</b></dd>
<dd><b>DXGI_FORMAT_Y410</b></dd>
<dd><b>DXGI_FORMAT_Y416</b></dd>
</dl>
<p>For these formats, only this bit should be set.</p>
<p>Available starting with Windows 8.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None.</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see  Remarks .</p>

## -remarks
<p>The driver can call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function to set <b>E_FAIL</b> if the format in the <i>Format</i> parameter does not exist or can set <b>E_INVALIDARG</b> if the <i>pFormatCaps</i> parameter is <b>NULL</b>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2aef590f-2328-4175-ab60-c72b1fd83db7">DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CHECKFORMATSUPPORT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

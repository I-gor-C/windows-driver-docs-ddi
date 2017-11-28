---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE
title: D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE
author: windows-driver-content
description: Specifies the alpha fill mode for video processing.
old-location: display\d3d11_1ddi_video_processor_alpha_fill_mode.htm
old-project: display
ms.assetid: 22b50f49-821a-407e-89c0-fe7d637664fa
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE
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

# D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE enumeration



## -description
<p>Specifies the alpha fill mode for video processing.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE { 
  D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE         = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_BACKGROUND     = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_DESTINATION    = 2,
  D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_SOURCE_STREAM  = 3
} D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE"></a><a id="d3d11_1ddi_video_processor_alpha_fill_mode_opaque"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE</b>

<dd>
<p>Alpha values inside the target rectangle are set to opaque. 

</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_BACKGROUND"></a><a id="d3d11_1ddi_video_processor_alpha_fill_mode_background"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_BACKGROUND</b>

<dd>
<p>Alpha values inside the target rectangle are set to the alpha value specified in the background color. To set the background color, call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn459003">VideoProcessorSetOutputBackgroundColor</a> function.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_DESTINATION"></a><a id="d3d11_1ddi_video_processor_alpha_fill_mode_destination"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_DESTINATION</b>

<dd>
<p>Existing alpha values remain unchanged in the output surface.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_SOURCE_STREAM"></a><a id="d3d11_1ddi_video_processor_alpha_fill_mode_source_stream"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE_SOURCE_STREAM</b>

<dd>
<p>Alpha values are taken from an input stream, scaled, and copied to the corresponding destination rectangle for that stream. The input stream is specified in the <i>StreamIndex</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439778">VideoProcessorSetOutputAlphaFillMode</a> function.</p>
<p>If the input stream does not have alpha data, the video processor sets the alpha values in the target rectangle to opaque. If the input stream is disabled or the source rectangle is empty, the alpha values in the target rectangle are not modified.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439778">VideoProcessorSetOutputAlphaFillMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn459003">VideoProcessorSetOutputBackgroundColor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

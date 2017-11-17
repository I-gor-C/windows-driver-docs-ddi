---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC
title: D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC
author: windows-driver-content
description: Describes a video stream for a video processor.
old-location: display\d3d11_1ddi_video_processor_content_desc.htm
ms.assetid: f624ffc4-3313-46a3-9231-15a54c3f2791
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC
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
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC, D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC structure



## -description
<p>Describes a video stream for a video processor.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC {
  D3D11_1DDI_VIDEO_FRAME_FORMAT InputFrameFormat;
  DXGI_RATIONAL                 InputFrameRate;
  UINT                          InputWidth;
  UINT                          InputHeight;
  DXGI_RATIONAL                 OutputFrameRate;
  UINT                          OutputWidth;
  UINT                          OutputHeight;
  D3D11_1DDI_VIDEO_USAGE        Usage;
} D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC;
````


## -struct-fields
<dl>

### -field <b>InputFrameFormat</b>

<dd>
<p>A member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450954">D3D11_1DDI_VIDEO_FRAME_FORMAT</a> enumeration that describes how the video stream is interlaced.</p>
</dd>

### -field <b>InputFrameRate</b>

<dd>
<p>The frame rate of the input video stream, specified as a <a href="direct3ddxgi.dxgi_rational">DXGI_RATIONAL</a> structure.</p>
</dd>

### -field <b>InputWidth</b>

<dd>
<p>The width of the input frames, in pixels.</p>
</dd>

### -field <b>InputHeight</b>

<dd>
<p>The height of the input frames, in pixels.</p>
</dd>

### -field <b>OutputFrameRate</b>

<dd>
<p>The frame rate of the output video stream, specified as a <a href="direct3ddxgi.dxgi_rational">DXGI_RATIONAL</a> structure.</p>
</dd>

### -field <b>OutputWidth</b>

<dd>
<p>The width of the output frames, in pixels.</p>
</dd>

### -field <b>OutputHeight</b>

<dd>
<p>The height of the output frames, in pixels.</p>
</dd>

### -field <b>Usage</b>

<dd>
<p>A member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451037">D3D11_1DDI_VIDEO_USAGE</a> enumeration that describes how the video processor will be used. The value indicates the desired trade-off between speed and video quality. The driver uses this flag as a hint when it creates the video processor.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450954">D3D11_1DDI_VIDEO_FRAME_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451037">D3D11_1DDI_VIDEO_USAGE</a>
</dt>
<dt>
<a href="direct3ddxgi.dxgi_rational">DXGI_RATIONAL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

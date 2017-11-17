---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING
title: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING
author: windows-driver-content
description: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING describes the details of a video decoder downsampling operation.
old-location: display\d3dwddm2_0ddi_video_capability_decoder_downsampling.htm
ms.assetid: 8D12F2AC-2A64-4FEF-813C-15899FBCA108
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING
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
ms.keywords: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING, D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING
req.iface: 
---

# D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING structure



## -description
<p><b>D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING</b> describes the details of a video decoder downsampling operation.</p>


## -syntax

````
typedef struct D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING {
  const D3D11_1DDI_VIDEO_DECODER_DESC   *pInputDesc;
  D3DDDI_COLOR_SPACE_TYPE               InputColorSpace;
  const D3D11_1DDI_VIDEO_DECODER_CONFIG *pInputConfig;
  const DXGI_RATIONAL                   *pFrameRate;
  const D3D11_1DDI_VIDEO_DECODER_DESC   *pOutputDesc;
  D3DDDI_COLOR_SPACE_TYPE               OutputColorSpace;
  BOOL                                  Supported;
  BOOL                                  RealTime;
} D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING;
````


## -struct-fields
<dl>

### -field <b>pInputDesc</b>

<dd>
<p>[in] Contains the decode profile used and the resolution and format of the reference frames.  This is the resolution/format to be downsampled (e.g. 4K, DXGI_FORMAT_P010).</p>
</dd>

### -field <b>InputColorSpace</b>

<dd>
<p>[in] Contains the color space information of the reference frame data.</p>
</dd>

### -field <b>pInputConfig</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh450947">D3D11_1DDI_VIDEO_DECODER_CONFIG</a> structure that contains the configuration data associated with the decode profile .</p>
</dd>

### -field <b>pFrameRate</b>

<dd>
<p>[in] Contains the frame rate of the video content.</p>
</dd>

### -field <b>pOutputDesc</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh450951">D3D11_1DDI_VIDEO_DECODER_DESC</a> structure that contains the resolution and the format of the display frames.  This is the destination resolution and format of the down sample operation.

</p>
<div class="alert"><b>Note</b>  The decode profile (<b>Guid</b>) member of <b>pOutputDesc</b> can be ignored.
</div>
<div> </div>
</dd>

### -field <b>OutputColorSpace</b>

<dd>
<p>[in] Contains the color space information of the display frame data.</p>
</dd>

### -field <b>Supported</b>

<dd>
<p>[out] The driver sets this to <b>TRUE</b> if the requested down sampling is supported.  Otherwise, the driver should set this to <b>FALSE</b>.</p>
</dd>

### -field <b>RealTime</b>

<dd>
<p>[out] The driver sets this to <b>TRUE</b> if the requested down sampling is supported and the resulting decode operations can occur in real-time.  Otherwise, the driver should set this to <b>FALSE</b>.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450947">D3D11_1DDI_VIDEO_DECODER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450951">D3D11_1DDI_VIDEO_DECODER_DESC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906320">D3DDDI_COLOR_SPACE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

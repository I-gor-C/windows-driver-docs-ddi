---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_COLOR
title: D3D11_1DDI_VIDEO_COLOR
author: windows-driver-content
description: Defines a color value for Microsoft Direct3D 11 video.
old-location: display\d3d11_1ddi_video_color.htm
ms.assetid: 200ca1d5-cbfd-4ad8-aa41-8238ea7ea5cf
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
req.alt-api: D3D11_1DDI_VIDEO_COLOR
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
ms.keywords: D3D11_1DDI_VIDEO_COLOR, D3D11_1DDI_VIDEO_COLOR
req.iface: 
---

# D3D11_1DDI_VIDEO_COLOR structure



## -description
<p>Defines a color value for Microsoft Direct3D 11 video.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_COLOR {
  union {
    D3D11_1DDI_VIDEO_COLOR_YCbCrA YCbCr;
    D3D11_1DDI_VIDEO_COLOR_RGBA   RGBA;
  };
} D3D11_1DDI_VIDEO_COLOR;
````


## -struct-fields
<dl>

### -field <b>YCbCr</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh450932">D3D11_1DDI_VIDEO_COLOR_YCbCrA</a> structure that contains a YCbCr color value.</p>
</dd>

### -field <b>RGBA</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh450928">D3D11_1DDI_VIDEO_COLOR_RGBA</a> structure that contains an RGB color value.</p>
</dd>
</dl>

## -remarks
<p>The anonymous union can represent both RGB and YCbCr colors. The interpretation of the union depends on the context.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450928">D3D11_1DDI_VIDEO_COLOR_RGBA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450932">D3D11_1DDI_VIDEO_COLOR_YCbCrA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_COLOR structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

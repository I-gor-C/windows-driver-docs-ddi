---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO
title: D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO
author: windows-driver-content
description: Specifies information about a video decoder buffer.
old-location: display\d3d11_1ddi_video_decoder_buffer_info.htm
old-project: display
ms.assetid: 1f013077-ea85-4c35-8667-cdf0c1353b0f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO, D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO
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

# D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO structure



## -description
<p>Specifies information about a video decoder buffer.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO {
  D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE Type;
  UINT                                 Size;
  UINT                                 Usage;
} D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of buffer, specified as a constant value of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451066">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a> enumeration.</p>
<p>In D3d10umddi.h, <a href="https://msdn.microsoft.com/library/windows/hardware/hh451066">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a> and <b>D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE</b> are defined as the same type.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of the buffer, in bytes.</p>
</dd>

### -field <b>Usage</b>

<dd>
<p>A value from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451037">D3D11_1DDI_VIDEO_USAGE</a> enumeration that identifies how the decode device plays video.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451037">D3D11_1DDI_VIDEO_USAGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451066">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

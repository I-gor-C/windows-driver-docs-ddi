---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT
title: D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT
author: windows-driver-content
description: Specifies how a video format can be used for video processing.
old-location: display\d3d11_1ddi_video_processor_format_support.htm
ms.assetid: 3fef0cb0-6584-487d-9660-1c748509a6a9
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
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT
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

# D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT enumeration



## -description
<p>Specifies how a video format can be used for video processing.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT { 
  D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT_INPUT   = 0x00000001,
  D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT_OUTPUT  = 0x00000002
} D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT_INPUT"></a><a id="d3d11_1ddi_video_processor_format_support_input"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT_INPUT</b>

<dd>
<p>The format can be used as the input to the video processor.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT_OUTPUT"></a><a id="d3d11_1ddi_video_processor_format_support_output"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT_OUTPUT</b>

<dd>
<p>The format can be used as the output from the video processor.</p>
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
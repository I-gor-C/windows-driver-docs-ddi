---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_DECODE_FRAME_0030
title: PFND3D12DDI_VIDEO_DECODE_FRAME_0030
author: windows-driver-content
description: Used to decode a video frame.
old-location: display\pfnd3d12ddi_video_decode_frame_0030.htm
ms.assetid: 6BC35C7C-8E27-45FF-B406-BCE6E486E115
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_VIDEO_DECODE_FRAME_0030
req.alt-loc: d3d12umddi.h
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# PFND3D12DDI_VIDEO_DECODE_FRAME_0030 callback



## -description
<p>Used to decode a video frame.</p>


## -prototype

````
VOID APIENTRY* PFND3D12DDI_VIDEO_DECODE_FRAME_0030(
         D3D12DDI_HCOMMANDLIST                              hDrvCommandList,
         D3D12DDI_HVIDEODECODER_0020                        hDrvDecoder,
         UINT64                                             SubmissionID,
   const D3D12DDI_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS_0021 *pOutputStreamParameters,
   const D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030  *pInputStreamParameters
);
````


## -parameters
<dl>

### -param <i>hDrvCommandList</i> 

<dd>
<p>The command list.</p>
</dd>

### -param <i>hDrvDecoder</i> 

<dd>
<p>The video decoder.</p>
</dd>

### -param <i>SubmissionID</i> 

<dd>
<p>The submission ID.</p>
</dd>

### -param <i>pOutputStreamParameters</i> 

<dd>
<p>The output arguments for the video decode.</p>
</dd>

### -param <i>pInputStreamParameters</i> 

<dd>
<p>The input arguments for the video decode.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>
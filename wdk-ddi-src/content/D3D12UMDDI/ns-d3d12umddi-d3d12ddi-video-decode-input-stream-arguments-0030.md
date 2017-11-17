---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030
title: D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030
author: windows-driver-content
description: Video decode input stream arguments.
old-location: display\d3d12ddi-video-decode-input-stream-arguments-0030.htm
ms.assetid: 186115c0-14ed-4ca0-9f47-fdcf8f0b586c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030
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
ms.keywords: D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030, D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030
req.iface: 
---

# D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030 structure



## -description
<p>Video decode input stream arguments.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030 {
  D3D12DDI_VIDEO_DECODE_FRAME_ARGUMENT_0020 [D3D12DDI_VIDEO_DECODE_MAX_ARGUMENTS_0020] FrameArguments;
  UINT                                                                                 FrameArgumentsCount;
  D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0020                                          ReferenceFrames;
  D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0020                                      CompressedBitstream;
  D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030                                      DecryptionParameters;
} D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030, D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030;
````


## -struct-fields
<dl>

### -field <b>FrameArguments</b>

<dd>
<p>Frame arguments.</p>
</dd>

### -field <b>FrameArgumentsCount</b>

<dd>
<p>Frame arguments count.</p>
</dd>

### -field <b>ReferenceFrames</b>

<dd>
<p>Reference frames.</p>
</dd>

### -field <b>CompressedBitstream</b>

<dd>
<p>Compressed bitstream.</p>
</dd>

### -field <b>DecryptionParameters</b>

<dd>
<p>Decryption parameters.</p>
</dd>
</dl>

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
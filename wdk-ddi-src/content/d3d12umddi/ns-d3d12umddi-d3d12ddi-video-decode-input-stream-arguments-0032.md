---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032
title: D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032
author: windows-driver-content
description: Video decode input stream arguments.
old-location: display\d3d12ddi-video-decode-input-stream-arguments-0032.htm
old-project: display
ms.assetid: ca647cd3-357b-4cd6-aa1c-6a03d5a77f10
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032, D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032
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
req.iface: 
---

# D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032 structure



## -description
<p>Video decode input stream arguments.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032 {
  D3D12DDI_VIDEO_DECODE_FRAME_ARGUMENT_0020 [D3D12DDI_VIDEO_DECODE_MAX_ARGUMENTS_0020] FrameArguments;
  UINT                                                                                 NumFrameArguments;
  D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032                                          ReferenceFrames;
  D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032                                      CompressedBitstream;
  D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030                                      DecryptionParameters;
  D3D12DDI_HVIDEODECODERHEAP_0032                                                      hDrvVideoDecoderHeap;
} D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032, D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032;
````


## -struct-fields
<dl>

### -field FrameArguments

<dd>
<p>Frame arguments.</p>
</dd>

### -field NumFrameArguments

<dd>
<p>The number of frame arguments.</p>
</dd>

### -field ReferenceFrames

<dd>
<p>Reference frames.</p>
</dd>

### -field CompressedBitstream

<dd>
<p>Compressed bitstream.</p>
</dd>

### -field DecryptionParameters

<dd>
<p>Decryption parameters.</p>
</dd>

### -field hDrvVideoDecoderHeap

<dd>
<p>Video decoder heap.</p>
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
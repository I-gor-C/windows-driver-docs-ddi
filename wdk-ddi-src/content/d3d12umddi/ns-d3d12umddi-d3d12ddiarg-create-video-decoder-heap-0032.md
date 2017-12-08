---
UID: NS.d3d12umddi.D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032
title: D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032
author: windows-driver-content
description: Creates a video decoder heap.
old-location: display\d3d12ddiarg-create-video-decoder-heap-0032.htm
old-project: display
ms.assetid: 86f8021d-9b02-457f-9bee-4631c711094f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032, D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032
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
req.alt-api: D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032
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

# D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032 structure



## -description
<p>Creates a video decoder heap.</p>


## -syntax

````
typedef struct _D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032 {
  UINT                                      NodeMask;
  D3D12DDI_VIDEO_DECODE_CONFIGURATION_0020  Configuration;
  UINT                                      DecodeWidth;
  UINT                                      DecodeHeight;
  UINT                                      MaxDecodePictureBufferCount;
  DXGI_RATIONAL                             FrameRate;
  UINT                                      BitRate;
} D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032, D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032;
````


## -struct-fields
<dl>

### -field NodeMask

<dd>
<p>Represents the set of nodes.</p>
</dd>

### -field Configuration

<dd>
<p>The video decode configuration.</p>
</dd>

### -field DecodeWidth

<dd>
<p>The decode width.</p>
</dd>

### -field DecodeHeight

<dd>
<p>The decode height.</p>
</dd>

### -field MaxDecodePictureBufferCount

<dd>
<p>The max decode picture buffer count.</p>
</dd>

### -field FrameRate

<dd>
<p>The frame rate.</p>
</dd>

### -field BitRate

<dd>
<p>The bitrate.</p>
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
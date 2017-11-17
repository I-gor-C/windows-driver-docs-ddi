---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032
title: D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032
author: windows-driver-content
description: Video decode reference frames.
old-location: display\d3d12ddi-video-decode-reference-frames-0032.htm
ms.assetid: 58a814ab-629e-4528-a349-c469defc0a5a
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
req.alt-api: D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032
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
ms.keywords: D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032, D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032
req.iface: 
---

# D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032 structure



## -description
<p>Video decode reference frames.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032 {
  D3D12DDI_HRESOURCE *               hDrvTexture2Ds;
  UINT *                             pSubresources;
  D3D12DDI_HVIDEODECODERHEAP_0032 *  hDrvVideoDecoderHeaps;
  UINT                               NumTexture2Ds;
} D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032, D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032;
````


## -struct-fields
<dl>

### -field <b>hDrvTexture2Ds</b>

<dd>
<p>Texture.</p>
</dd>

### -field <b>pSubresources</b>

<dd>
<p>Subresources.</p>
</dd>

### -field <b>hDrvVideoDecoderHeaps</b>

<dd>
<p>Video decoder heaps.</p>
</dd>

### -field <b>NumTexture2Ds</b>

<dd>
<p>The number of textures.</p>
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
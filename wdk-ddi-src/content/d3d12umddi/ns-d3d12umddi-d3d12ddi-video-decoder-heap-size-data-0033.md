---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033
title: D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033
author: windows-driver-content
description: The video decoder heap size data.
old-location: display\d3d12ddi-video-decoder-heap-size-data-0033.htm
old-project: display
ms.assetid: beec0f3e-f87b-408b-8745-14b556254d77
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033, D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033
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
req.alt-api: D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033
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

# D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033 structure



## -description
<p>The video decoder heap size data.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033 {
  D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0033  VideoDecoderHeapDesc;
  UINT64                                      MemoryPoolL0Size;
  UINT64                                      MemoryPoolL1Size;
} D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033, D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033;
````


## -struct-fields
<dl>

### -field VideoDecoderHeapDesc

<dd>
<p>The video decoder heap description.</p>
</dd>

### -field MemoryPoolL0Size

<dd>
<p>The memory pool L0 size.</p>
</dd>

### -field MemoryPoolL1Size

<dd>
<p>The memory pool L1 size.</p>
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
---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032
title: D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032
author: windows-driver-content
description: Data structure for the D3D12DDICAPS_TYPE_VIDEO_0032_PROCESSOR_SIZE capability check. Retrieves the memory allocation size of a video processor created with the given properties.
old-location: display\d3d12ddi_video_processor_size_data_0032.htm
ms.assetid: B5A0E067-E91B-4B35-A355-36E15665CF43
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
req.alt-api: D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032
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
ms.keywords: D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032, D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032
req.iface: 
---

# D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032 structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Data structure for the D3D12DDICAPS_TYPE_VIDEO_0032_PROCESSOR_SIZE capability check.  Retrieves the memory allocation size of a video processor created with the given properties.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032 {
  D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0032 VideoProcessorDesc;
  UINT64                                  MemoryPoolL0Size;
  UINT64                                  MemoryPoolL1Size;
} D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032;
````


## -struct-fields
<dl>

### -field <b>VideoProcessorDesc</b>

<dd>
<p>The creation properties for a video processor heap.  Driver should map these creation properties to size.</p>
</dd>

### -field <b>MemoryPoolL0Size</b>

<dd>
<p>The L0 size of the heap object.  Memory Pool L0 is the memory pool “closest” to the GPU.  In the case of UMA adapters, this is the amount of system memory used.  For discrete adapters, this is the amount of discrete memory used.</p>
</dd>

### -field <b>MemoryPoolL1Size</b>

<dd>
<p>The L1 size of the heap object.  Memory Pool L1 is the memory pool “second closest” to the GPU.  In the case of UMA adapters, this value is zero.  In the case of discrete adapters, this is the amount of system memory used.</p>
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
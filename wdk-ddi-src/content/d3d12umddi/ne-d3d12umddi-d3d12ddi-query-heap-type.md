---
UID: NE.d3d12umddi.D3D12DDI_QUERY_HEAP_TYPE
title: D3D12DDI_QUERY_HEAP_TYPE
author: windows-driver-content
description: Type of a query heap, which is an array of query results.
old-location: display\d3d12ddi_query_heap_type.htm
old-project: display
ms.assetid: 8A1A42B5-D978-4019-825B-94DB81C44FEA
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_QUERY_HEAP_TYPE
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_QUERY_HEAP_TYPE enumeration



## -description
<p>Type of a query heap, which is an array of query results.</p>


## -syntax

````
typedef enum D3D12DDI_QUERY_HEAP_TYPE { 
  D3D12DDI_QUERY_HEAP_TYPE_OCCLUSION                     = 0,
  D3D12DDI_QUERY_HEAP_TYPE_TIMESTAMP                     = 1,
  D3D12DDI_QUERY_HEAP_TYPE_PIPELINE_STATISTICS           = 2,
  D3D12DDI_QUERY_HEAP_TYPE_SO_STATISTICS                 = 3,
  D3D12DDI_QUERY_HEAP_TYPE_0020_VIDEO_DECODE_STATISTICS  = 4,
  D3D12DDI_QUERY_HEAP_TYPE_0032_COPY_QUEUE_TIMESTAMP     = 5
} D3D12DDI_QUERY_HEAP_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_QUERY_HEAP_TYPE_OCCLUSION"></a><a id="d3d12ddi_query_heap_type_occlusion"></a><b>D3D12DDI_QUERY_HEAP_TYPE_OCCLUSION</b>

<dd>
<p>Occlusion.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_HEAP_TYPE_TIMESTAMP"></a><a id="d3d12ddi_query_heap_type_timestamp"></a><b>D3D12DDI_QUERY_HEAP_TYPE_TIMESTAMP</b>

<dd>
<p>Timestamp.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_HEAP_TYPE_PIPELINE_STATISTICS"></a><a id="d3d12ddi_query_heap_type_pipeline_statistics"></a><b>D3D12DDI_QUERY_HEAP_TYPE_PIPELINE_STATISTICS</b>

<dd>
<p>Pipeline statistics.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_HEAP_TYPE_SO_STATISTICS"></a><a id="d3d12ddi_query_heap_type_so_statistics"></a><b>D3D12DDI_QUERY_HEAP_TYPE_SO_STATISTICS</b>

<dd>
<p>SO statistics.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_HEAP_TYPE_0020_VIDEO_DECODE_STATISTICS"></a><a id="d3d12ddi_query_heap_type_0020_video_decode_statistics"></a><b>D3D12DDI_QUERY_HEAP_TYPE_0020_VIDEO_DECODE_STATISTICS</b>

<dd>
<p>Video decode statistics.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_HEAP_TYPE_0032_COPY_QUEUE_TIMESTAMP"></a><a id="d3d12ddi_query_heap_type_0032_copy_queue_timestamp"></a><b>D3D12DDI_QUERY_HEAP_TYPE_0032_COPY_QUEUE_TIMESTAMP</b>

<dd>
<p>Copy queue timestamp.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NE.d3d12umddi.D3D12DDI_QUERY_TYPE
title: D3D12DDI_QUERY_TYPE
author: windows-driver-content
description: Type of a query.
old-location: display\d3d12ddi_query_type.htm
old-project: display
ms.assetid: C411997A-0F01-4D88-816A-BD375D0744C7
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
req.alt-api: D3D12DDI_QUERY_TYPE
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

# D3D12DDI_QUERY_TYPE enumeration



## -description
<p>Type of a query.</p>


## -syntax

````
typedef enum D3D12DDI_QUERY_TYPE { 
  D3D12DDI_QUERY_TYPE_OCCLUSION                     = 0,
  D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION              = 1,
  D3D12DDI_QUERY_TYPE_TIMESTAMP                     = 2,
  D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS           = 3,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0         = 4,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1         = 5,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2         = 6,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3         = 7,
  D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS  = 8
} D3D12DDI_QUERY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_QUERY_TYPE_OCCLUSION"></a><a id="d3d12ddi_query_type_occlusion"></a><b>D3D12DDI_QUERY_TYPE_OCCLUSION</b>

<dd>
<p>Occlusion.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION"></a><a id="d3d12ddi_query_type_binary_occlusion"></a><b>D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION</b>

<dd>
<p>Binary occlusion.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_TIMESTAMP"></a><a id="d3d12ddi_query_type_timestamp"></a><b>D3D12DDI_QUERY_TYPE_TIMESTAMP</b>

<dd>
<p>Timestamp.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS"></a><a id="d3d12ddi_query_type_pipeline_statistics"></a><b>D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS</b>

<dd>
<p>Pipeline statistics.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0"></a><a id="d3d12ddi_query_type_so_statistics_stream0"></a><b>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0</b>

<dd>
<p>SO statistics for Stream0.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1"></a><a id="d3d12ddi_query_type_so_statistics_stream1"></a><b>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1</b>

<dd>
<p>SO statistics for Stream1.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2"></a><a id="d3d12ddi_query_type_so_statistics_stream2"></a><b>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2</b>

<dd>
<p>SO statistics for Stream2.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3"></a><a id="d3d12ddi_query_type_so_statistics_stream3"></a><b>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3</b>

<dd>
<p>SO statistics for Stream3.</p>
</dd>

### -field <a id="D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS"></a><a id="d3d12ddi_query_type_0020_video_decode_statistics"></a><b>D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS</b>

<dd>
<p>Video decode statistics.</p>
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
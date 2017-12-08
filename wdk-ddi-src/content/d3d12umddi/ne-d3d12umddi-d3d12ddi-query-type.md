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

### -field D3D12DDI_QUERY_TYPE_OCCLUSION

<dd>
<p>Occlusion.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION

<dd>
<p>Binary occlusion.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_TIMESTAMP

<dd>
<p>Timestamp.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS

<dd>
<p>Pipeline statistics.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0

<dd>
<p>SO statistics for Stream0.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1

<dd>
<p>SO statistics for Stream1.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2

<dd>
<p>SO statistics for Stream2.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3

<dd>
<p>SO statistics for Stream3.</p>
</dd>

### -field D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS

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
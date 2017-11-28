---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
title: D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
author: windows-driver-content
description: Video decode profile count data.
old-location: display\d3d12ddi-video-decode-profile-count-data-0032.htm
old-project: display
ms.assetid: 8398579d-e8cf-4c58-ac74-eeddf2dca23b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032, D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
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
req.alt-api: D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
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

# D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032 structure



## -description
<p>Video decode profile count data.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032 {
  UINT  NodeIndex;
  UINT  ProfileCount;
} D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032, D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032;
````


## -struct-fields
<dl>

### -field <b>NodeIndex</b>

<dd>
<p>Node index.</p>
</dd>

### -field <b>ProfileCount</b>

<dd>
<p>Profile count.</p>
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
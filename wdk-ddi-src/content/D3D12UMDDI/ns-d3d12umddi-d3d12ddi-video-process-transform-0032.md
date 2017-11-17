---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032
title: D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032
author: windows-driver-content
description: Video process transform.
old-location: display\d3d12ddi-video-process-transform-0032.htm
ms.assetid: 7c2393e6-3e1b-4b4a-b6ea-5848c38440b0
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
req.alt-api: D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032
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
ms.keywords: D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032, D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032
req.iface: 
---

# D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032 structure



## -description
<p>Video process transform.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032 {
  D3D12DDI_RECT                            SourceRectangle;
  D3D12DDI_RECT                            DestinationRectangle;
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020  Orientation;
} D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032, D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032;
````


## -struct-fields
<dl>

### -field <b>SourceRectangle</b>

<dd>
<p>Source rectangle.</p>
</dd>

### -field <b>DestinationRectangle</b>

<dd>
<p>Destination rectangle.</p>
</dd>

### -field <b>Orientation</b>

<dd>
<p>Orientation.</p>
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
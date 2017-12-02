---
UID: NE.d3d12umddi.D3D12DDI_RESOURCE_STATES
title: D3D12DDI_RESOURCE_STATES
author: windows-driver-content
description: Contains resource states.
old-location: display\d3d12ddi_resource_states.htm
old-project: display
ms.assetid: E5DB8AF3-A6ED-4CD7-9723-78ACD57F1723
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
req.alt-api: D3D12DDI_RESOURCE_STATES
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

# D3D12DDI_RESOURCE_STATES enumeration



## -description
<p>Contains resource states. </p>


## -syntax

````
typedef enum D3D12DDI_RESOURCE_STATES { 
  D3D12DDI_RESOURCE_STATE_COMMON                      = 0x00000000,
  D3D12DDI_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER  = 0x00000001,
  D3D12DDI_RESOURCE_STATE_INDEX_BUFFER                = 0x00000002,
  D3D12DDI_RESOURCE_STATE_RENDER_TARGET               = 0x00000004,
  D3D12DDI_RESOURCE_STATE_UNORDERED_ACCESS            = 0x00000008,
  D3D12DDI_RESOURCE_STATE_DEPTH_WRITE                 = 0x00000010,
  D3D12DDI_RESOURCE_STATE_DEPTH_READ                  = 0x00000020,
  D3D12DDI_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE   = 0x00000040,
  D3D12DDI_RESOURCE_STATE_PIXEL_SHADER_RESOURCE       = 0x00000080,
  D3D12DDI_RESOURCE_STATE_STREAM_OUT                  = 0x00000100,
  D3D12DDI_RESOURCE_STATE_INDIRECT_ARGUMENT           = 0x00000200,
  D3D12DDI_RESOURCE_STATE_COPY_DEST                   = 0x00000400,
  D3D12DDI_RESOURCE_STATE_COPY_SOURCE                 = 0x00000800,
  D3D12DDI_RESOURCE_STATE_RESOLVE_DEST                = 0x00001000,
  D3D12DDI_RESOURCE_STATE_RESOLVE_SOURCE              = 0x00002000,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_READ      = 0x00010000,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_WRITE     = 0x00020000,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_READ     = 0x00040000,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_WRITE    = 0x00080000
} D3D12DDI_RESOURCE_STATES;
````


## -enum-fields
<dl>

### -field D3D12DDI_RESOURCE_STATE_COMMON

<dd>
<p>Common. </p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER

<dd>
<p>Vertex and constant buffer.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_INDEX_BUFFER

<dd>
<p>Index buffer.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_RENDER_TARGET

<dd>
<p>Render target.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_UNORDERED_ACCESS

<dd>
<p>Unordered access.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_DEPTH_WRITE

<dd>
<p>Depth write. </p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_DEPTH_READ

<dd>
<p>Depth read.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE

<dd>
<p>Non-pixel shader resource.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_PIXEL_SHADER_RESOURCE

<dd>
<p>Pixel shader retsource.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_STREAM_OUT

<dd>
<p>Stream out.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_INDIRECT_ARGUMENT

<dd>
<p>Indirect argument.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_COPY_DEST

<dd>
<p>Copy destination.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_COPY_SOURCE

<dd>
<p>Copy source.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_RESOLVE_DEST

<dd>
<p>Resolve destination. </p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_RESOLVE_SOURCE

<dd>
<p>Resolve source.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_READ

<dd>
<p>Video decode read.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_WRITE

<dd>
<p>Video decode write.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_READ

<dd>
<p>Video process read.</p>
</dd>

### -field D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_WRITE

<dd>
<p>Video process write.</p>
</dd>
</dl>

## -remarks
<p>Resource barriers allow transitioning between hardware specific states for a corresponding operation and to synchronize read after write.  </p>

<p>Resource barriers are an existing concept in D3D12 that is extended to support video decode by adding new usage flags.
The write state is used for the decode target.  The write state is also used when decode conversion is enabled for the non-converted reference.
</p>

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
---
UID: NE.d3d12umddi.D3D12DDI_RESOURCE_FLAGS_0003
title: D3D12DDI_RESOURCE_FLAGS_0003
author: windows-driver-content
description: Specifies resource flag values.
old-location: display\d3d12ddi_resource_flags_0003.htm
old-project: display
ms.assetid: 595A4177-4A18-48D6-8B5C-D7D2FBD9FE9B
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
req.alt-api: D3D12DDI_RESOURCE_FLAGS_0003
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

# D3D12DDI_RESOURCE_FLAGS_0003 enumeration



## -description
<p>Specifies resource flag values.</p>


## -syntax

````
typedef enum D3D12DDI_RESOURCE_FLAGS_0003 { 
  D3D12DDI_RESOURCE_FLAG_0003_NONE                         = 0x0,
  D3D12DDI_RESOURCE_FLAG_0003_RENDER_TARGET                = 0x1,
  D3D12DDI_RESOURCE_FLAG_0003_DEPTH_STENCIL                = 0x2,
  D3D12DDI_RESOURCE_FLAG_0003_CROSS_ADAPTER                = 0x4,
  D3D12DDI_RESOURCE_FLAG_0003_SIMULTANEOUS_ACCESS          = 0x8,
  D3D12DDI_RESOURCE_FLAG_0003_SHADER_RESOURCE              = 0x10,
  D3D12DDI_RESOURCE_FLAG_0020_VIDEO_DECODE_REFERENCE_ONLY  = 0x20,
  D3D12DDI_RESOURCE_FLAG_0020_CONTENT_PROTECTION           = 0x40,
  D3D12DDI_RESOURCE_FLAG_0022_UNORDERED_ACCESS             = 0x80
} D3D12DDI_RESOURCE_FLAGS_0003;
````


## -enum-fields
<dl>

### -field D3D12DDI_RESOURCE_FLAG_0003_NONE

<dd>
<p>Constant for no flags.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0003_RENDER_TARGET

<dd>
<p>Render target.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0003_DEPTH_STENCIL

<dd>
<p>Depth stencil.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0003_CROSS_ADAPTER

<dd>
<p>Cross adapter.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0003_SIMULTANEOUS_ACCESS

<dd>
<p>Simultaneous access.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0003_SHADER_RESOURCE

<dd>
<p>Shader resource.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0020_VIDEO_DECODE_REFERENCE_ONLY

<dd>
<p>Video decode reference only.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0020_CONTENT_PROTECTION 

<dd>
<p>Content protection.</p>
</dd>

### -field D3D12DDI_RESOURCE_FLAG_0022_UNORDERED_ACCESS

<dd>
<p>Unordered access. This value is available as a resource flag for the fallback plans.</p>
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
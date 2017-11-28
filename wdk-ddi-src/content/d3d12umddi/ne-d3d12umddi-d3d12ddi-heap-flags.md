---
UID: NE.d3d12umddi.D3D12DDI_HEAP_FLAGS
title: D3D12DDI_HEAP_FLAGS
author: windows-driver-content
description: Contains Direct3D 12 heap flags.
old-location: display\d3d12ddi_heap_flags.htm
old-project: display
ms.assetid: 8224E497-7F52-469B-98C9-ECC5F1970894
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
req.alt-api: D3D12DDI_HEAP_FLAGS
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

# D3D12DDI_HEAP_FLAGS enumeration



## -description
<p>Contains Direct3D 12 heap flags. </p>


## -syntax

````
typedef enum D3D12DDI_HEAP_FLAGS { 
  D3D12DDI_HEAP_FLAG_NONE                 = 0x0,
  D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES   = 0x2,
  D3D12DDI_HEAP_FLAG_BUFFERS              = 0x4,
  D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE  = 0x8,
  D3D12DDI_HEAP_FLAG_PRIMARY              = 0x10,
  D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES       = 0x20,
  D3D12DDI_HEAP_FLAG_CONTENT_PROTECTION   = 0x40
} D3D12DDI_HEAP_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_HEAP_FLAG_NONE"></a><a id="d3d12ddi_heap_flag_none"></a><b>D3D12DDI_HEAP_FLAG_NONE</b>

<dd>
<p>No flags.</p>
</dd>

### -field <a id="D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES"></a><a id="d3d12ddi_heap_flag_non_rt_ds_textures"></a><b>D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES</b>

<dd>
<p>The heap supports resources allocated for other than Render Target (RT) and Depth-Stencil (DS) textures. </p>
</dd>

### -field <a id="D3D12DDI_HEAP_FLAG_BUFFERS"></a><a id="d3d12ddi_heap_flag_buffers"></a><b>D3D12DDI_HEAP_FLAG_BUFFERS</b>

<dd>
<p>The heap supports resources allocated for buffers.</p>
</dd>

### -field <a id="D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE"></a><a id="d3d12ddi_heap_flag_coherent_systemwide"></a><b>D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE</b>

<dd>
<p>The heap supports resources allocated for coherent systemwide. </p>
</dd>

### -field <a id="D3D12DDI_HEAP_FLAG_PRIMARY"></a><a id="d3d12ddi_heap_flag_primary"></a><b>D3D12DDI_HEAP_FLAG_PRIMARY</b>

<dd>
<p>The heap supports resources allocated for primary.</p>
</dd>

### -field <a id="D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES"></a><a id="d3d12ddi_heap_flag_rt_ds_textures"></a><b>D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES</b>

<dd>
<p>The heap supports resources allocated for RT and DS textures.</p>
</dd>

### -field <a id="D3D12DDI_HEAP_FLAG_CONTENT_PROTECTION_"></a><a id="d3d12ddi_heap_flag_content_protection_"></a><b>D3D12DDI_HEAP_FLAG_CONTENT_PROTECTION </b>

<dd>
<p>The heap supports resources allocated for content protection.</p>
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
---
UID: NE.d3d12umddi.D3D12DDI_TEXTURE_LAYOUT
title: D3D12DDI_TEXTURE_LAYOUT
author: windows-driver-content
description: Specifies a texture layout.
old-location: display\d3d12ddi_texture_layout.htm
old-project: display
ms.assetid: F039A0D9-D1AE-4940-B67D-30CC6344EC7D
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
req.alt-api: D3D12DDI_TEXTURE_LAYOUT
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

# D3D12DDI_TEXTURE_LAYOUT enumeration



## -description
<p>Specifies a texture layout.</p>


## -syntax

````
typedef enum D3D12DDI_TEXTURE_LAYOUT { 
  D3D12DDI_TL_UNDEFINED                    = 0,
  D3D12DDI_TL_ROW_MAJOR                    = 1,
  D3D12DDI_TL_64KB_TILE_UNDEFINED_SWIZZLE  = 2,
  D3D12DDI_TL_64KB_TILE_STANDARD_SWIZZLE   = 3,
  D3D12DDI_TL_DEVICE_DEPENDENT_SWIZZLE_0   = 0x100
} D3D12DDI_TEXTURE_LAYOUT;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_TL_UNDEFINED"></a><a id="d3d12ddi_tl_undefined"></a><b>D3D12DDI_TL_UNDEFINED</b>

<dd>
<p>Texture layout undefined. </p>
</dd>

### -field <a id="D3D12DDI_TL_ROW_MAJOR"></a><a id="d3d12ddi_tl_row_major"></a><b>D3D12DDI_TL_ROW_MAJOR</b>

<dd>
<p>Texture layout row major.</p>
</dd>

### -field <a id="D3D12DDI_TL_64KB_TILE_UNDEFINED_SWIZZLE"></a><a id="d3d12ddi_tl_64kb_tile_undefined_swizzle"></a><b>D3D12DDI_TL_64KB_TILE_UNDEFINED_SWIZZLE</b>

<dd>
<p>A 64 KB tile with undefined swizzle.</p>
</dd>

### -field <a id="D3D12DDI_TL_64KB_TILE_STANDARD_SWIZZLE"></a><a id="d3d12ddi_tl_64kb_tile_standard_swizzle"></a><b>D3D12DDI_TL_64KB_TILE_STANDARD_SWIZZLE</b>

<dd>
<p>A 64 KB tile with standard swizzle.</p>
</dd>

### -field <a id="D3D12DDI_TL_DEVICE_DEPENDENT_SWIZZLE_0"></a><a id="d3d12ddi_tl_device_dependent_swizzle_0"></a><b>D3D12DDI_TL_DEVICE_DEPENDENT_SWIZZLE_0</b>

<dd>
<p>A device dependant swizzle.</p>
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
---
UID: NS.d3d10umddi.D3DWDDM1_3DDI_TILE_REGION_SIZE
title: D3DWDDM1_3DDI_TILE_REGION_SIZE
author: windows-driver-content
description: Specifies a tiled region.
old-location: display\d3dwddm1_3ddi_tile_region_size.htm
old-project: display
ms.assetid: 276ED4AC-15D9-4550-AC51-83320DE9D5B2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM1_3DDI_TILE_REGION_SIZE, D3DWDDM1_3DDI_TILE_REGION_SIZE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM1_3DDI_TILE_REGION_SIZE
req.alt-loc: D3d10umddi.h
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

# D3DWDDM1_3DDI_TILE_REGION_SIZE structure



## -description
<p>Specifies a tiled region.</p>


## -syntax

````
typedef struct D3DWDDM1_3DDI_TILE_REGION_SIZE {
  UINT   NumTiles;
  BOOL   bUseBox;
  UINT   Width;
  UINT16 Height;
  UINT16 Depth;
} D3DWDDM1_3DDI_TILE_REGION_SIZE;
````


## -struct-fields
<dl>

### -field NumTiles

<dd>
<p>The number of tiles within the tiled region.</p>
<div class="alert"><b>Note</b>  <b>NumTiles</b> must equal <b>Width</b> * <b>Height</b> * <b>Depth</b>.</div>
<div> </div>
</dd>

### -field bUseBox

<dd>
<p>If <b>TRUE</b>, the tiled region is defined by the <b>Width</b>, <b>Height</b>, and <b>Depth</b> members. In this case, one update region cannot span mipmaps, although it can span array slices using the  <b>Depth</b> member.</p>
<p>If <b>FALSE</b>, the <b>Width</b>, <b>Height</b>, and <b>Depth</b> members should be ignored, and the tiled region is defined by the <b>NumTiles</b> member. In this case, tiles are mapped linearly, first across the <i>x</i>-direction, then the <i>y</i>-direction, then (as applicable) across the <i>z</i>-direction, and then spilling over mipmaps and arrays in subresource order. This procedure is useful for mapping an entire resource at one time.</p>
<p>In either case, the starting location for the region within the resource 
                  is specified as a separate parameter outside this structure.</p>
</dd>

### -field Width

<dd>
<p>The width (in the <i>x</i>-direction) of the tiled region. Used for buffer, 1-D, 2-D, and 3-D rendering.</p>
</dd>

### -field Height

<dd>
<p>The height (in the <i>y</i>-direction) of the tiled region. Used for 2-D and 3-D rendering.</p>
</dd>

### -field Depth

<dd>
<p>The depth (in the <i>z</i>-direction) of the tiled region. Used for 3-D rendering or for arrays. In the case of arrays, advancing in depth skips to the next slice of the same mipmap size.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>
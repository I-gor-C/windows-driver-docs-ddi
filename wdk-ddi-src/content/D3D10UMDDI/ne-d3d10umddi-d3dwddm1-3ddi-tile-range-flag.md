---
UID: NE.d3d10umddi.D3DWDDM1_3DDI_TILE_RANGE_FLAG
title: D3DWDDM1_3DDI_TILE_RANGE_FLAG
author: windows-driver-content
description: Specifies a range of tile mappings to use with the UpdateTileMappings function.
old-location: display\d3dwddm1_3ddi_tile_range_flag.htm
ms.assetid: 7D8B55F1-00BD-414B-9E78-DABCEBEF949F
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM1_3DDI_TILE_RANGE_FLAG
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# D3DWDDM1_3DDI_TILE_RANGE_FLAG enumeration



## -description
<p>Specifies a range of tile mappings to use with the UpdateTileMappings function.</p>


## -syntax

````
enum D3DWDDM1_3DDI_TILE_RANGE_FLAG {
  D3DWDDM_1_3DDI_TILE_RANGE_NULL               = 0x00000001, 
  D3DWDDM_1_3DDI_TILE_RANGE_SKIP               = 0x00000002, 
  D3DWDDM_1_3DDI_TILE_RANGE_REUSE_SINGLE_TILE  = 0x00000004 

};
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM_1_3DDI_TILE_RANGE_NULL"></a><a id="d3dwddm_1_3ddi_tile_range_null"></a><b>D3DWDDM_1_3DDI_TILE_RANGE_NULL</b>

<dd>
<p>The tile range is <b>NULL</b>.</p>
<p>If this flag is set in the UpdateTileMappings function's <i>pRangeFlags</i> parameter, the <i>pRangeTileCounts</i> parameter specifies the total 
number of tiles in all the tile regions, and the <i>pTilePoolStartOffsets</i> parameter is ignored.</p>
</dd>

### -field <a id="D3DWDDM_1_3DDI_TILE_RANGE_SKIP"></a><a id="d3dwddm_1_3ddi_tile_range_skip"></a><b>D3DWDDM_1_3DDI_TILE_RANGE_SKIP</b>

<dd>
<p>Tiles should be skipped over, and existing tile mappings should be left unchanged.</p>
<p>If this flag is set in the UpdateTileMappings function's <i>pRangeFlags</i> parameter, the <i>pRangeTileCounts</i> parameter specifies how many tiles from the tile regions to skip over, and the <i>pTilePoolStartOffsets</i> parameter is ignored.</p>
</dd>

### -field <a id="D3DWDDM_1_3DDI_TILE_RANGE_REUSE_SINGLE_TILE"></a><a id="d3dwddm_1_3ddi_tile_range_reuse_single_tile"></a><b>D3DWDDM_1_3DDI_TILE_RANGE_REUSE_SINGLE_TILE</b>

<dd>
<p>A single tile in the tile pool should be reused.</p>
<p>If this flag is set in the UpdateTileMappings function's <i>pRangeFlags</i> parameter, the <i>pTilePoolStartOffsets</i> parameter specifies the single tile in the tile pool to map to, and the <i>pRangeTileCounts</i> parameter specifies how many tiles from the tile region to map to that tile pool location.</p>
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
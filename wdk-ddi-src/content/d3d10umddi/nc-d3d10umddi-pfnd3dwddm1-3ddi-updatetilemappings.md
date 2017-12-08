---
UID: NC.d3d10umddi.PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS
title: PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS
author: windows-driver-content
description: Updates mappings of tile locations in tiled resources to memory locations in a tile pool.
old-location: display\updatetilemappings.htm
old-project: display
ms.assetid: 1C8FC920-145F-4AE9-B049-F6BDAE29D1F1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UpdateTileMappings
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

# PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS callback



## -description
<p>Updates mappings of tile locations in tiled resources to memory locations in a tile pool.</p>


## -prototype

````
PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS UpdateTileMappings;

VOID APIENTRY* UpdateTileMappings(
                 D3D10DDI_HDEVICE                        hDevice,
                 D3D10DDI_HRESOURCE                      hTiledResource,
                 UINT                                    NumTiledResourceRegions,
  _In_     const D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE *pTiledResourceRegionStartCoords,
  _In_opt_ const D3DWDDM1_3DDI_TILE_REGION_SIZE          *pTiledResourceRegionSizes,
                 D3D10DDI_HRESOURCE                      hTilePool,
                 UINT                                    NumRanges,
  _In_opt_ const UINT                                    *pRangeFlags,
  _In_opt_ const UINT                                    *pTilePoolStartOffsets,
  _In_opt_ const UINT                                    *pRangeTileCounts,
                 UINT                                    Flags
)
{ ... }
````


## -parameters
<dl>

### -param hDevice 

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param hTiledResource 

<dd>
<p>A handle to the tiled resource.</p>
</dd>

### -param NumTiledResourceRegions 

<dd>
<p>The number of tiled resource regions.</p>
</dd>

### -param pTiledResourceRegionStartCoords [in]

<dd>
<p>An array of <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-tiled-resource-coordinate.md">D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE</a> structures that describe the starting coordinates of the tiled resource regions. The <i>NumTiledResourceRegions</i> parameter specifies the number of <b>D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE</b> structures in the array.</p>
</dd>

### -param pTiledResourceRegionSizes [in, optional]

<dd>
<p>An array of <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-tile-region-size.md">D3DWDDM1_3DDI_TILE_REGION_SIZE</a> structures that describe the sizes of the tiled resource regions. The <i>NumTiledResourceRegions</i> parameter specifies the number of <b>D3DWDDM1_3DDI_TILE_REGION_SIZE</b> structures in the array.</p>
</dd>

### -param hTilePool 

<dd>
<p>A handle to the tile pool.</p>
</dd>

### -param NumRanges 

<dd>
<p>The number of tile-pool ranges.</p>
</dd>

### -param pRangeFlags [in, optional]

<dd>
<p>An array of values that describe each tile-pool range. The <i>NumRanges</i> parameter specifies the number of values in the array. Each value can be a combination of values of type <a href="..\d3d10umddi\ne-d3d10umddi-d3dwddm1-3ddi-tile-range-flag.md">D3DWDDM1_3DDI_TILE_RANGE_FLAG</a> combined by using a bitwise <b>OR</b> operation.</p>
</dd>

### -param pTilePoolStartOffsets [in, optional]

<dd>
<p>An array of offsets into the tile pool. These are zero-based tile offsets, counting in tiles (not bytes).</p>
</dd>

### -param pRangeTileCounts [in, optional]

<dd>
<p>An array of values that specify the number of tiles in each tile-pool range. The <i>NumRanges</i> parameter specifies the number of values in the array.</p>
</dd>

### -param Flags 

<dd>
<p>A combination of <a href="..\d3d10umddi\ne-d3d10umddi-d3dwddm1-3ddi-tile-mapping-flag.md">D3DWDDM1_3DDI_TILE_MAPPING_FLAG</a> values that are combined by using a bitwise <b>OR</b> operation.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. The driver can set <b>E_INVALIDARG</b> if a required input parameter does not exist or is <b>NULL</b>.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3dwddm1-3ddi-tile-mapping-flag.md">D3DWDDM1_3DDI_TILE_MAPPING_FLAG</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3dwddm1-3ddi-tile-range-flag.md">D3DWDDM1_3DDI_TILE_RANGE_FLAG</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-tile-region-size.md">D3DWDDM1_3DDI_TILE_REGION_SIZE</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-tiled-resource-coordinate.md">D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

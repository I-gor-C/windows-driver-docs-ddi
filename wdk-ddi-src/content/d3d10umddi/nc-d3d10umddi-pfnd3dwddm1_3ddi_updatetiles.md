---
UID: NC:d3d10umddi.PFND3DWDDM1_3DDI_UPDATETILES
title: PFND3DWDDM1_3DDI_UPDATETILES
author: windows-driver-content
description: Updates tiles by copying from app memory to the tiled resource.
old-location: display\updatetiles.htm
old-project: display
ms.assetid: 4891AB01-DE51-4B32-AA52-5619E86CC474
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3DWDDM1_3DDI_UPDATETILES, UpdateTiles, UpdateTiles callback function [Display Devices], d3d10umddi/UpdateTiles, display.updatetiles
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	UpdateTiles
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM1_3DDI_UPDATETILES callback function
Updates tiles by copying from app memory to the tiled resource.

## Syntax

```
PFND3DWDDM1_3DDI_UPDATETILES Pfnd3dwddm13DdiUpdatetiles;

void Pfnd3dwddm13DdiUpdatetiles(
  D3D10DDI_HDEVICE hDevice,
  D3D10DDI_HRESOURCE hDestTiledResource,
  const D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE *pDestTileRegionStartCoord,
  const D3DWDDM1_3DDI_TILE_REGION_SIZE *pDestTileRegionSize,
  const VOID *pSourceTileData,
  UINT Flags
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`hDestTiledResource`

A handle to the tiled resource.

`*pDestTileRegionStartCoord`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn440996">D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE</a> structure that describes the starting coordinates of the tiled resource.

`*pDestTileRegionSize`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn440997">D3DWDDM1_3DDI_TILE_REGION_SIZE</a> structure that describes the size of the tiled region.

`*pSourceTileData`

A pointer to memory that contains the source tile data that this function uses to update the tiled resource.

`Flags`

A combination of values of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn458989">D3DWDDM1_3DDI_TILE_COPY_FLAG</a> that are combined by using a bitwise <b>OR</b> operation. The only valid value is <b>D3DWDDM1_3DDI_TILE_COPY_NO_OVERWRITE</b>. The other enumeration constant values aren't meaningful here, though by definition using  <b>D3DWDDM1_3DDI_TILE_COPY_SWIZZLED_TILED_RESOURCE_TO_LINEAR_BUFFER</b> results in what the <i>UpdateTiles</i> function does, sourcing from app memory.


## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code.

The Direct3D runtime does not expect this function to fail.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1,WDDM 1.3 Windows Server 2012 R2 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn440996">D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn458989">D3DWDDM1_3DDI_TILE_COPY_FLAG</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn440997">D3DWDDM1_3DDI_TILE_REGION_SIZE</a>



<a href="https://msdn.microsoft.com/4891AB01-DE51-4B32-AA52-5619E86CC474">UpdateTiles</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
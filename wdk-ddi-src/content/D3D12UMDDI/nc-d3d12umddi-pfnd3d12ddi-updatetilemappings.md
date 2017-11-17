---
UID: NC.d3d12umddi.PFND3D12DDI_UPDATETILEMAPPINGS
title: PFND3D12DDI_UPDATETILEMAPPINGS
author: windows-driver-content
description: 
ms.assetid: 53944168-bd89-4514-9cc4-01252f99e282
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PFND3D12DDI_UPDATETILEMAPPINGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_UPDATETILEMAPPINGS Pfnd3d12ddiUpdatetilemappings; 

// Definition

VOID Pfnd3d12ddiUpdatetilemappings 
(
	 D3D12DDI_HCOMMANDQUEUE
	 D3D12DDI_HRESOURCE
	UINT NumTiledResourceRegions
	 const D3D12DDI_TILED_RESOURCE_COORDINATE *pResourceRegionStartCoords
	 const D3D12DDI_TILE_REGION_SIZE *pResourceRegionSizes
	 D3D12DDI_HHEAP
	UINT NumRanges
	 const D3D12DDI_TILE_RANGE_FLAGS *
	 const UINT *pHeapStartOffsets
	 const UINT *pRangeTileCounts
	 D3D12DDI_TILE_MAPPING_FLAGS
)
{...}

PFND3D12DDI_UPDATETILEMAPPINGS 


```

## -parameters

### -param D3D12DDI_HCOMMANDQUEUE: 
### -param D3D12DDI_HRESOURCE: 
### -param NumTiledResourceRegions: 
### -param *pResourceRegionStartCoords: 
### -param *pResourceRegionSizes: 
### -param D3D12DDI_HHEAP: 
### -param NumRanges: 
### -param *: 
### -param *pHeapStartOffsets: 
### -param *pRangeTileCounts: 
### -param D3D12DDI_TILE_MAPPING_FLAGS: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
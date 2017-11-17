---
UID: NC.d3d12umddi.PFND3D12DDI_COPYTILEMAPPINGS
title: PFND3D12DDI_COPYTILEMAPPINGS
author: windows-driver-content
description: 
ms.assetid: 6554a08a-50ab-4e40-995c-f6524db98b4a
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

# PFND3D12DDI_COPYTILEMAPPINGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_COPYTILEMAPPINGS Pfnd3d12ddiCopytilemappings; 

// Definition

VOID Pfnd3d12ddiCopytilemappings 
(
	 D3D12DDI_HCOMMANDQUEUE
	D3D12DDI_HRESOURCE hDstResource
	 const D3D12DDI_TILED_RESOURCE_COORDINATE *pDstRegionStartCoord
	D3D12DDI_HRESOURCE hSrcResource
	 const D3D12DDI_TILED_RESOURCE_COORDINATE *pSrcRegionStartCoord
	 const D3D12DDI_TILE_REGION_SIZE *
	 D3D12DDI_TILE_MAPPING_FLAGS
)
{...}

PFND3D12DDI_COPYTILEMAPPINGS 


```

## -parameters

### -param D3D12DDI_HCOMMANDQUEUE: 
### -param hDstResource: 
### -param *pDstRegionStartCoord: 
### -param hSrcResource: 
### -param *pSrcRegionStartCoord: 
### -param *: 
### -param D3D12DDI_TILE_MAPPING_FLAGS: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d12umddi.PFND3D12DDI_COPYTILES
title: PFND3D12DDI_COPYTILES
author: windows-driver-content
description: 
ms.assetid: 67ddb367-6919-423b-9e65-9b0c86a721ad
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

# PFND3D12DDI_COPYTILES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_COPYTILES Pfnd3d12ddiCopytiles; 

// Definition

VOID Pfnd3d12ddiCopytiles 
(
	 D3D12DDI_HCOMMANDLIST
	D3D12DDI_HRESOURCE hResource
	 const D3D12DDI_TILED_RESOURCE_COORDINATE *pRegionStartCoord
	 const D3D12DDI_TILE_REGION_SIZE *pRegionSize
	D3D12DDI_HRESOURCE hBuffer
	UINT64 BufferStartOffsetInBytes
	 D3D12DDI_TILE_COPY_FLAGS
)
{...}

PFND3D12DDI_COPYTILES 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param hResource: 
### -param *pRegionStartCoord: 
### -param *pRegionSize: 
### -param hBuffer: 
### -param BufferStartOffsetInBytes: 
### -param D3D12DDI_TILE_COPY_FLAGS: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
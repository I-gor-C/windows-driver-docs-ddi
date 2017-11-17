---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0025
title: PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0025
author: windows-driver-content
description: 
ms.assetid: 25dc5534-c8c4-4c5f-ac66-db44bc0d0068
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

# PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0025 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0025 Pfnd3d12ddiCalcprivatedepthstencilstatesize0025; 

// Definition

SIZE_T Pfnd3d12ddiCalcprivatedepthstencilstatesize0025 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDI_DEPTH_STENCIL_DESC_0025 *
)
{...}

PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0025 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
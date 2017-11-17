---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE
title: PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE
author: windows-driver-content
description: 
ms.assetid: 970b4271-24aa-4d49-961b-b592e6d71d87
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

# PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE Pfnd3d12ddiCalcprivatedepthstencilstatesize; 

// Definition

SIZE_T Pfnd3d12ddiCalcprivatedepthstencilstatesize 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDI_DEPTH_STENCIL_DESC *
)
{...}

PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
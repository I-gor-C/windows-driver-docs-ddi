---
UID: NC.d3d12umddi.PFND3D12DDI_GET_PASS_OPTIMIZATION_FLOW
title: PFND3D12DDI_GET_PASS_OPTIMIZATION_FLOW
author: windows-driver-content
description: 
ms.assetid: 641356a8-6c82-4e80-8c12-250b9a4b0d03
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

# PFND3D12DDI_GET_PASS_OPTIMIZATION_FLOW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GET_PASS_OPTIMIZATION_FLOW Pfnd3d12ddiGetPassOptimizationFlow; 

// Definition

VOID Pfnd3d12ddiGetPassOptimizationFlow 
(
	 D3D12DDI_HPASS
	BOOL BuildOnPreviousCompletedOptimization
	UINT *pNumOptimizationRounds
	D3D12DDIARG_PASS_OPTIMIZATION_ROUND_DESC *pPassOptimizationRounds
)
{...}

PFND3D12DDI_GET_PASS_OPTIMIZATION_FLOW 


```

## -parameters

### -param D3D12DDI_HPASS: 
### -param BuildOnPreviousCompletedOptimization: 
### -param *pNumOptimizationRounds: 
### -param *pPassOptimizationRounds: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
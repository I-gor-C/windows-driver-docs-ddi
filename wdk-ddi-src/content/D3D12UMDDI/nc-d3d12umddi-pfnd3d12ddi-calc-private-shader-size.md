---
UID: NC.d3d12umddi.PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE
title: PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE
author: windows-driver-content
description: 
ms.assetid: 9261f05a-71f0-41ce-8d91-bc9116a6826c
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

# PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE Pfnd3d12ddiCalcPrivateShaderSize; 

// Definition

SIZE_T Pfnd3d12ddiCalcPrivateShaderSize 
(
	 D3D12DDI_HDEVICE
	CONST UINT *pShaderCode
	 D3D12DDI_HROOTSIGNATURE
	CONST D3D12DDIARG_STAGE_IO_SIGNATURES *
)
{...}

PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *pShaderCode: 
### -param D3D12DDI_HROOTSIGNATURE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
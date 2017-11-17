---
UID: NC.d3d10umddi.PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE
title: PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE
author: windows-driver-content
description: 
ms.assetid: ca61d464-a515-47d3-b1a6-e31275f26cdf
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
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

# PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE Pfnd3d111DdiCalcprivatetessellationshadersize; 

// Definition

SIZE_T Pfnd3d111DdiCalcprivatetessellationshadersize 
(
	 D3D10DDI_HDEVICE
	CONST UINT *pShaderCode
	CONST D3D11_1DDIARG_TESSELLATION_IO_SIGNATURES *
)
{...}

PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *pShaderCode: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d12umddi.PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026
title: PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026
author: windows-driver-content
description: 
ms.assetid: 13355333-3f61-43d0-a192-a1d525455088
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

# PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026 Pfnd3d12ddiCalcPrivateShaderSize0026; 

// Definition

SIZE_T Pfnd3d12ddiCalcPrivateShaderSize0026 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDIARG_CREATE_SHADER_0026 *
)
{...}

PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
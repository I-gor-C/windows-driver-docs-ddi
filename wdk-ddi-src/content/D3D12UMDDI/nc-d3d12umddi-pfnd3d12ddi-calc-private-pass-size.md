---
UID: NC.d3d12umddi.PFND3D12DDI_CALC_PRIVATE_PASS_SIZE
title: PFND3D12DDI_CALC_PRIVATE_PASS_SIZE
author: windows-driver-content
description: 
ms.assetid: 8063ee2a-de37-480c-ba19-04b33c882f82
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

# PFND3D12DDI_CALC_PRIVATE_PASS_SIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALC_PRIVATE_PASS_SIZE Pfnd3d12ddiCalcPrivatePassSize; 

// Definition

SIZE_T Pfnd3d12ddiCalcPrivatePassSize 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDIARG_CREATE_PASS *
)
{...}

PFND3D12DDI_CALC_PRIVATE_PASS_SIZE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
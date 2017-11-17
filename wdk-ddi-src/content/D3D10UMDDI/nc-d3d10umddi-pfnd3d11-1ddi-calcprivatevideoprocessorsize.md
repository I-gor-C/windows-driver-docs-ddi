---
UID: NC.d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE
author: windows-driver-content
description: 
ms.assetid: cca0411a-8de8-4b1d-9207-cfbb8e81cc08
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

# PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE Pfnd3d111DdiCalcprivatevideoprocessorsize; 

// Definition

SIZE_T Pfnd3d111DdiCalcprivatevideoprocessorsize 
(
	 D3D10DDI_HDEVICE
	CONST D3D11_1DDIARG_CREATEVIDEOPROCESSOR *
)
{...}

PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE
author: windows-driver-content
description: 
ms.assetid: fe8e555a-0cbb-405e-bec1-4dc375d55121
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

# PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE Pfnd3d111DdiCalcprivatevideodecodersize; 

// Definition

SIZE_T Pfnd3d111DdiCalcprivatevideodecodersize 
(
	 D3D10DDI_HDEVICE
	CONST D3D11_1DDIARG_CREATEVIDEODECODER *
)
{...}

PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
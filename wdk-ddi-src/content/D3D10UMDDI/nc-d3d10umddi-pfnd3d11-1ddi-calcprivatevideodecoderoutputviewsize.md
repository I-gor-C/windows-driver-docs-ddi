---
UID: NC.d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE
author: windows-driver-content
description: 
ms.assetid: 8a9bcda3-8053-4bcb-86a9-5edc4b12b481
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

# PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE Pfnd3d111DdiCalcprivatevideodecoderoutputviewsize; 

// Definition

SIZE_T Pfnd3d111DdiCalcprivatevideodecoderoutputviewsize 
(
	 D3D10DDI_HDEVICE
	CONST D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW *
)
{...}

PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
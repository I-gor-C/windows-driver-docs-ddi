---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEODECODERBEGINFRAME
title: PFND3D11_1DDI_VIDEODECODERBEGINFRAME
author: windows-driver-content
description: 
ms.assetid: 132abfda-ac55-4408-b187-9d829e5cba5b
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

# PFND3D11_1DDI_VIDEODECODERBEGINFRAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEODECODERBEGINFRAME Pfnd3d111DdiVideodecoderbeginframe; 

// Definition

HRESULT Pfnd3d111DdiVideodecoderbeginframe 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HDECODE
	CONST D3D11_1DDIARG_VIDEODECODERBEGINFRAME *
)
{...}

PFND3D11_1DDI_VIDEODECODERBEGINFRAME 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HDECODE: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
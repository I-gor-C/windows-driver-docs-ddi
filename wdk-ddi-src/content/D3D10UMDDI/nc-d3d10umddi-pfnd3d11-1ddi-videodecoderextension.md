---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEODECODEREXTENSION
title: PFND3D11_1DDI_VIDEODECODEREXTENSION
author: windows-driver-content
description: 
ms.assetid: 2baf1735-345d-4e4f-91f1-e7f66af95286
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

# PFND3D11_1DDI_VIDEODECODEREXTENSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEODECODEREXTENSION Pfnd3d111DdiVideodecoderextension; 

// Definition

HRESULT Pfnd3d111DdiVideodecoderextension 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HDECODE
	CONST D3D11_1DDIARG_VIDEODECODEREXTENSION *
)
{...}

PFND3D11_1DDI_VIDEODECODEREXTENSION 


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
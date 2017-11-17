---
UID: NC.d3d10umddi.PFND3D11_1DDI_DESTROYVIDEODECODER
title: PFND3D11_1DDI_DESTROYVIDEODECODER
author: windows-driver-content
description: 
ms.assetid: b6d189ea-1abe-45fd-971d-5c260d02bbfb
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

# PFND3D11_1DDI_DESTROYVIDEODECODER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_DESTROYVIDEODECODER Pfnd3d111DdiDestroyvideodecoder; 

// Definition

VOID Pfnd3d111DdiDestroyvideodecoder 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HDECODE
)
{...}

PFND3D11_1DDI_DESTROYVIDEODECODER 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HDECODE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
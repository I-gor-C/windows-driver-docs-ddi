---
UID: NC.d3d10umddi.PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW
title: PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW
author: windows-driver-content
description: 
ms.assetid: b7e9b56a-f923-4c1f-a046-146c7f45aeda
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

# PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW Pfnd3d111DdiDestroyvideoprocessorinputview; 

// Definition

VOID Pfnd3d111DdiDestroyvideoprocessorinputview 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW
)
{...}

PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
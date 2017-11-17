---
UID: NC.d3d10umddi.PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM
title: PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM
author: windows-driver-content
description: 
ms.assetid: a1b5f58d-e3ba-4125-b83e-493daa2348aa
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

# PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM Pfnd3d111DdiDestroyvideoprocessorenum; 

// Definition

VOID Pfnd3d111DdiDestroyvideoprocessorenum 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSORENUM
)
{...}

PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSORENUM: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
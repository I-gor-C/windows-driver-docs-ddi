---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE
title: PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE
author: windows-driver-content
description: 
ms.assetid: 8dde8fa6-cef5-4416-b01b-8b87025fc715
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

# PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE Pfnd3d111DdiGetvideoprocessorcustomrate; 

// Definition

VOID Pfnd3d111DdiGetvideoprocessorcustomrate 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSORENUM
	 UINT
	 UINT
	D3D11_1DDI_VIDEO_PROCESSOR_CUSTOM_RATE *
)
{...}

PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSORENUM: 
### -param UINT: 
### -param UINT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
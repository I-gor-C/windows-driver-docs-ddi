---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS
title: PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS
author: windows-driver-content
description: 
ms.assetid: 9c9e12ca-0014-4bca-a592-9cfcdc51b4c2
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

# PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS Pfnd3d111DdiGetvideoprocessorrateconversioncaps; 

// Definition

VOID Pfnd3d111DdiGetvideoprocessorrateconversioncaps 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSORENUM
	 UINT
	D3D11_1DDI_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS *
)
{...}

PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSORENUM: 
### -param UINT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
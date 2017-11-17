---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORBLT
title: PFND3D11_1DDI_VIDEOPROCESSORBLT
author: windows-driver-content
description: 
ms.assetid: efaa11b8-15a2-41fe-b88e-7396d371df4a
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

# PFND3D11_1DDI_VIDEOPROCESSORBLT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEOPROCESSORBLT Pfnd3d111DdiVideoprocessorblt; 

// Definition

HRESULT Pfnd3d111DdiVideoprocessorblt 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSOR
	 D3D11_1DDI_HVIDEOPROCESSOROUTPUTVIEW
	 UINT
	 UINT
	CONST D3D11_1DDI_VIDEO_PROCESSOR_STREAM *
)
{...}

PFND3D11_1DDI_VIDEOPROCESSORBLT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSOR: 
### -param D3D11_1DDI_HVIDEOPROCESSOROUTPUTVIEW: 
### -param UINT: 
### -param UINT: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
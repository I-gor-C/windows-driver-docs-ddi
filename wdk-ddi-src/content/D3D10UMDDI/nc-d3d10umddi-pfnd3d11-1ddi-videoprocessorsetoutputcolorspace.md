---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE
title: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE
author: windows-driver-content
description: 
ms.assetid: 371e4592-c23c-424b-b067-eb165a736534
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

# PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE Pfnd3d111DdiVideoprocessorsetoutputcolorspace; 

// Definition

VOID Pfnd3d111DdiVideoprocessorsetoutputcolorspace 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSOR
	CONST D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE *
)
{...}

PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSOR: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
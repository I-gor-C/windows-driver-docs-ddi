---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT
title: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT
author: windows-driver-content
description: 
ms.assetid: 4aadfef4-dd69-4fe4-8215-7a5fc869b986
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

# PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT Pfnd3d111DdiVideoprocessorsetstreamstereoformat; 

// Definition

VOID Pfnd3d111DdiVideoprocessorsetstreamstereoformat 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSOR
	 UINT
	 BOOL
	 D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT
	 BOOL
	 BOOL
	 D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
	 int
)
{...}

PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSOR: 
### -param UINT: 
### -param BOOL: 
### -param D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT: 
### -param BOOL: 
### -param BOOL: 
### -param D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE: 
### -param int: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
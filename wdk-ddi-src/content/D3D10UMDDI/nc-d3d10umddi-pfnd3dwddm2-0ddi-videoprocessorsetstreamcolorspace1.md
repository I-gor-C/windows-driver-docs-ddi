---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1
title: PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1
author: windows-driver-content
description: 
ms.assetid: 97246bd5-d07c-4321-8fdc-bd0eda9d0343
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

# PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1 Pfnd3dwddm20DdiVideoprocessorsetstreamcolorspace1; 

// Definition

VOID Pfnd3dwddm20DdiVideoprocessorsetstreamcolorspace1 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor
	UINT StreamIndex
	D3DDDI_COLOR_SPACE_TYPE ColorSpace
)
{...}

PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1 


```

## -parameters

### -param hDevice: 
### -param hVideoProcessor: 
### -param StreamIndex: 
### -param ColorSpace: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
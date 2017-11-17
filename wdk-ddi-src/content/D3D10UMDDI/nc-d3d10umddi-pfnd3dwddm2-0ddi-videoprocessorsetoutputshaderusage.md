---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE
title: PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE
author: windows-driver-content
description: 
ms.assetid: 846efe55-f93e-4b9d-835f-a997fd0cb3c5
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

# PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE Pfnd3dwddm20DdiVideoprocessorsetoutputshaderusage; 

// Definition

VOID Pfnd3dwddm20DdiVideoprocessorsetoutputshaderusage 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor
	BOOL ShaderUsage
)
{...}

PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE 


```

## -parameters

### -param hDevice: 
### -param hVideoProcessor: 
### -param ShaderUsage: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE
title: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE
author: windows-driver-content
description: 
ms.assetid: f487573e-008b-4de3-9891-53edd7d9441f
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

# PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE Pfnd3d111DdiVideoprocessorsetoutputalphafillmode; 

// Definition

VOID Pfnd3d111DdiVideoprocessorsetoutputalphafillmode 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSOR
	 D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE
	 UINT
)
{...}

PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSOR: 
### -param D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE: 
### -param UINT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
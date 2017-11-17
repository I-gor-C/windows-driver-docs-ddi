---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR
title: PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR
author: windows-driver-content
description: 
ms.assetid: 37ae8606-5218-4cd4-9d3f-51fffe51c630
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

# PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR Pfnd3dwddm20DdiVideoprocessorsetstreammirror; 

// Definition

VOID Pfnd3dwddm20DdiVideoprocessorsetstreammirror 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor
	UINT StreamIndex
	BOOL Enable
	BOOL FlipHorizontal
	BOOL FlipVertical
)
{...}

PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR 


```

## -parameters

### -param hDevice: 
### -param hVideoProcessor: 
### -param StreamIndex: 
### -param Enable: 
### -param FlipHorizontal: 
### -param FlipVertical: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
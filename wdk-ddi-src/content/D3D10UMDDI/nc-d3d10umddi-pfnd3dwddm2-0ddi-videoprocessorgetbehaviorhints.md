---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS
title: PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS
author: windows-driver-content
description: 
ms.assetid: a756ad71-1360-4914-8ed8-6f53e3385480
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

# PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS Pfnd3dwddm20DdiVideoprocessorgetbehaviorhints; 

// Definition

HRESULT Pfnd3dwddm20DdiVideoprocessorgetbehaviorhints 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor
	UINT OutputWidth
	UINT OutputHeight
	DXGI_FORMAT OutputFormat
	UINT StreamCount
	 const D3DWDDM2_0DDI_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT *pStreams
	UINT *pBehaviorHints
)
{...}

PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS 


```

## -parameters

### -param hDevice: 
### -param hVideoProcessor: 
### -param OutputWidth: 
### -param OutputHeight: 
### -param OutputFormat: 
### -param StreamCount: 
### -param *pStreams: 
### -param *pBehaviorHints: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d10umddi.PFND3DWDDM2_1DDI_VIDEOPROCESSORSETOUTPUTHDRMETADATA
title: PFND3DWDDM2_1DDI_VIDEOPROCESSORSETOUTPUTHDRMETADATA
author: windows-driver-content
description: 
ms.assetid: 84b1f606-e963-48ee-9339-9ef8c259ce50
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

# PFND3DWDDM2_1DDI_VIDEOPROCESSORSETOUTPUTHDRMETADATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_1DDI_VIDEOPROCESSORSETOUTPUTHDRMETADATA Pfnd3dwddm21DdiVideoprocessorsetoutputhdrmetadata; 

// Definition

VOID Pfnd3dwddm21DdiVideoprocessorsetoutputhdrmetadata 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor
	D3DDDI_HDR_METADATA_TYPE Type
	UINT Size
	CONST VOID *pMetaData
)
{...}

PFND3DWDDM2_1DDI_VIDEOPROCESSORSETOUTPUTHDRMETADATA 


```

## -parameters

### -param hDevice: 
### -param hVideoProcessor: 
### -param Type: 
### -param Size: 
### -param *pMetaData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
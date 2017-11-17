---
UID: NC.d3d10umddi.PFND3DWDDM2_1DDI_VIDEOPROCESSORSETSTREAMHDRMETADATA
title: PFND3DWDDM2_1DDI_VIDEOPROCESSORSETSTREAMHDRMETADATA
author: windows-driver-content
description: 
ms.assetid: 1c65569c-8ca9-40d3-a049-308c0b9be27c
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

# PFND3DWDDM2_1DDI_VIDEOPROCESSORSETSTREAMHDRMETADATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_1DDI_VIDEOPROCESSORSETSTREAMHDRMETADATA Pfnd3dwddm21DdiVideoprocessorsetstreamhdrmetadata; 

// Definition

VOID Pfnd3dwddm21DdiVideoprocessorsetstreamhdrmetadata 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor
	UINT StreamIndex
	D3DDDI_HDR_METADATA_TYPE Type
	UINT Size
	CONST VOID *pMetaData
)
{...}

PFND3DWDDM2_1DDI_VIDEOPROCESSORSETSTREAMHDRMETADATA 


```

## -parameters

### -param hDevice: 
### -param hVideoProcessor: 
### -param StreamIndex: 
### -param Type: 
### -param Size: 
### -param *pMetaData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING
title: PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING
author: windows-driver-content
description: 
ms.assetid: b7ce1453-f316-47fb-ad2e-448bd9383515
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

# PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING Pfnd3dwddm20DdiVideodecoderupdatedownsampling; 

// Definition

HRESULT Pfnd3dwddm20DdiVideodecoderupdatedownsampling 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HDECODE hDecoder
	CONST D3D11_1DDI_VIDEO_DECODER_DESC *pOutputDesc
	D3DDDI_COLOR_SPACE_TYPE OutputColorSpace
)
{...}

PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING 


```

## -parameters

### -param hDevice: 
### -param hDecoder: 
### -param *pOutputDesc: 
### -param OutputColorSpace: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
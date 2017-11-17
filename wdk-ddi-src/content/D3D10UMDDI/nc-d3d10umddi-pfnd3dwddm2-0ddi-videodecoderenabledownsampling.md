---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING
title: PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING
author: windows-driver-content
description: 
ms.assetid: f4c65ef4-5db1-4cf0-aff3-794c066b03a9
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

# PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING Pfnd3dwddm20DdiVideodecoderenabledownsampling; 

// Definition

HRESULT Pfnd3dwddm20DdiVideodecoderenabledownsampling 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HDECODE hDecoder
	D3DDDI_COLOR_SPACE_TYPE InputColorSpace
	CONST D3D11_1DDI_VIDEO_DECODER_DESC *pOutputDesc
	D3DDDI_COLOR_SPACE_TYPE OutputColorSpace
	UINT ReferenceFrameCount
)
{...}

PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING 


```

## -parameters

### -param hDevice: 
### -param hDecoder: 
### -param InputColorSpace: 
### -param *pOutputDesc: 
### -param OutputColorSpace: 
### -param ReferenceFrameCount: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
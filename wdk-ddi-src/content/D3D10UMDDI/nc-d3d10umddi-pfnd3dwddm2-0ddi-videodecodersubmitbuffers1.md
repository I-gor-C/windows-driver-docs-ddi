---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1
title: PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1
author: windows-driver-content
description: 
ms.assetid: 205b6caa-1a1e-4bb2-8c27-35b6504475ca
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

# PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1 Pfnd3dwddm20DdiVideodecodersubmitbuffers1; 

// Definition

HRESULT Pfnd3dwddm20DdiVideodecodersubmitbuffers1 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HDECODE hDecode
	UINT BufferCount
	CONST D3DWDDM2_0DDI_VIDEO_DECODER_BUFFER_DESC1 *pBufferDesc
)
{...}

PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1 


```

## -parameters

### -param hDevice: 
### -param hDecode: 
### -param BufferCount: 
### -param *pBufferDesc: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
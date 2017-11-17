---
UID: NC.d3d10umddi.PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS
title: PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS
author: windows-driver-content
description: 
ms.assetid: b56c56c3-62da-442b-9f71-095ef7eeba4e
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

# PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS Pfnd3d111DdiVideodecodersubmitbuffers; 

// Definition

HRESULT Pfnd3d111DdiVideodecodersubmitbuffers 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HDECODE
	 UINT
	CONST D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC *
)
{...}

PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HDECODE: 
### -param UINT: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
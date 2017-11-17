---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERCONFIG
title: PFND3D11_1DDI_GETVIDEODECODERCONFIG
author: windows-driver-content
description: 
ms.assetid: 8a227d17-2a8a-4e8f-bf20-098b25510f0d
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

# PFND3D11_1DDI_GETVIDEODECODERCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEODECODERCONFIG Pfnd3d111DdiGetvideodecoderconfig; 

// Definition

VOID Pfnd3d111DdiGetvideodecoderconfig 
(
	 D3D10DDI_HDEVICE
	CONST D3D11_1DDI_VIDEO_DECODER_DESC *
	 UINT
	D3D11_1DDI_VIDEO_DECODER_CONFIG *
)
{...}

PFND3D11_1DDI_GETVIDEODECODERCONFIG 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param UINT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
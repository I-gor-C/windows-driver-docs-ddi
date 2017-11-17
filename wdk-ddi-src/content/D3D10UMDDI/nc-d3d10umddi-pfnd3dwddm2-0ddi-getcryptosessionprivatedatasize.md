---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE
title: PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE
author: windows-driver-content
description: 
ms.assetid: eb348e6d-1af0-4afc-811e-2f7ec19dd7ba
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

# PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE Pfnd3dwddm20DdiGetcryptosessionprivatedatasize; 

// Definition

void Pfnd3dwddm20DdiGetcryptosessionprivatedatasize 
(
	D3D10DDI_HDEVICE hDevice
	CONST GUID *pCryptoType
	CONST GUID *pDecoderProfile
	CONST GUID *pKeyExchangeType
	UINT *pPrivateInputSize
	UINT *pPrivateOutputSize
)
{...}

PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE 


```

## -parameters

### -param hDevice: 
### -param *pCryptoType: 
### -param *pDecoderProfile: 
### -param *pKeyExchangeType: 
### -param *pPrivateInputSize: 
### -param *pPrivateOutputSize: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
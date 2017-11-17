---
UID: NC.d3d10umddi.PFND3D11_1DDI_CREATECRYPTOSESSION
title: PFND3D11_1DDI_CREATECRYPTOSESSION
author: windows-driver-content
description: 
ms.assetid: e679d871-1d87-4f29-b63d-11d13f218b4d
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

# PFND3D11_1DDI_CREATECRYPTOSESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CREATECRYPTOSESSION Pfnd3d111DdiCreatecryptosession; 

// Definition

HRESULT Pfnd3d111DdiCreatecryptosession 
(
	D3D10DDI_HDEVICE hDevice
	CONST D3D11_1DDIARG_CREATECRYPTOSESSION *pCreateData
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
	D3D11_1DDI_HRTCRYPTOSESSION hRTCryptoSession
)
{...}

PFND3D11_1DDI_CREATECRYPTOSESSION 


```

## -parameters

### -param hDevice: 
### -param *pCreateData: 
### -param hCryptoSession: 
### -param hRTCryptoSession: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
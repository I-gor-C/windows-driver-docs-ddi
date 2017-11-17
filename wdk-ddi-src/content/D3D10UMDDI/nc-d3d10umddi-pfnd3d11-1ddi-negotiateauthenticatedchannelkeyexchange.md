---
UID: NC.d3d10umddi.PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE
title: PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE
author: windows-driver-content
description: 
ms.assetid: c6659624-2fc5-43bd-9d94-59a1091d34cb
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

# PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE Pfnd3d111DdiNegotiateauthenticatedchannelkeyexchange; 

// Definition

HRESULT Pfnd3d111DdiNegotiateauthenticatedchannelkeyexchange 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HAUTHCHANNEL hCAuthChannel
	UINT DataSize
	VOID *pData
)
{...}

PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE 


```

## -parameters

### -param hDevice: 
### -param hCAuthChannel: 
### -param DataSize: 
### -param *pData: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d10umddi.PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE
title: PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE
author: windows-driver-content
description: 
ms.assetid: cc2ba778-5e6d-4e60-8b12-2e2948ab6a51
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

# PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE Pfnd3d111DdiCryptosessiongethandle; 

// Definition

HRESULT Pfnd3d111DdiCryptosessiongethandle 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
	HANDLE *pHandle
)
{...}

PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE 


```

## -parameters

### -param hDevice: 
### -param hCryptoSession: 
### -param *pHandle: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS
title: PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS
author: windows-driver-content
description: 
ms.assetid: 263c99cf-809d-4925-8974-aa11818589b1
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

# PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS Pfnd3dwddm20DdiCheckcryptosessionstatus; 

// Definition

void Pfnd3dwddm20DdiCheckcryptosessionstatus 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
	D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS *pStatus
)
{...}

PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS 


```

## -parameters

### -param hDevice: 
### -param hCryptoSession: 
### -param *pStatus: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
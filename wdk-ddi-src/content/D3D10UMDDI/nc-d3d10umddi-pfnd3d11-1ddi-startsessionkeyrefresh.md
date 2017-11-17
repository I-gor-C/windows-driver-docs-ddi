---
UID: NC.d3d10umddi.PFND3D11_1DDI_STARTSESSIONKEYREFRESH
title: PFND3D11_1DDI_STARTSESSIONKEYREFRESH
author: windows-driver-content
description: 
ms.assetid: 32763b3d-bd71-42f3-8941-138142d83ba5
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

# PFND3D11_1DDI_STARTSESSIONKEYREFRESH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_STARTSESSIONKEYREFRESH Pfnd3d111DdiStartsessionkeyrefresh; 

// Definition

VOID Pfnd3d111DdiStartsessionkeyrefresh 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
	UINT RandomNumberSize
	VOID *pRandomNumber
)
{...}

PFND3D11_1DDI_STARTSESSIONKEYREFRESH 


```

## -parameters

### -param hDevice: 
### -param hCryptoSession: 
### -param RandomNumberSize: 
### -param *pRandomNumber: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
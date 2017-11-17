---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETENCRYPTIONBLTKEY
title: PFND3D11_1DDI_GETENCRYPTIONBLTKEY
author: windows-driver-content
description: 
ms.assetid: cc3fa2ca-c347-468d-aef5-74e1965390af
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

# PFND3D11_1DDI_GETENCRYPTIONBLTKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETENCRYPTIONBLTKEY Pfnd3d111DdiGetencryptionbltkey; 

// Definition

VOID Pfnd3d111DdiGetencryptionbltkey 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
	UINT KeySize
	VOID *pReadbackKey
)
{...}

PFND3D11_1DDI_GETENCRYPTIONBLTKEY 


```

## -parameters

### -param hDevice: 
### -param hCryptoSession: 
### -param KeySize: 
### -param *pReadbackKey: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3dumddi.PFND3DDDI_INVALIDATECACHECB
title: PFND3DDDI_INVALIDATECACHECB
author: windows-driver-content
description: 
ms.assetid: 870b79f4-1459-4f4a-8fca-361d9800f5e9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dumddi.h
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

# PFND3DDDI_INVALIDATECACHECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_INVALIDATECACHECB Pfnd3dddiInvalidatecachecb; 

// Definition

HRESULT Pfnd3dddiInvalidatecachecb 
(
	HANDLE hDevice
	CONST D3DDDICB_INVALIDATECACHE *
)
{...}

PFND3DDDI_INVALIDATECACHECB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3dumddi.PFND3DDDI_SYNCTOKENCB
title: PFND3DDDI_SYNCTOKENCB
author: windows-driver-content
description: 
ms.assetid: 2ebb00b5-7c91-4fee-b66b-88faec67a951
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

# PFND3DDDI_SYNCTOKENCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_SYNCTOKENCB Pfnd3dddiSynctokencb; 

// Definition

HRESULT Pfnd3dddiSynctokencb 
(
	HANDLE hDevice
	CONST D3DDDICB_SYNCTOKEN *
)
{...}

PFND3DDDI_SYNCTOKENCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
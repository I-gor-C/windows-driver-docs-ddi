---
UID: NC.d3dumddi.PFND3DDDI_SYNCTOKEN
title: PFND3DDDI_SYNCTOKEN
author: windows-driver-content
description: 
ms.assetid: 95a4e168-6d6f-4472-8fda-b2dcab64c1c9
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

# PFND3DDDI_SYNCTOKEN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_SYNCTOKEN Pfnd3dddiSynctoken; 

// Definition

VOID Pfnd3dddiSynctoken 
(
	HANDLE hDevice
	CONST D3DDDIARG_SYNCTOKEN *
)
{...}

PFND3DDDI_SYNCTOKEN 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
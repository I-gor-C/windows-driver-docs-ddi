---
UID: NC.d3dumddi.PFND3DDDI_RECLAIMALLOCATIONS2CB
title: PFND3DDDI_RECLAIMALLOCATIONS2CB
author: windows-driver-content
description: 
ms.assetid: 37042b6b-1a6a-403c-810a-ba009db4ae84
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

# PFND3DDDI_RECLAIMALLOCATIONS2CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_RECLAIMALLOCATIONS2CB Pfnd3dddiReclaimallocations2cb; 

// Definition

HRESULT Pfnd3dddiReclaimallocations2cb 
(
	HANDLE hDevice
	D3DDDICB_RECLAIMALLOCATIONS2 *
)
{...}

PFND3DDDI_RECLAIMALLOCATIONS2CB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
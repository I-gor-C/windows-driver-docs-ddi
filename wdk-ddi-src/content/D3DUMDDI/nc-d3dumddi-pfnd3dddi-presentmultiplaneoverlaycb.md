---
UID: NC.d3dumddi.PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB
title: PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB
author: windows-driver-content
description: 
ms.assetid: 859cb2f5-c622-4083-bc42-f465784ff77a
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

# PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB Pfnd3dddiPresentmultiplaneoverlaycb; 

// Definition

HRESULT Pfnd3dddiPresentmultiplaneoverlaycb 
(
	HANDLE hDevice
	CONST D3DDDICB_PRESENTMULTIPLANEOVERLAY *
)
{...}

PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
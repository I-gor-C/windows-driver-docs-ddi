---
UID: NC.d3dumddi.PFND3DDDI_PRESENTMULTIPLANEOVERLAY
title: PFND3DDDI_PRESENTMULTIPLANEOVERLAY
author: windows-driver-content
description: 
ms.assetid: e9a5ba30-60fa-4e4e-a3ae-1ddfa7e72f38
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

# PFND3DDDI_PRESENTMULTIPLANEOVERLAY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_PRESENTMULTIPLANEOVERLAY Pfnd3dddiPresentmultiplaneoverlay; 

// Definition

HRESULT Pfnd3dddiPresentmultiplaneoverlay 
(
	HANDLE hDevice
	CONST D3DDDIARG_PRESENTMULTIPLANEOVERLAY *
)
{...}

PFND3DDDI_PRESENTMULTIPLANEOVERLAY 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
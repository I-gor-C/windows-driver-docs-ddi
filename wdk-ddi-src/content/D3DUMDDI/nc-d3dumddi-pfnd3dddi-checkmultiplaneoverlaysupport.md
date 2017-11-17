---
UID: NC.d3dumddi.PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT
title: PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: 
ms.assetid: eedcbd82-62a0-496a-b9be-d4aeb13dd0fb
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

# PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT Pfnd3dddiCheckmultiplaneoverlaysupport; 

// Definition

HRESULT Pfnd3dddiCheckmultiplaneoverlaysupport 
(
	HANDLE hDevice
	D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT *
)
{...}

PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3dumddi.PFND3DDDI_CREATECONTEXTCB
title: PFND3DDDI_CREATECONTEXTCB
author: windows-driver-content
description: 
ms.assetid: 4f5835df-91b1-409c-ab85-884c63286ebb
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

# PFND3DDDI_CREATECONTEXTCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_CREATECONTEXTCB Pfnd3dddiCreatecontextcb; 

// Definition

HRESULT Pfnd3dddiCreatecontextcb 
(
	HANDLE hDevice
	D3DDDICB_CREATECONTEXT *
)
{...}

PFND3DDDI_CREATECONTEXTCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
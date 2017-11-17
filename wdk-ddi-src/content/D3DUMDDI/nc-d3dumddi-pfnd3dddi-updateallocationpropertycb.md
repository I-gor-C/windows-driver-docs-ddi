---
UID: NC.d3dumddi.PFND3DDDI_UPDATEALLOCATIONPROPERTYCB
title: PFND3DDDI_UPDATEALLOCATIONPROPERTYCB
author: windows-driver-content
description: 
ms.assetid: 8a2fe1dc-c3aa-4c68-b93c-59b024f710b3
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

# PFND3DDDI_UPDATEALLOCATIONPROPERTYCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_UPDATEALLOCATIONPROPERTYCB Pfnd3dddiUpdateallocationpropertycb; 

// Definition

HRESULT Pfnd3dddiUpdateallocationpropertycb 
(
	HANDLE hDevice
	D3DDDI_UPDATEALLOCPROPERTY *
)
{...}

PFND3DDDI_UPDATEALLOCATIONPROPERTYCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
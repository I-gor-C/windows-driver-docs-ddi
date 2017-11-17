---
UID: NC.d3dumddi.PFND3DDDI_RECLAIMALLOCATIONSCB
title: PFND3DDDI_RECLAIMALLOCATIONSCB
author: windows-driver-content
description: 
ms.assetid: 1144097a-f24f-4493-900c-9e964992e140
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

# PFND3DDDI_RECLAIMALLOCATIONSCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_RECLAIMALLOCATIONSCB Pfnd3dddiReclaimallocationscb; 

// Definition

HRESULT Pfnd3dddiReclaimallocationscb 
(
	HANDLE hDevice
	CONST D3DDDICB_RECLAIMALLOCATIONS *
)
{...}

PFND3DDDI_RECLAIMALLOCATIONSCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3dumddi.PFND3DDDI_OFFERALLOCATIONSCB
title: PFND3DDDI_OFFERALLOCATIONSCB
author: windows-driver-content
description: 
ms.assetid: 741dba4c-b50d-4104-a7d9-5bf92fb3bc4b
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

# PFND3DDDI_OFFERALLOCATIONSCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_OFFERALLOCATIONSCB Pfnd3dddiOfferallocationscb; 

// Definition

HRESULT Pfnd3dddiOfferallocationscb 
(
	HANDLE hDevice
	CONST D3DDDICB_OFFERALLOCATIONS *
)
{...}

PFND3DDDI_OFFERALLOCATIONSCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
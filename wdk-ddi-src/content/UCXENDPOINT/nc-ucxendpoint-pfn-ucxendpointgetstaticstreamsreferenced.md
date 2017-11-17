---
UID: NC.ucxendpoint.PFN_UCXENDPOINTGETSTATICSTREAMSREFERENCED
title: PFN_UCXENDPOINTGETSTATICSTREAMSREFERENCED
author: windows-driver-content
description: 
ms.assetid: 9cf8ca26-79b0-42f8-a31d-138e8b3203a1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxendpoint.h
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

# PFN_UCXENDPOINTGETSTATICSTREAMSREFERENCED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXENDPOINTGETSTATICSTREAMSREFERENCED PfnUcxendpointgetstaticstreamsreferenced; 

// Definition

WDFAPI PfnUcxendpointgetstaticstreamsreferenced 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXENDPOINT Endpoint
	PVOID Tag
)
{...}

PFN_UCXENDPOINTGETSTATICSTREAMSREFERENCED 


```

## -parameters

### -param DriverGlobals: 
### -param Endpoint: 
### -param Tag: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
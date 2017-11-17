---
UID: NC.ucxendpoint.PFN_UCXENDPOINTPURGECOMPLETE
title: PFN_UCXENDPOINTPURGECOMPLETE
author: windows-driver-content
description: 
ms.assetid: bdfca55d-ecf0-415c-8b11-7cc68853450e
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

# PFN_UCXENDPOINTPURGECOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXENDPOINTPURGECOMPLETE PfnUcxendpointpurgecomplete; 

// Definition

WDFAPI PfnUcxendpointpurgecomplete 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXENDPOINT Endpoint
)
{...}

PFN_UCXENDPOINTPURGECOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Endpoint: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
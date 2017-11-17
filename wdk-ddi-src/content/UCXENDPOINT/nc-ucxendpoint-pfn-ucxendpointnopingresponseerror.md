---
UID: NC.ucxendpoint.PFN_UCXENDPOINTNOPINGRESPONSEERROR
title: PFN_UCXENDPOINTNOPINGRESPONSEERROR
author: windows-driver-content
description: 
ms.assetid: d5c0c29d-78db-4628-bd5c-084aad288e13
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

# PFN_UCXENDPOINTNOPINGRESPONSEERROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXENDPOINTNOPINGRESPONSEERROR PfnUcxendpointnopingresponseerror; 

// Definition

WDFAPI PfnUcxendpointnopingresponseerror 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXENDPOINT Endpoint
)
{...}

PFN_UCXENDPOINTNOPINGRESPONSEERROR 


```

## -parameters

### -param DriverGlobals: 
### -param Endpoint: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
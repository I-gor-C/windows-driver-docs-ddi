---
UID: NC.ucxendpoint.PFN_UCXENDPOINTSETWDFIOQUEUE
title: *PFN_UCXENDPOINTSETWDFIOQUEUE
author: windows-driver-content
description: 
ms.assetid: 11dfa55e-6753-45cd-9b2d-a6fc939ec4d8
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

# *PFN_UCXENDPOINTSETWDFIOQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UCXENDPOINTSETWDFIOQUEUE *PfnUcxendpointsetwdfioqueue; 

// Definition

VOID *PfnUcxendpointsetwdfioqueue 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXENDPOINT Endpoint
	WDFQUEUE WdfQueue
)
{...}

*PFN_UCXENDPOINTSETWDFIOQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param Endpoint: 
### -param WdfQueue: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
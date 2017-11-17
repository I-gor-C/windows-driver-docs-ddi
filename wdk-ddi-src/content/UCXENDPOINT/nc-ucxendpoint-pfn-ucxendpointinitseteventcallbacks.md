---
UID: NC.ucxendpoint.PFN_UCXENDPOINTINITSETEVENTCALLBACKS
title: *PFN_UCXENDPOINTINITSETEVENTCALLBACKS
author: windows-driver-content
description: 
ms.assetid: 0b3a0111-b766-40f1-a4de-d78c4023ee74
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

# *PFN_UCXENDPOINTINITSETEVENTCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UCXENDPOINTINITSETEVENTCALLBACKS *PfnUcxendpointinitseteventcallbacks; 

// Definition

VOID *PfnUcxendpointinitseteventcallbacks 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	PUCXENDPOINT_INIT EndpointInit
	PUCX_ENDPOINT_EVENT_CALLBACKS EventCallbacks
)
{...}

*PFN_UCXENDPOINTINITSETEVENTCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param EndpointInit: 
### -param EventCallbacks: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.udecxusbendpoint.PFN_UDECXUSBENDPOINTSETWDFIOQUEUE
title: *PFN_UDECXUSBENDPOINTSETWDFIOQUEUE
author: windows-driver-content
description: 
ms.assetid: 0275cd3f-7d24-4067-af74-d5bff74abecd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbendpoint.h
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

# *PFN_UDECXUSBENDPOINTSETWDFIOQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBENDPOINTSETWDFIOQUEUE *PfnUdecxusbendpointsetwdfioqueue; 

// Definition

VOID *PfnUdecxusbendpointsetwdfioqueue 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	UDECXUSBENDPOINT UdecxUsbEndpoint
	WDFQUEUE WdfQueue
)
{...}

*PFN_UDECXUSBENDPOINTSETWDFIOQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbEndpoint: 
### -param WdfQueue: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
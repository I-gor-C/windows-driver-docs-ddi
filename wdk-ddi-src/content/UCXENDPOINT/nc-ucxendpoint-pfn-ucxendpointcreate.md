---
UID: NC.ucxendpoint.PFN_UCXENDPOINTCREATE
title: PFN_UCXENDPOINTCREATE
author: windows-driver-content
description: 
ms.assetid: 5076592c-3f81-4298-9818-d096cd9bbd0c
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

# PFN_UCXENDPOINTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXENDPOINTCREATE PfnUcxendpointcreate; 

// Definition

WDFAPI PfnUcxendpointcreate 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXUSBDEVICE UsbDevice
	PUCXENDPOINT_INIT *EndpointInit
	PWDF_OBJECT_ATTRIBUTES Attributes
	UCXENDPOINT *Endpoint
)
{...}

PFN_UCXENDPOINTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param *EndpointInit: 
### -param Attributes: 
### -param *Endpoint: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITSETENDPOINTSTYPE
title: *PFN_UDECXUSBDEVICEINITSETENDPOINTSTYPE
author: windows-driver-content
description: 
ms.assetid: 9c4147dd-2810-498e-a962-e6966407aa75
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbdevice.h
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

# *PFN_UDECXUSBDEVICEINITSETENDPOINTSTYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITSETENDPOINTSTYPE *PfnUdecxusbdeviceinitsetendpointstype; 

// Definition

VOID *PfnUdecxusbdeviceinitsetendpointstype 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit
	UDECX_ENDPOINT_TYPE UdecxEndpointType
)
{...}

*PFN_UDECXUSBDEVICEINITSETENDPOINTSTYPE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDeviceInit: 
### -param UdecxEndpointType: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
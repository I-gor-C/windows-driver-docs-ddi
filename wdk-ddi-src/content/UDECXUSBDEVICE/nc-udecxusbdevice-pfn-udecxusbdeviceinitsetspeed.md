---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITSETSPEED
title: *PFN_UDECXUSBDEVICEINITSETSPEED
author: windows-driver-content
description: 
ms.assetid: d422b6a0-06dc-489c-9dea-d3a3a2bbe23f
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

# *PFN_UDECXUSBDEVICEINITSETSPEED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITSETSPEED *PfnUdecxusbdeviceinitsetspeed; 

// Definition

VOID *PfnUdecxusbdeviceinitsetspeed 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit
	UDECX_USB_DEVICE_SPEED UsbDeviceSpeed
)
{...}

*PFN_UDECXUSBDEVICEINITSETSPEED 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDeviceInit: 
### -param UsbDeviceSpeed: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITSETSTATECHANGECALLBACKS
title: *PFN_UDECXUSBDEVICEINITSETSTATECHANGECALLBACKS
author: windows-driver-content
description: 
ms.assetid: 81bdb21b-24b9-401a-aa31-0c5e606a7eb3
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

# *PFN_UDECXUSBDEVICEINITSETSTATECHANGECALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITSETSTATECHANGECALLBACKS *PfnUdecxusbdeviceinitsetstatechangecallbacks; 

// Definition

VOID *PfnUdecxusbdeviceinitsetstatechangecallbacks 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit
	PUDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS Callbacks
)
{...}

*PFN_UDECXUSBDEVICEINITSETSTATECHANGECALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDeviceInit: 
### -param Callbacks: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
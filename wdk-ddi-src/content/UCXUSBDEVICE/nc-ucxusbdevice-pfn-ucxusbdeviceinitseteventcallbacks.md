---
UID: NC.ucxusbdevice.PFN_UCXUSBDEVICEINITSETEVENTCALLBACKS
title: *PFN_UCXUSBDEVICEINITSETEVENTCALLBACKS
author: windows-driver-content
description: 
ms.assetid: 40863398-fc30-4ce6-bd0f-b50e2cb9ce0c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxusbdevice.h
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

# *PFN_UCXUSBDEVICEINITSETEVENTCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UCXUSBDEVICEINITSETEVENTCALLBACKS *PfnUcxusbdeviceinitseteventcallbacks; 

// Definition

VOID *PfnUcxusbdeviceinitseteventcallbacks 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	PUCXUSBDEVICE_INIT UsbDeviceInit
	PUCX_USBDEVICE_EVENT_CALLBACKS EventCallbacks
)
{...}

*PFN_UCXUSBDEVICEINITSETEVENTCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDeviceInit: 
### -param EventCallbacks: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
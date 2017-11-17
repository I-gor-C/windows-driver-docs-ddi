---
UID: NC.ucxusbdevice.PFN_UCXUSBDEVICEREMOTEWAKENOTIFICATION
title: PFN_UCXUSBDEVICEREMOTEWAKENOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 40059922-2e99-43e1-a85b-2f15c73e1c41
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

# PFN_UCXUSBDEVICEREMOTEWAKENOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXUSBDEVICEREMOTEWAKENOTIFICATION PfnUcxusbdeviceremotewakenotification; 

// Definition

WDFAPI PfnUcxusbdeviceremotewakenotification 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXUSBDEVICE UsbDevice
	ULONG Interface
)
{...}

PFN_UCXUSBDEVICEREMOTEWAKENOTIFICATION 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Interface: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
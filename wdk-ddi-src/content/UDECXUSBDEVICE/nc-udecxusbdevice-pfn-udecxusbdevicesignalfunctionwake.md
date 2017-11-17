---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICESIGNALFUNCTIONWAKE
title: *PFN_UDECXUSBDEVICESIGNALFUNCTIONWAKE
author: windows-driver-content
description: 
ms.assetid: b64c6255-1304-416b-800d-2377718f8acb
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

# *PFN_UDECXUSBDEVICESIGNALFUNCTIONWAKE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICESIGNALFUNCTIONWAKE *PfnUdecxusbdevicesignalfunctionwake; 

// Definition

VOID *PfnUdecxusbdevicesignalfunctionwake 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	UDECXUSBDEVICE UdecxUsbDevice
	ULONG Interface
)
{...}

*PFN_UDECXUSBDEVICESIGNALFUNCTIONWAKE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDevice: 
### -param Interface: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
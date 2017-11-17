---
UID: NC.ursdevice.PFN_URSREPORTHARDWAREEVENT
title: PFN_URSREPORTHARDWAREEVENT
author: windows-driver-content
description: 
ms.assetid: 04cdef2c-601a-49ad-98c0-559691523857
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ursdevice.h
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

# PFN_URSREPORTHARDWAREEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_URSREPORTHARDWAREEVENT PfnUrsreporthardwareevent; 

// Definition

WDFAPI PfnUrsreporthardwareevent 
(
	PURS_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	URS_HARDWARE_EVENT HardwareEvent
)
{...}

PFN_URSREPORTHARDWAREEVENT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param HardwareEvent: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
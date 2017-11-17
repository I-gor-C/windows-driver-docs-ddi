---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTCREATE
title: PFN_WDFINTERRUPTCREATE
author: windows-driver-content
description: 
ms.assetid: b35efd87-d259-4ca5-9ad8-5e920abbea53
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfinterrupt.h
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

# PFN_WDFINTERRUPTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTCREATE PfnWdfinterruptcreate; 

// Definition

WDFAPI PfnWdfinterruptcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_INTERRUPT_CONFIG Configuration
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFINTERRUPT *Interrupt
)
{...}

PFN_WDFINTERRUPTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Configuration: 
### -param Attributes: 
### -param *Interrupt: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTGETDEVICE
title: *PFN_WDFINTERRUPTGETDEVICE
author: windows-driver-content
description: 
ms.assetid: 4a71746e-071a-4e76-8066-1e35f48fa303
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

# *PFN_WDFINTERRUPTGETDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFINTERRUPTGETDEVICE *PfnWdfinterruptgetdevice; 

// Definition

WDFDEVICE *PfnWdfinterruptgetdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
)
{...}

*PFN_WDFINTERRUPTGETDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns WDFDEVICE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
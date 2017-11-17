---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTGETINFO
title: PFN_WDFINTERRUPTGETINFO
author: windows-driver-content
description: 
ms.assetid: 09a4b75f-b6af-4a24-8a59-6b284399e0ba
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

# PFN_WDFINTERRUPTGETINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTGETINFO PfnWdfinterruptgetinfo; 

// Definition

WDFAPI PfnWdfinterruptgetinfo 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
	PWDF_INTERRUPT_INFO Info
)
{...}

PFN_WDFINTERRUPTGETINFO 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 
### -param Info: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
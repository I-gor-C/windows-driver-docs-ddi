---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTSYNCHRONIZE
title: PFN_WDFINTERRUPTSYNCHRONIZE
author: windows-driver-content
description: 
ms.assetid: c885d431-654e-4284-9028-6076ccefa693
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

# PFN_WDFINTERRUPTSYNCHRONIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTSYNCHRONIZE PfnWdfinterruptsynchronize; 

// Definition

WDFAPI PfnWdfinterruptsynchronize 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
	PFN_WDF_INTERRUPT_SYNCHRONIZE Callback
	WDFCONTEXT Context
)
{...}

PFN_WDFINTERRUPTSYNCHRONIZE 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 
### -param Callback: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
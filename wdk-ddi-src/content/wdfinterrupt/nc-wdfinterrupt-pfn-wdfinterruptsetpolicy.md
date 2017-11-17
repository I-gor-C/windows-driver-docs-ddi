---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTSETPOLICY
title: PFN_WDFINTERRUPTSETPOLICY
author: windows-driver-content
description: 
ms.assetid: 4b77c856-2950-4663-a76e-03a174974523
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

# PFN_WDFINTERRUPTSETPOLICY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTSETPOLICY PfnWdfinterruptsetpolicy; 

// Definition

WDFAPI PfnWdfinterruptsetpolicy 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
	WDF_INTERRUPT_POLICY Policy
	WDF_INTERRUPT_PRIORITY Priority
	KAFFINITY TargetProcessorSet
)
{...}

PFN_WDFINTERRUPTSETPOLICY 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 
### -param Policy: 
### -param Priority: 
### -param TargetProcessorSet: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
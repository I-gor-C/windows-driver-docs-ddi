---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTTRYTOACQUIRELOCK
title: PFN_WDFINTERRUPTTRYTOACQUIRELOCK
author: windows-driver-content
description: 
ms.assetid: 9f5435d2-d4d1-4c37-af7a-83f6c66e73e2
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

# PFN_WDFINTERRUPTTRYTOACQUIRELOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTTRYTOACQUIRELOCK PfnWdfinterrupttrytoacquirelock; 

// Definition

WDFAPI PfnWdfinterrupttrytoacquirelock 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_not_held_(_Curr_)WDFINTERRUPT Interrupt
)
{...}

PFN_WDFINTERRUPTTRYTOACQUIRELOCK 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
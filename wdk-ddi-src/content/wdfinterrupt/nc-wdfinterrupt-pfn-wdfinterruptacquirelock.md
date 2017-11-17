---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTACQUIRELOCK
title: PFN_WDFINTERRUPTACQUIRELOCK
author: windows-driver-content
description: 
ms.assetid: fde146bc-09c7-4a3a-a80c-3e628c048e02
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

# PFN_WDFINTERRUPTACQUIRELOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTACQUIRELOCK PfnWdfinterruptacquirelock; 

// Definition

WDFAPI PfnWdfinterruptacquirelock 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_not_held_(_Curr_)_Acquires_lock_(_Curr_) WDFINTERRUPT
)
{...}

PFN_WDFINTERRUPTACQUIRELOCK 


```

## -parameters

### -param DriverGlobals: 
### -param WDFINTERRUPT: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
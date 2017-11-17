---
UID: NC.wdfsync.PFN_WDFSPINLOCKACQUIRE
title: PFN_WDFSPINLOCKACQUIRE
author: windows-driver-content
description: 
ms.assetid: e99e8042-0552-401d-8cfd-615cb01c16e3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfsync.h
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

# PFN_WDFSPINLOCKACQUIRE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFSPINLOCKACQUIRE PfnWdfspinlockacquire; 

// Definition

WDFAPI PfnWdfspinlockacquire 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_not_held_(_Curr_)_Acquires_lock_(_Curr_) _IRQL_saves_
)
{...}

PFN_WDFSPINLOCKACQUIRE 


```

## -parameters

### -param DriverGlobals: 
### -param _IRQL_saves_: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdfsync.PFN_WDFOBJECTACQUIRELOCK
title: PFN_WDFOBJECTACQUIRELOCK
author: windows-driver-content
description: 
ms.assetid: 1afdecb8-82f9-4c94-a1c5-27a901efc356
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

# PFN_WDFOBJECTACQUIRELOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTACQUIRELOCK PfnWdfobjectacquirelock; 

// Definition

WDFAPI PfnWdfobjectacquirelock 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_not_held_(_Curr_)_Acquires_lock_(_Curr_) WDFOBJECT
)
{...}

PFN_WDFOBJECTACQUIRELOCK 


```

## -parameters

### -param DriverGlobals: 
### -param WDFOBJECT: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
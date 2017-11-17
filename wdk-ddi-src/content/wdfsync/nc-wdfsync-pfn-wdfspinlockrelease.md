---
UID: NC.wdfsync.PFN_WDFSPINLOCKRELEASE
title: PFN_WDFSPINLOCKRELEASE
author: windows-driver-content
description: 
ms.assetid: 91fca296-ae8e-4273-bcb0-1575f5198d67
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

# PFN_WDFSPINLOCKRELEASE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFSPINLOCKRELEASE PfnWdfspinlockrelease; 

// Definition

WDFAPI PfnWdfspinlockrelease 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_held_(_Curr_)_Releases_lock_(_Curr_) _IRQL_restores_
)
{...}

PFN_WDFSPINLOCKRELEASE 


```

## -parameters

### -param DriverGlobals: 
### -param _IRQL_restores_: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
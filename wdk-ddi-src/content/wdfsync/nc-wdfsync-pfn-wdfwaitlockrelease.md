---
UID: NC.wdfsync.PFN_WDFWAITLOCKRELEASE
title: PFN_WDFWAITLOCKRELEASE
author: windows-driver-content
description: 
ms.assetid: e0cddf20-366d-4d7c-b19e-e002b1d1f83a
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

# PFN_WDFWAITLOCKRELEASE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWAITLOCKRELEASE PfnWdfwaitlockrelease; 

// Definition

WDFAPI PfnWdfwaitlockrelease 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_held_(_Curr_)_Releases_lock_(_Curr_) WDFWAITLOCK
)
{...}

PFN_WDFWAITLOCKRELEASE 


```

## -parameters

### -param DriverGlobals: 
### -param WDFWAITLOCK: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
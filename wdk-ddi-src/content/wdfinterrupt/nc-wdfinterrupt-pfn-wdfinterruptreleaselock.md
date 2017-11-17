---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTRELEASELOCK
title: PFN_WDFINTERRUPTRELEASELOCK
author: windows-driver-content
description: 
ms.assetid: 4b4c3af8-394e-455d-b3cc-f458decad18c
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

# PFN_WDFINTERRUPTRELEASELOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTRELEASELOCK PfnWdfinterruptreleaselock; 

// Definition

WDFAPI PfnWdfinterruptreleaselock 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_held_(_Curr_)_Releases_lock_(_Curr_) WDFINTERRUPT
)
{...}

PFN_WDFINTERRUPTRELEASELOCK 


```

## -parameters

### -param DriverGlobals: 
### -param WDFINTERRUPT: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
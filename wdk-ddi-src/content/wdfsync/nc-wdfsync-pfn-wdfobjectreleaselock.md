---
UID: NC.wdfsync.PFN_WDFOBJECTRELEASELOCK
title: PFN_WDFOBJECTRELEASELOCK
author: windows-driver-content
description: 
ms.assetid: f22d1a68-57b9-47d9-bf3c-61a82f3c880d
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

# PFN_WDFOBJECTRELEASELOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTRELEASELOCK PfnWdfobjectreleaselock; 

// Definition

WDFAPI PfnWdfobjectreleaselock 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_held_(_Curr_)_Releases_lock_(_Curr_) WDFOBJECT
)
{...}

PFN_WDFOBJECTRELEASELOCK 


```

## -parameters

### -param DriverGlobals: 
### -param WDFOBJECT: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
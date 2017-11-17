---
UID: NC.wdfsync.PFN_WDFSPINLOCKCREATE
title: PFN_WDFSPINLOCKCREATE
author: windows-driver-content
description: 
ms.assetid: e0c46660-fa0a-479c-a900-cdde760ec4cf
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

# PFN_WDFSPINLOCKCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFSPINLOCKCREATE PfnWdfspinlockcreate; 

// Definition

WDFAPI PfnWdfspinlockcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES SpinLockAttributes
	WDFSPINLOCK *SpinLock
)
{...}

PFN_WDFSPINLOCKCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param SpinLockAttributes: 
### -param *SpinLock: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
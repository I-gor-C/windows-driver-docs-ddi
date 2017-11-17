---
UID: NC.wdfsync.PFN_WDFWAITLOCKCREATE
title: PFN_WDFWAITLOCKCREATE
author: windows-driver-content
description: 
ms.assetid: 2cc6ca68-b146-4c7e-b461-5aaeacd309ba
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

# PFN_WDFWAITLOCKCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWAITLOCKCREATE PfnWdfwaitlockcreate; 

// Definition

WDFAPI PfnWdfwaitlockcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES LockAttributes
	WDFWAITLOCK *Lock
)
{...}

PFN_WDFWAITLOCKCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param LockAttributes: 
### -param *Lock: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
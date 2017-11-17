---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTDISABLE
title: PFN_WDFINTERRUPTDISABLE
author: windows-driver-content
description: 
ms.assetid: f8f6f0ff-bd47-4d62-9a63-6222b6f1e3e9
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

# PFN_WDFINTERRUPTDISABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTDISABLE PfnWdfinterruptdisable; 

// Definition

WDFAPI PfnWdfinterruptdisable 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
)
{...}

PFN_WDFINTERRUPTDISABLE 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
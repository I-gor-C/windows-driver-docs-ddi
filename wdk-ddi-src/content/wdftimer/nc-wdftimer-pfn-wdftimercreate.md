---
UID: NC.wdftimer.PFN_WDFTIMERCREATE
title: PFN_WDFTIMERCREATE
author: windows-driver-content
description: 
ms.assetid: 0b647368-5f5b-4e32-b3bd-dd4c37ab2c49
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdftimer.h
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

# PFN_WDFTIMERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFTIMERCREATE PfnWdftimercreate; 

// Definition

WDFAPI PfnWdftimercreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_TIMER_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFTIMER *Timer
)
{...}

PFN_WDFTIMERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Config: 
### -param Attributes: 
### -param *Timer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
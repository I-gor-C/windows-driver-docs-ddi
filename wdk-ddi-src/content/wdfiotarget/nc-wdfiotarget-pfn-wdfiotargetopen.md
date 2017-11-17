---
UID: NC.wdfiotarget.PFN_WDFIOTARGETOPEN
title: PFN_WDFIOTARGETOPEN
author: windows-driver-content
description: 
ms.assetid: 0e209976-91e7-4b52-9c30-5233aaef673d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETOPEN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETOPEN PfnWdfiotargetopen; 

// Definition

WDFAPI PfnWdfiotargetopen 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	PWDF_IO_TARGET_OPEN_PARAMS OpenParams
)
{...}

PFN_WDFIOTARGETOPEN 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param OpenParams: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
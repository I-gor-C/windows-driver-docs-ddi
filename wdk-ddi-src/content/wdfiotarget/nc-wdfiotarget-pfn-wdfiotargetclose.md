---
UID: NC.wdfiotarget.PFN_WDFIOTARGETCLOSE
title: PFN_WDFIOTARGETCLOSE
author: windows-driver-content
description: 
ms.assetid: 8e7efb4b-e671-4d0d-a407-2dddaba98192
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

# PFN_WDFIOTARGETCLOSE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETCLOSE PfnWdfiotargetclose; 

// Definition

WDFAPI PfnWdfiotargetclose 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
)
{...}

PFN_WDFIOTARGETCLOSE 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.strmini.PHW_TIMER_ROUTINE
title: PHW_TIMER_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 7879bd57-0bf4-4094-a81b-b98ed944640f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: strmini.h
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

# PHW_TIMER_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_TIMER_ROUTINE PhwTimerRoutine; 

// Definition

VOID PhwTimerRoutine 
(
	IN PVOID Context
)
{...}

PHW_TIMER_ROUTINE 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
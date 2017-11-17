---
UID: NC.ntddk.PTIMER_APC_ROUTINE
title: PTIMER_APC_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 3a762e8a-6a2e-4ab3-95c6-cdc5dc377426
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# PTIMER_APC_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTIMER_APC_ROUTINE PtimerApcRoutine; 

// Definition

VOID PtimerApcRoutine 
(
	PVOID TimerContext
	ULONG TimerLowValue
	LONG TimerHighValue
)
{...}

PTIMER_APC_ROUTINE 


```

## -parameters

### -param TimerContext: 
### -param TimerLowValue: 
### -param TimerHighValue: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
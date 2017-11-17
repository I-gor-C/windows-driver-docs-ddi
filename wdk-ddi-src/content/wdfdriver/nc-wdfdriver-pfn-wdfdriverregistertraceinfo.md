---
UID: NC.wdfdriver.PFN_WDFDRIVERREGISTERTRACEINFO
title: PFN_WDFDRIVERREGISTERTRACEINFO
author: windows-driver-content
description: 
ms.assetid: f31ea9e1-725f-45b3-866f-932486ff4b0a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVERREGISTERTRACEINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVERREGISTERTRACEINFO PfnWdfdriverregistertraceinfo; 

// Definition

WDFAPI PfnWdfdriverregistertraceinfo 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PDRIVER_OBJECT DriverObject
	PFN_WDF_TRACE_CALLBACK EvtTraceCallback
	PVOID ControlBlock
)
{...}

PFN_WDFDRIVERREGISTERTRACEINFO 


```

## -parameters

### -param DriverGlobals: 
### -param DriverObject: 
### -param EvtTraceCallback: 
### -param ControlBlock: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
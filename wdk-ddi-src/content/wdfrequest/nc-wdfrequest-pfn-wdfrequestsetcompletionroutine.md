---
UID: NC.wdfrequest.PFN_WDFREQUESTSETCOMPLETIONROUTINE
title: PFN_WDFREQUESTSETCOMPLETIONROUTINE
author: windows-driver-content
description: 
ms.assetid: d90397c6-8039-40c0-966d-32a0491a4b82
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTSETCOMPLETIONROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTSETCOMPLETIONROUTINE PfnWdfrequestsetcompletionroutine; 

// Definition

WDFAPI PfnWdfrequestsetcompletionroutine 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PFN_WDF_REQUEST_COMPLETION_ROUTINE CompletionRoutine
	__drv_aliasesMem WDFCONTEXT
)
{...}

PFN_WDFREQUESTSETCOMPLETIONROUTINE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param CompletionRoutine: 
### -param WDFCONTEXT: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
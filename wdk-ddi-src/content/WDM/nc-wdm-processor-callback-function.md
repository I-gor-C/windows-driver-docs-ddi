---
UID: NC.wdm.PROCESSOR_CALLBACK_FUNCTION
title: PROCESSOR_CALLBACK_FUNCTION
author: windows-driver-content
description: 
ms.assetid: f5eff163-e8ee-49d2-89b7-979a07fc925e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PROCESSOR_CALLBACK_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PROCESSOR_CALLBACK_FUNCTION ProcessorCallbackFunction; 

// Definition

VOID ProcessorCallbackFunction 
(
	PVOID CallbackContext
	PKE_PROCESSOR_CHANGE_NOTIFY_CONTEXT ChangeContext
	PNTSTATUS OperationStatus
)
{...}

PROCESSOR_CALLBACK_FUNCTION PPROCESSOR_CALLBACK_FUNCTION


```

## -parameters

### -param CallbackContext: 
### -param ChangeContext: 
### -param OperationStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdm.CALLBACK_FUNCTION
title: CALLBACK_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 0fb741ef-b2b9-4857-84d5-2e25e51f1500
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

# CALLBACK_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CALLBACK_FUNCTION CallbackFunction; 

// Definition

VOID CallbackFunction 
(
	PVOID CallbackContext
	PVOID Argument1
	PVOID Argument2
)
{...}

CALLBACK_FUNCTION PCALLBACK_FUNCTION


```

## -parameters

### -param CallbackContext: 
### -param Argument1: 
### -param Argument2: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
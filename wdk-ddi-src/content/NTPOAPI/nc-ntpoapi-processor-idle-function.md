---
UID: NC.ntpoapi.PROCESSOR_IDLE_FUNCTION
title: PROCESSOR_IDLE_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 6155f974-b4ce-4f9b-93d8-d67b1fa7229c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntpoapi.h
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

# PROCESSOR_IDLE_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PROCESSOR_IDLE_FUNCTION ProcessorIdleFunction; 

// Definition

VOID ProcessorIdleFunction 
(
	_PROCESSOR_POWER_STATE *PState
)
{...}

PROCESSOR_IDLE_FUNCTION 


```

## -parameters

### -param *PState: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
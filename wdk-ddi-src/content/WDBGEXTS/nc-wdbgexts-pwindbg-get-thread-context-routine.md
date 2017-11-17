---
UID: NC.wdbgexts.PWINDBG_GET_THREAD_CONTEXT_ROUTINE
title: PWINDBG_GET_THREAD_CONTEXT_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 58e9584d-b7c5-4d68-abbc-5442e1c0ddbc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_GET_THREAD_CONTEXT_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_GET_THREAD_CONTEXT_ROUTINE PwindbgGetThreadContextRoutine; 

// Definition

ULONG PwindbgGetThreadContextRoutine 
(
	ULONG Processor
	PCONTEXT lpContext
	ULONG cbSizeOfContext
)
{...}

PWINDBG_GET_THREAD_CONTEXT_ROUTINE 


```

## -parameters

### -param Processor: 
### -param lpContext: 
### -param cbSizeOfContext: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
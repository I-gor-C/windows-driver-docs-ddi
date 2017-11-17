---
UID: NC.dbghelp.LPCALL_BACK_USER_INTERRUPT_ROUTINE
title: LPCALL_BACK_USER_INTERRUPT_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 2a667f73-54b3-4a0c-9bd3-3801241e1c41
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# LPCALL_BACK_USER_INTERRUPT_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPCALL_BACK_USER_INTERRUPT_ROUTINE LpcallBackUserInterruptRoutine; 

// Definition

ULONG LpcallBackUserInterruptRoutine 
(
	 VOID
)
{...}

LPCALL_BACK_USER_INTERRUPT_ROUTINE 


```

## -parameters

### -param VOID: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
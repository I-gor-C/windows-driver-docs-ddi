---
UID: NC.fltkernel.PFLTOPLOCK_WAIT_COMPLETE_ROUTINE
title: PFLTOPLOCK_WAIT_COMPLETE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 3ce1e028-fa7e-46e2-aa13-2244f9d5c32a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fltkernel.h
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

# PFLTOPLOCK_WAIT_COMPLETE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLTOPLOCK_WAIT_COMPLETE_ROUTINE PfltoplockWaitCompleteRoutine; 

// Definition

VOID PfltoplockWaitCompleteRoutine 
(
	PFLT_CALLBACK_DATA CallbackData
	PVOID Context
)
{...}

PFLTOPLOCK_WAIT_COMPLETE_ROUTINE 


```

## -parameters

### -param CallbackData: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
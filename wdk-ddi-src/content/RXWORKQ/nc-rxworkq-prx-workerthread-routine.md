---
UID: NC.rxworkq.PRX_WORKERTHREAD_ROUTINE
title: PRX_WORKERTHREAD_ROUTINE
author: windows-driver-content
description: 
ms.assetid: dfa57be3-5282-4cc4-be6f-3967c7bd5d45
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rxworkq.h
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

# PRX_WORKERTHREAD_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRX_WORKERTHREAD_ROUTINE PrxWorkerthreadRoutine; 

// Definition

VOID PrxWorkerthreadRoutine 
(
	IN PVOID Context
)
{...}

PRX_WORKERTHREAD_ROUTINE 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
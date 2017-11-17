---
UID: NC.parallel.PPARALLEL_DEFERRED_ROUTINE
title: PPARALLEL_DEFERRED_ROUTINE
author: windows-driver-content
description: 
ms.assetid: c9a2c590-ce73-43ae-8fe2-438d3d066ec4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: parallel.h
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

# PPARALLEL_DEFERRED_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPARALLEL_DEFERRED_ROUTINE PparallelDeferredRoutine; 

// Definition

VOID PparallelDeferredRoutine 
(
	PVOID DeferredContext
)
{...}

PPARALLEL_DEFERRED_ROUTINE 


```

## -parameters

### -param DeferredContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
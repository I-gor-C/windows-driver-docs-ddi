---
UID: NC.wdm.WORKER_THREAD_ROUTINE
title: WORKER_THREAD_ROUTINE
author: windows-driver-content
description: 
ms.assetid: b8257171-35c3-47ef-8025-af8a085d8149
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

# WORKER_THREAD_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WORKER_THREAD_ROUTINE WorkerThreadRoutine; 

// Definition

VOID WorkerThreadRoutine 
(
	PVOID Parameter
)
{...}

WORKER_THREAD_ROUTINE PWORKER_THREAD_ROUTINE


```

## -parameters

### -param Parameter: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
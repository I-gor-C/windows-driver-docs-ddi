---
UID: NC.fltkernel.PFLT_CALLBACK_DATA_QUEUE_ACQUIRE
title: PFLT_CALLBACK_DATA_QUEUE_ACQUIRE
author: windows-driver-content
description: 
ms.assetid: e981fe21-d3a5-4db9-96b8-269c8c1ad077
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

# PFLT_CALLBACK_DATA_QUEUE_ACQUIRE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_CALLBACK_DATA_QUEUE_ACQUIRE PfltCallbackDataQueueAcquire; 

// Definition

VOID PfltCallbackDataQueueAcquire 
(
	PFLT_CALLBACK_DATA_QUEUE Cbdq
	PKIRQL Irql
)
{...}

PFLT_CALLBACK_DATA_QUEUE_ACQUIRE 


```

## -parameters

### -param Cbdq: 
### -param Irql: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
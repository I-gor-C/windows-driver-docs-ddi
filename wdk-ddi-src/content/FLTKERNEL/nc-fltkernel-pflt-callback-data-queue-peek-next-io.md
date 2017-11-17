---
UID: NC.fltkernel.PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO
title: PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO
author: windows-driver-content
description: 
ms.assetid: f8ee626e-9759-403a-b044-def7a8e71512
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

# PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO PfltCallbackDataQueuePeekNextIo; 

// Definition

PFLT_CALLBACK_DATA PfltCallbackDataQueuePeekNextIo 
(
	PFLT_CALLBACK_DATA_QUEUE Cbdq
	PFLT_CALLBACK_DATA Cbd
	PVOID PeekContext
)
{...}

PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO 


```

## -parameters

### -param Cbdq: 
### -param Cbd: 
### -param PeekContext: 



## -returns

Returns PFLT_CALLBACK_DATA that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
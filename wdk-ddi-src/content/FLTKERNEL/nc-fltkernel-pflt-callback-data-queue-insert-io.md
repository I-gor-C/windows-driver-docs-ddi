---
UID: NC.fltkernel.PFLT_CALLBACK_DATA_QUEUE_INSERT_IO
title: PFLT_CALLBACK_DATA_QUEUE_INSERT_IO
author: windows-driver-content
description: 
ms.assetid: f7759184-9b1a-4272-abf9-a52713528be9
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

# PFLT_CALLBACK_DATA_QUEUE_INSERT_IO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_CALLBACK_DATA_QUEUE_INSERT_IO PfltCallbackDataQueueInsertIo; 

// Definition

NTSTATUS PfltCallbackDataQueueInsertIo 
(
	PFLT_CALLBACK_DATA_QUEUE Cbdq
	PFLT_CALLBACK_DATA Cbd
	PVOID InsertContext
)
{...}

PFLT_CALLBACK_DATA_QUEUE_INSERT_IO 


```

## -parameters

### -param Cbdq: 
### -param Cbd: 
### -param InsertContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
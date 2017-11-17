---
UID: NC.fltkernel.PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO
title: PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO
author: windows-driver-content
description: 
ms.assetid: c8a7557a-229e-43ee-8106-664472e68cbd
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

# PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO PfltCallbackDataQueueCompleteCanceledIo; 

// Definition

VOID PfltCallbackDataQueueCompleteCanceledIo 
(
	PFLT_CALLBACK_DATA_QUEUE Cbdq
	PFLT_CALLBACK_DATA Cbd
)
{...}

PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO 


```

## -parameters

### -param Cbdq: 
### -param Cbd: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
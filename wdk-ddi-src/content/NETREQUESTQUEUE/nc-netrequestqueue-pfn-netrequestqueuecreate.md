---
UID: NC.netrequestqueue.PFN_NETREQUESTQUEUECREATE
title: PFN_NETREQUESTQUEUECREATE
author: windows-driver-content
description: 
ms.assetid: 1b96fcf9-27ff-43e7-b79e-e177688f1226
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequestqueue.h
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

# PFN_NETREQUESTQUEUECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTQUEUECREATE PfnNetrequestqueuecreate; 

// Definition

WDFAPI PfnNetrequestqueuecreate 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PNET_REQUEST_QUEUE_CONFIG NetRequestQueueConfig
	PWDF_OBJECT_ATTRIBUTES QueueAttributes
	NETREQUESTQUEUE *Queue
)
{...}

PFN_NETREQUESTQUEUECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param NetRequestQueueConfig: 
### -param QueueAttributes: 
### -param *Queue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
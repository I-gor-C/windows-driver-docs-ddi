---
UID: NC.netrxqueue.PFN_NETRXQUEUECREATE
title: PFN_NETRXQUEUECREATE
author: windows-driver-content
description: 
ms.assetid: 3dbb6595-47b8-4475-9f9e-3e25f382ae0c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrxqueue.h
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

# PFN_NETRXQUEUECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUECREATE PfnNetrxqueuecreate; 

// Definition

WDFAPI PfnNetrxqueuecreate 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PNETRXQUEUE_INIT NetRxQueueInit
	PWDF_OBJECT_ATTRIBUTES RxQueueAttributes
	PNET_RXQUEUE_CONFIG Configuration
	NETRXQUEUE *RxQueue
)
{...}

PFN_NETRXQUEUECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param NetRxQueueInit: 
### -param RxQueueAttributes: 
### -param Configuration: 
### -param *RxQueue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
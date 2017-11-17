---
UID: NC.netrxqueue.PFN_NETRXQUEUENOTIFYMORERECEIVEDPACKETSAVAILABLE
title: PFN_NETRXQUEUENOTIFYMORERECEIVEDPACKETSAVAILABLE
author: windows-driver-content
description: 
ms.assetid: 496f442f-6a9a-4a9a-b74d-4b52d86b4544
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

# PFN_NETRXQUEUENOTIFYMORERECEIVEDPACKETSAVAILABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUENOTIFYMORERECEIVEDPACKETSAVAILABLE PfnNetrxqueuenotifymorereceivedpacketsavailable; 

// Definition

WDFAPI PfnNetrxqueuenotifymorereceivedpacketsavailable 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETRXQUEUE RxQueue
)
{...}

PFN_NETRXQUEUENOTIFYMORERECEIVEDPACKETSAVAILABLE 


```

## -parameters

### -param DriverGlobals: 
### -param RxQueue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
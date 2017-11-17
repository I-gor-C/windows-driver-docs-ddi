---
UID: NC.netrxqueue.PFN_NETRXQUEUEGETBUFFERLAYOUTHINT
title: PFN_NETRXQUEUEGETBUFFERLAYOUTHINT
author: windows-driver-content
description: 
ms.assetid: bf3e626a-d1ff-42cc-98a0-120d9656c762
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

# PFN_NETRXQUEUEGETBUFFERLAYOUTHINT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUEGETBUFFERLAYOUTHINT PfnNetrxqueuegetbufferlayouthint; 

// Definition

WDFAPI PfnNetrxqueuegetbufferlayouthint 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETRXQUEUE NetRxQueue
	PNET_RXQUEUE_BUFFER_LAYOUT_HINT BufferLayoutHint
)
{...}

PFN_NETRXQUEUEGETBUFFERLAYOUTHINT 


```

## -parameters

### -param DriverGlobals: 
### -param NetRxQueue: 
### -param BufferLayoutHint: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
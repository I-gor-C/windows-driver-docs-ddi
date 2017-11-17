---
UID: NC.netrxqueue.PFN_NETRXQUEUEGETPACKETCONTEXTTOKEN
title: PFN_NETRXQUEUEGETPACKETCONTEXTTOKEN
author: windows-driver-content
description: 
ms.assetid: c015ba55-dd5d-423f-b1f6-d9764dcb5fe4
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

# PFN_NETRXQUEUEGETPACKETCONTEXTTOKEN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUEGETPACKETCONTEXTTOKEN PfnNetrxqueuegetpacketcontexttoken; 

// Definition

WDFAPI PfnNetrxqueuegetpacketcontexttoken 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETRXQUEUE NetRxQueue
	PCNET_CONTEXT_TYPE_INFO ContextTypeInfo
)
{...}

PFN_NETRXQUEUEGETPACKETCONTEXTTOKEN 


```

## -parameters

### -param DriverGlobals: 
### -param NetRxQueue: 
### -param ContextTypeInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
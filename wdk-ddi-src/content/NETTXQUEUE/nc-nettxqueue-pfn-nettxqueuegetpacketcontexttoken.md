---
UID: NC.nettxqueue.PFN_NETTXQUEUEGETPACKETCONTEXTTOKEN
title: PFN_NETTXQUEUEGETPACKETCONTEXTTOKEN
author: windows-driver-content
description: 
ms.assetid: 904f2bf7-becb-43aa-a895-133a64996304
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: nettxqueue.h
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

# PFN_NETTXQUEUEGETPACKETCONTEXTTOKEN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETTXQUEUEGETPACKETCONTEXTTOKEN PfnNettxqueuegetpacketcontexttoken; 

// Definition

WDFAPI PfnNettxqueuegetpacketcontexttoken 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETTXQUEUE NetTxQueue
	PCNET_CONTEXT_TYPE_INFO ContextTypeInfo
)
{...}

PFN_NETTXQUEUEGETPACKETCONTEXTTOKEN 


```

## -parameters

### -param DriverGlobals: 
### -param NetTxQueue: 
### -param ContextTypeInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.nettxqueue.PFN_NETTXQUEUEGETRINGBUFFER
title: PFN_NETTXQUEUEGETRINGBUFFER
author: windows-driver-content
description: 
ms.assetid: ec01608c-9c5e-43ec-b5bc-d41127e4a032
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

# PFN_NETTXQUEUEGETRINGBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETTXQUEUEGETRINGBUFFER PfnNettxqueuegetringbuffer; 

// Definition

WDFAPI PfnNettxqueuegetringbuffer 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETTXQUEUE NetTxQueue
)
{...}

PFN_NETTXQUEUEGETRINGBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param NetTxQueue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
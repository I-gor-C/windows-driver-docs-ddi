---
UID: NC.nettxqueue.PFN_NETTXQUEUENOTIFYMORECOMPLETEDPACKETSAVAILABLE
title: PFN_NETTXQUEUENOTIFYMORECOMPLETEDPACKETSAVAILABLE
author: windows-driver-content
description: 
ms.assetid: 07e41bca-6f6b-469f-a2e5-a9c222e77a17
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

# PFN_NETTXQUEUENOTIFYMORECOMPLETEDPACKETSAVAILABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETTXQUEUENOTIFYMORECOMPLETEDPACKETSAVAILABLE PfnNettxqueuenotifymorecompletedpacketsavailable; 

// Definition

WDFAPI PfnNettxqueuenotifymorecompletedpacketsavailable 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETTXQUEUE TxQueue
)
{...}

PFN_NETTXQUEUENOTIFYMORECOMPLETEDPACKETSAVAILABLE 


```

## -parameters

### -param DriverGlobals: 
### -param TxQueue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.netrxqueue.PFN_NETRXQUEUEINITSETDMAALLOCATORCONFIG
title: PFN_NETRXQUEUEINITSETDMAALLOCATORCONFIG
author: windows-driver-content
description: 
ms.assetid: edaedc4c-ad5a-4300-afad-8322d200e7db
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

# PFN_NETRXQUEUEINITSETDMAALLOCATORCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUEINITSETDMAALLOCATORCONFIG PfnNetrxqueueinitsetdmaallocatorconfig; 

// Definition

WDFAPI PfnNetrxqueueinitsetdmaallocatorconfig 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PNETRXQUEUE_INIT NetRxQueueInit
	PNET_RXQUEUE_DMA_ALLOCATOR_CONFIG DmaAllocatorConfig
)
{...}

PFN_NETRXQUEUEINITSETDMAALLOCATORCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param NetRxQueueInit: 
### -param DmaAllocatorConfig: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
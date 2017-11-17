---
UID: NC.netrxqueue.PFN_NETRXQUEUEINITADDPACKETCONTEXTATTRIBUTES
title: PFN_NETRXQUEUEINITADDPACKETCONTEXTATTRIBUTES
author: windows-driver-content
description: 
ms.assetid: fd3f5c19-39f3-4b86-9275-ab340146a8a8
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

# PFN_NETRXQUEUEINITADDPACKETCONTEXTATTRIBUTES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUEINITADDPACKETCONTEXTATTRIBUTES PfnNetrxqueueinitaddpacketcontextattributes; 

// Definition

WDFAPI PfnNetrxqueueinitaddpacketcontextattributes 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PNETRXQUEUE_INIT NetRxQueueInit
	PNET_PACKET_CONTEXT_ATTRIBUTES PacketContextAttributes
)
{...}

PFN_NETRXQUEUEINITADDPACKETCONTEXTATTRIBUTES 


```

## -parameters

### -param DriverGlobals: 
### -param NetRxQueueInit: 
### -param PacketContextAttributes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
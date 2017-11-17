---
UID: NC.nettxqueue.PFN_NETTXQUEUEINITADDPACKETCONTEXTATTRIBUTES
title: PFN_NETTXQUEUEINITADDPACKETCONTEXTATTRIBUTES
author: windows-driver-content
description: 
ms.assetid: d122f712-3a56-41ab-b418-56e1055d1a4a
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

# PFN_NETTXQUEUEINITADDPACKETCONTEXTATTRIBUTES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETTXQUEUEINITADDPACKETCONTEXTATTRIBUTES PfnNettxqueueinitaddpacketcontextattributes; 

// Definition

WDFAPI PfnNettxqueueinitaddpacketcontextattributes 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PNETTXQUEUE_INIT NetTxQueueInit
	PNET_PACKET_CONTEXT_ATTRIBUTES PacketContextAttributes
)
{...}

PFN_NETTXQUEUEINITADDPACKETCONTEXTATTRIBUTES 


```

## -parameters

### -param DriverGlobals: 
### -param NetTxQueueInit: 
### -param PacketContextAttributes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
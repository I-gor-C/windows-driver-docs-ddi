---
UID: NC.nettxqueue.EVT_TXQUEUE_CANCEL
title: EVT_TXQUEUE_CANCEL
author: windows-driver-content
description: 
ms.assetid: e736846b-4719-4569-b3f4-d278e73b97ba
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

# EVT_TXQUEUE_CANCEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TXQUEUE_CANCEL EvtTxqueueCancel; 

// Definition

VOID EvtTxqueueCancel 
(
	NETTXQUEUE TxQueue
)
{...}

EVT_TXQUEUE_CANCEL PFN_TXQUEUE_CANCEL


```

## -parameters

### -param TxQueue: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
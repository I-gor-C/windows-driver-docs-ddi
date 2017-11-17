---
UID: NC.nettxqueue.EVT_TXQUEUE_ADVANCE
title: EVT_TXQUEUE_ADVANCE
author: windows-driver-content
description: 
ms.assetid: 79c1af4b-fc75-42e9-871d-6c0ef0052db6
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

# EVT_TXQUEUE_ADVANCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TXQUEUE_ADVANCE EvtTxqueueAdvance; 

// Definition

VOID EvtTxqueueAdvance 
(
	NETTXQUEUE TxQueue
)
{...}

EVT_TXQUEUE_ADVANCE PFN_TXQUEUE_ADVANCE


```

## -parameters

### -param TxQueue: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
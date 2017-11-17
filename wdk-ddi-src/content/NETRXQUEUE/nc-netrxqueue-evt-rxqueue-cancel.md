---
UID: NC.netrxqueue.EVT_RXQUEUE_CANCEL
title: EVT_RXQUEUE_CANCEL
author: windows-driver-content
description: 
ms.assetid: a41d567b-41dc-41ac-9814-97e451e37bd7
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

# EVT_RXQUEUE_CANCEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_RXQUEUE_CANCEL EvtRxqueueCancel; 

// Definition

VOID EvtRxqueueCancel 
(
	NETRXQUEUE RxQueue
)
{...}

EVT_RXQUEUE_CANCEL PFN_RXQUEUE_CANCEL


```

## -parameters

### -param RxQueue: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
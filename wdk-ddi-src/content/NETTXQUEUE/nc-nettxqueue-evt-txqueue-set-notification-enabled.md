---
UID: NC.nettxqueue.EVT_TXQUEUE_SET_NOTIFICATION_ENABLED
title: EVT_TXQUEUE_SET_NOTIFICATION_ENABLED
author: windows-driver-content
description: 
ms.assetid: f7a4b6d9-7a20-4b4c-8bd0-c9377ba9aea8
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

# EVT_TXQUEUE_SET_NOTIFICATION_ENABLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TXQUEUE_SET_NOTIFICATION_ENABLED EvtTxqueueSetNotificationEnabled; 

// Definition

VOID EvtTxqueueSetNotificationEnabled 
(
	NETTXQUEUE TxQueue
	BOOLEAN NotificationEnabled
)
{...}

EVT_TXQUEUE_SET_NOTIFICATION_ENABLED PFN_TXQUEUE_SET_NOTIFICATION_ENABLED


```

## -parameters

### -param TxQueue: 
### -param NotificationEnabled: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
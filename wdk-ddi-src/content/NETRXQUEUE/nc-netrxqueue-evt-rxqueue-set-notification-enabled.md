---
UID: NC.netrxqueue.EVT_RXQUEUE_SET_NOTIFICATION_ENABLED
title: EVT_RXQUEUE_SET_NOTIFICATION_ENABLED
author: windows-driver-content
description: 
ms.assetid: a8b1b515-86f8-468d-9f2f-9647792ba981
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

# EVT_RXQUEUE_SET_NOTIFICATION_ENABLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_RXQUEUE_SET_NOTIFICATION_ENABLED EvtRxqueueSetNotificationEnabled; 

// Definition

VOID EvtRxqueueSetNotificationEnabled 
(
	NETRXQUEUE RxQueue
	BOOLEAN NotificationEnabled
)
{...}

EVT_RXQUEUE_SET_NOTIFICATION_ENABLED PFN_RXQUEUE_SET_NOTIFICATION_ENABLED


```

## -parameters

### -param RxQueue: 
### -param NotificationEnabled: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.NDIS_PD_REQUEST_DRAIN_NOTIFICATION
title: NDIS_PD_REQUEST_DRAIN_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 0c33dfcb-266c-4223-ab0c-c9a6ebe6ac9c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# NDIS_PD_REQUEST_DRAIN_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_PD_REQUEST_DRAIN_NOTIFICATION NdisPdRequestDrainNotification; 

// Definition

VOID() NdisPdRequestDrainNotification 
(
	NDIS_PD_QUEUE * NdisPDQueue
)
{...}

NDIS_PD_REQUEST_DRAIN_NOTIFICATION NDIS_PD_REQUEST_DRAIN_NOTIFICATION_HANDLER


```

## -parameters

### -param NdisPDQueue: 



## -returns

Returns VOID() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
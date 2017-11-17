---
UID: NC.ndis.NDIS_PD_ACQUIRE_RECEIVE_QUEUES
title: NDIS_PD_ACQUIRE_RECEIVE_QUEUES
author: windows-driver-content
description: 
ms.assetid: 38b4badb-74fe-4631-8d91-e4d5ef919e8f
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

# NDIS_PD_ACQUIRE_RECEIVE_QUEUES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_PD_ACQUIRE_RECEIVE_QUEUES NdisPdAcquireReceiveQueues; 

// Definition

NTSTATUS() NdisPdAcquireReceiveQueues 
(
	NDIS_PD_PROVIDER_HANDLE ProviderHandle
	CONST NDIS_PD_ACQUIRE_QUEUES_PARAMETERS * Parameters
	NDIS_PD_QUEUE ** NdisPDQueueArray
	ULONG * QueueCount
	NDIS_PD_QUEUE_PARAMETERS * QueueParametersArray
	ULONG * QueueParametersArraySize
	ULONG * QueueParametersArrayElementSize
)
{...}

NDIS_PD_ACQUIRE_RECEIVE_QUEUES NDIS_PD_ACQUIRE_RECEIVE_QUEUES_HANDLER


```

## -parameters

### -param ProviderHandle: 
### -param Parameters: 
### -param NdisPDQueueArray: 
### -param QueueCount: 
### -param QueueParametersArray: 
### -param QueueParametersArraySize: 
### -param QueueParametersArrayElementSize: 



## -returns

Returns NTSTATUS() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
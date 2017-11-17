---
UID: NC.ndis.NDIS_PD_RELEASE_RECEIVE_QUEUES
title: NDIS_PD_RELEASE_RECEIVE_QUEUES
author: windows-driver-content
description: 
ms.assetid: 7fa4fea4-5bae-4264-acbb-157234784a23
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

# NDIS_PD_RELEASE_RECEIVE_QUEUES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_PD_RELEASE_RECEIVE_QUEUES NdisPdReleaseReceiveQueues; 

// Definition

VOID() NdisPdReleaseReceiveQueues 
(
	NDIS_PD_PROVIDER_HANDLE ProviderHandle
)
{...}

NDIS_PD_RELEASE_RECEIVE_QUEUES NDIS_PD_RELEASE_RECEIVE_QUEUES_HANDLER


```

## -parameters

### -param ProviderHandle: 



## -returns

Returns VOID() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
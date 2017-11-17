---
UID: NC.ndischimney.NDIS_TCP_OFFLOAD_RECEIVE_INDICATE
title: NDIS_TCP_OFFLOAD_RECEIVE_INDICATE
author: windows-driver-content
description: 
ms.assetid: 75d602e9-9473-4cb0-a6a6-3a5940d4ed33
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndischimney.h
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

# NDIS_TCP_OFFLOAD_RECEIVE_INDICATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_TCP_OFFLOAD_RECEIVE_INDICATE NdisTcpOffloadReceiveIndicate; 

// Definition

NDIS_STATUS NdisTcpOffloadReceiveIndicate 
(
	IN NDIS_HANDLE NdisOffloadHandle
	IN PNET_BUFFER_LIST NetBufferList
	IN NDIS_STATUS Status
	OUT PULONG BytesConsumed
)
{...}

NDIS_TCP_OFFLOAD_RECEIVE_INDICATE 


```

## -parameters

### -param NdisOffloadHandle: 
### -param NetBufferList: 
### -param Status: 
### -param BytesConsumed: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
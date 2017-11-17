---
UID: NC.ndischimney.NDIS_TCP_OFFLOAD_SEND_COMPLETE
title: NDIS_TCP_OFFLOAD_SEND_COMPLETE
author: windows-driver-content
description: 
ms.assetid: 5d85b9f4-73b6-4f9a-8d10-c50f3be0265e
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

# NDIS_TCP_OFFLOAD_SEND_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_TCP_OFFLOAD_SEND_COMPLETE NdisTcpOffloadSendComplete; 

// Definition

VOID NdisTcpOffloadSendComplete 
(
	IN NDIS_HANDLE NdisMiniportHandle
	IN PNET_BUFFER_LIST NetBufferList
)
{...}

NDIS_TCP_OFFLOAD_SEND_COMPLETE 


```

## -parameters

### -param NdisMiniportHandle: 
### -param NetBufferList: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
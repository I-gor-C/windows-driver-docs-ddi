---
UID: NC.ndischimney.NDIS_TCP_OFFLOAD_FORWARD_COMPLETE
title: NDIS_TCP_OFFLOAD_FORWARD_COMPLETE
author: windows-driver-content
description: 
ms.assetid: b6fbc9e3-c681-4b23-bca0-27b9701d6a6f
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

# NDIS_TCP_OFFLOAD_FORWARD_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_TCP_OFFLOAD_FORWARD_COMPLETE NdisTcpOffloadForwardComplete; 

// Definition

VOID NdisTcpOffloadForwardComplete 
(
	IN NDIS_HANDLE NdisMiniportHandle
	IN PNET_BUFFER_LIST NetBufferList
)
{...}

NDIS_TCP_OFFLOAD_FORWARD_COMPLETE 


```

## -parameters

### -param NdisMiniportHandle: 
### -param NetBufferList: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
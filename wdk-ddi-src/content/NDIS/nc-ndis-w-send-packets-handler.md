---
UID: NC.ndis.W_SEND_PACKETS_HANDLER
title: W_SEND_PACKETS_HANDLER
author: windows-driver-content
description: 
ms.assetid: 7412c150-423f-412b-9a51-debd4c5eda99
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

# W_SEND_PACKETS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_SEND_PACKETS_HANDLER WSendPacketsHandler; 

// Definition

VOID WSendPacketsHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	PPNDIS_PACKET PacketArray
	UINT NumberOfPackets
)
{...}

W_SEND_PACKETS_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param PacketArray: 
### -param NumberOfPackets: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
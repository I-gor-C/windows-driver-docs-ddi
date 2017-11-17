---
UID: NC.ndis.W_RETURN_PACKET_HANDLER
title: W_RETURN_PACKET_HANDLER
author: windows-driver-content
description: 
ms.assetid: 1ca3aa75-4f17-4553-a419-9713622be792
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

# W_RETURN_PACKET_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_RETURN_PACKET_HANDLER WReturnPacketHandler; 

// Definition

VOID WReturnPacketHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	PNDIS_PACKET Packet
)
{...}

W_RETURN_PACKET_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param Packet: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
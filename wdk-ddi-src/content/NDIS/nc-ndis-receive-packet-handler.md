---
UID: NC.ndis.RECEIVE_PACKET_HANDLER
title: RECEIVE_PACKET_HANDLER
author: windows-driver-content
description: 
ms.assetid: eb41151c-269e-4c87-830b-9b39944b11ad
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

# RECEIVE_PACKET_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RECEIVE_PACKET_HANDLER ReceivePacketHandler; 

// Definition

INT ReceivePacketHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	PNDIS_PACKET Packet
)
{...}

RECEIVE_PACKET_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param Packet: 



## -returns

Returns INT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
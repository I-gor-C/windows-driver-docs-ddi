---
UID: NC.ndis.CO_RECEIVE_PACKET_HANDLER
title: CO_RECEIVE_PACKET_HANDLER
author: windows-driver-content
description: 
ms.assetid: bb4421be-179c-4945-8806-d9ea5fd51b79
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

# CO_RECEIVE_PACKET_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CO_RECEIVE_PACKET_HANDLER CoReceivePacketHandler; 

// Definition

UINT CoReceivePacketHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	NDIS_HANDLE ProtocolVcContext
	PNDIS_PACKET Packet
)
{...}

CO_RECEIVE_PACKET_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param ProtocolVcContext: 
### -param Packet: 



## -returns

Returns UINT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
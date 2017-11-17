---
UID: NC.ndis.WAN_RECEIVE_HANDLER
title: WAN_RECEIVE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 6270f744-9dd9-486c-b940-fa9631d58e04
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

# WAN_RECEIVE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WAN_RECEIVE_HANDLER WanReceiveHandler; 

// Definition

NDIS_STATUS WanReceiveHandler 
(
	NDIS_HANDLE NdisLinkHandle
	PUCHAR Packet
	ULONG PacketSize
)
{...}

WAN_RECEIVE_HANDLER 


```

## -parameters

### -param NdisLinkHandle: 
### -param Packet: 
### -param PacketSize: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.WAN_RCV_HANDLER
title: WAN_RCV_HANDLER
author: windows-driver-content
description: 
ms.assetid: 22510fcf-9547-42a9-ae87-afda94e74021
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

# WAN_RCV_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WAN_RCV_HANDLER WanRcvHandler; 

// Definition

VOID WanRcvHandler 
(
	PNDIS_STATUS Status
	NDIS_HANDLE MiniportAdapterHandle
	NDIS_HANDLE NdisLinkContext
	PUCHAR Packet
	ULONG PacketSize
)
{...}

WAN_RCV_HANDLER 


```

## -parameters

### -param Status: 
### -param MiniportAdapterHandle: 
### -param NdisLinkContext: 
### -param Packet: 
### -param PacketSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.FILTER_PACKET_INDICATION_HANDLER
title: FILTER_PACKET_INDICATION_HANDLER
author: windows-driver-content
description: 
ms.assetid: fed16a3f-f4fb-47bb-a0f7-b63d34fee098
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

# FILTER_PACKET_INDICATION_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FILTER_PACKET_INDICATION_HANDLER FilterPacketIndicationHandler; 

// Definition

VOID FilterPacketIndicationHandler 
(
	NDIS_HANDLE Miniport
	PPNDIS_PACKET PacketArray
	UINT NumberOfPackets
)
{...}

FILTER_PACKET_INDICATION_HANDLER 


```

## -parameters

### -param Miniport: 
### -param PacketArray: 
### -param NumberOfPackets: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
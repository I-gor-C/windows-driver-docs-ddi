---
UID: NC.ndis.W_CO_SEND_PACKETS_HANDLER
title: W_CO_SEND_PACKETS_HANDLER
author: windows-driver-content
description: 
ms.assetid: 8dbd642c-cb47-48d9-97d1-17e40f9cd235
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

# W_CO_SEND_PACKETS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_CO_SEND_PACKETS_HANDLER WCoSendPacketsHandler; 

// Definition

VOID WCoSendPacketsHandler 
(
	NDIS_HANDLE MiniportVcContext
	PPNDIS_PACKET PacketArray
	UINT NumberOfPackets
)
{...}

W_CO_SEND_PACKETS_HANDLER 


```

## -parameters

### -param MiniportVcContext: 
### -param PacketArray: 
### -param NumberOfPackets: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
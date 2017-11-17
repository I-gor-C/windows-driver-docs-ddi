---
UID: NC.ndis.CO_SEND_COMPLETE_HANDLER
title: CO_SEND_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: b0d1e111-bccf-4a37-916a-98673951af7a
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

# CO_SEND_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CO_SEND_COMPLETE_HANDLER CoSendCompleteHandler; 

// Definition

VOID CoSendCompleteHandler 
(
	NDIS_STATUS Status
	NDIS_HANDLE ProtocolVcContext
	PNDIS_PACKET Packet
)
{...}

CO_SEND_COMPLETE_HANDLER 


```

## -parameters

### -param Status: 
### -param ProtocolVcContext: 
### -param Packet: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
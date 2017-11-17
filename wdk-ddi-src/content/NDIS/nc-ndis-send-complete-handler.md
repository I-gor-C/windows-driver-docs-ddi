---
UID: NC.ndis.SEND_COMPLETE_HANDLER
title: SEND_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: cacba29f-4d60-4430-a33e-c3cb5dac065e
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

# SEND_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SEND_COMPLETE_HANDLER SendCompleteHandler; 

// Definition

VOID SendCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	PNDIS_PACKET Packet
	NDIS_STATUS Status
)
{...}

SEND_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param Packet: 
### -param Status: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
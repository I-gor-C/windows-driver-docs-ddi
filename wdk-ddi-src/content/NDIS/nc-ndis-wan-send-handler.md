---
UID: NC.ndis.WAN_SEND_HANDLER
title: WAN_SEND_HANDLER
author: windows-driver-content
description: 
ms.assetid: 3b0a1fbd-c2c8-42dd-85b4-93fc2eb714fb
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

# WAN_SEND_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WAN_SEND_HANDLER WanSendHandler; 

// Definition

NDIS_STATUS WanSendHandler 
(
	NDIS_HANDLE NdisBindingHandle
	NDIS_HANDLE LinkHandle
	PVOID Packet
)
{...}

WAN_SEND_HANDLER 


```

## -parameters

### -param NdisBindingHandle: 
### -param LinkHandle: 
### -param Packet: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
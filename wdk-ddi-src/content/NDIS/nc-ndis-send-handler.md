---
UID: NC.ndis.SEND_HANDLER
title: SEND_HANDLER
author: windows-driver-content
description: 
ms.assetid: 21adec7c-b6f7-48ac-a2cd-d5448e1c3910
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

# SEND_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SEND_HANDLER SendHandler; 

// Definition

NDIS_STATUS SendHandler 
(
	NDIS_HANDLE NdisBindingHandle
	PNDIS_PACKET Packet
)
{...}

SEND_HANDLER 


```

## -parameters

### -param NdisBindingHandle: 
### -param Packet: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
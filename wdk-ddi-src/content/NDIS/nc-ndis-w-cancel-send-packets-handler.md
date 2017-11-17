---
UID: NC.ndis.W_CANCEL_SEND_PACKETS_HANDLER
title: W_CANCEL_SEND_PACKETS_HANDLER
author: windows-driver-content
description: 
ms.assetid: 6943abed-c0db-486e-a34d-6b4160f75606
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

# W_CANCEL_SEND_PACKETS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_CANCEL_SEND_PACKETS_HANDLER WCancelSendPacketsHandler; 

// Definition

VOID WCancelSendPacketsHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	PVOID CancelId
)
{...}

W_CANCEL_SEND_PACKETS_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param CancelId: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
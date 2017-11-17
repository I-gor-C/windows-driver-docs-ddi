---
UID: NC.ndis.CO_REQUEST_HANDLER
title: CO_REQUEST_HANDLER
author: windows-driver-content
description: 
ms.assetid: d4ca8ba5-a87a-4fc8-a9c7-6f8444983785
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

# CO_REQUEST_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CO_REQUEST_HANDLER CoRequestHandler; 

// Definition

NDIS_STATUS CoRequestHandler 
(
	NDIS_HANDLE ProtocolAfContext
	NDIS_HANDLE ProtocolVcContext
	NDIS_HANDLE ProtocolPartyContext
	PNDIS_REQUEST NdisRequest
)
{...}

CO_REQUEST_HANDLER 


```

## -parameters

### -param ProtocolAfContext: 
### -param ProtocolVcContext: 
### -param ProtocolPartyContext: 
### -param NdisRequest: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
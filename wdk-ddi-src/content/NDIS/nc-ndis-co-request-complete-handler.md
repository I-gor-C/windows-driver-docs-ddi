---
UID: NC.ndis.CO_REQUEST_COMPLETE_HANDLER
title: CO_REQUEST_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 10edd2ca-3a91-4cc9-9ab7-6d54088e27df
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

# CO_REQUEST_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CO_REQUEST_COMPLETE_HANDLER CoRequestCompleteHandler; 

// Definition

VOID CoRequestCompleteHandler 
(
	NDIS_STATUS Status
	NDIS_HANDLE ProtocolAfContext
	NDIS_HANDLE ProtocolVcContext
	NDIS_HANDLE ProtocolPartyContext
	PNDIS_REQUEST NdisRequest
)
{...}

CO_REQUEST_COMPLETE_HANDLER 


```

## -parameters

### -param Status: 
### -param ProtocolAfContext: 
### -param ProtocolVcContext: 
### -param ProtocolPartyContext: 
### -param NdisRequest: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.REQUEST_COMPLETE_HANDLER
title: REQUEST_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: f08c0524-1241-4f7c-80f3-8511a2d7829e
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

# REQUEST_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

REQUEST_COMPLETE_HANDLER RequestCompleteHandler; 

// Definition

VOID RequestCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	PNDIS_REQUEST NdisRequest
	NDIS_STATUS Status
)
{...}

REQUEST_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param NdisRequest: 
### -param Status: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
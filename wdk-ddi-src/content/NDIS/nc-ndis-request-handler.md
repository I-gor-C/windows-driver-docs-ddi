---
UID: NC.ndis.REQUEST_HANDLER
title: REQUEST_HANDLER
author: windows-driver-content
description: 
ms.assetid: ab58a204-d928-46dc-b842-70b7ac165f6d
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

# REQUEST_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

REQUEST_HANDLER RequestHandler; 

// Definition

NDIS_STATUS RequestHandler 
(
	NDIS_HANDLE NdisBindingHandle
	PNDIS_REQUEST NdisRequest
)
{...}

REQUEST_HANDLER 


```

## -parameters

### -param NdisBindingHandle: 
### -param NdisRequest: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.W_CO_REQUEST_HANDLER
title: W_CO_REQUEST_HANDLER
author: windows-driver-content
description: 
ms.assetid: 4ac9ee1d-dc43-4ba4-aed1-f12f522ef1e1
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

# W_CO_REQUEST_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_CO_REQUEST_HANDLER WCoRequestHandler; 

// Definition

NDIS_STATUS WCoRequestHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	NDIS_HANDLE MiniportVcContext OPTIONAL
	PNDIS_REQUEST NdisRequest
)
{...}

W_CO_REQUEST_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param OPTIONAL: 
### -param NdisRequest: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
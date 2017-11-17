---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_ABORT
title: EVT_UCX_ENDPOINT_ABORT
author: windows-driver-content
description: 
ms.assetid: 78e28cb6-6d90-417c-b6be-46101c43ea93
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxendpoint.h
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

# EVT_UCX_ENDPOINT_ABORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ENDPOINT_ABORT EvtUcxEndpointAbort; 

// Definition

VOID EvtUcxEndpointAbort 
(
	UCXCONTROLLER UcxController
	UCXENDPOINT UcxEndpoint
)
{...}

EVT_UCX_ENDPOINT_ABORT PFN_UCX_ENDPOINT_ABORT


```

## -parameters

### -param UcxController: 
### -param UcxEndpoint: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
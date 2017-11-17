---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_START
title: EVT_UCX_ENDPOINT_START
author: windows-driver-content
description: 
ms.assetid: b8b7f4d0-05a7-48df-bc1d-65e3ab9efb76
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

# EVT_UCX_ENDPOINT_START callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ENDPOINT_START EvtUcxEndpointStart; 

// Definition

VOID EvtUcxEndpointStart 
(
	UCXCONTROLLER UcxController
	UCXENDPOINT UcxEndpoint
)
{...}

EVT_UCX_ENDPOINT_START PFN_UCX_ENDPOINT_START


```

## -parameters

### -param UcxController: 
### -param UcxEndpoint: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
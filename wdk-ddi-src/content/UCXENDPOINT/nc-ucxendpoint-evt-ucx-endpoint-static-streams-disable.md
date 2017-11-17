---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE
title: EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE
author: windows-driver-content
description: 
ms.assetid: 48c3c42e-bc0f-4beb-920b-32da16c99112
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

# EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE EvtUcxEndpointStaticStreamsDisable; 

// Definition

VOID EvtUcxEndpointStaticStreamsDisable 
(
	UCXENDPOINT UcxEndpoint
	UCXSSTREAMS UcxStaticStreams
	WDFREQUEST Request
)
{...}

EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE PFN_UCX_ENDPOINT_STATIC_STREAMS_DISABLE


```

## -parameters

### -param UcxEndpoint: 
### -param UcxStaticStreams: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
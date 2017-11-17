---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD
title: EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD
author: windows-driver-content
description: 
ms.assetid: 43109378-bca8-4f1e-853f-e20dfb83292c
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

# EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD EvtUcxEndpointStaticStreamsAdd; 

// Definition

NTSTATUS EvtUcxEndpointStaticStreamsAdd 
(
	UCXENDPOINT UcxEndpoint
	ULONG NumberOfStreams
	PUCXSSTREAMS_INIT UcxStaticStreamsInit
)
{...}

EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD PFN_UCX_ENDPOINT_STATIC_STREAMS_ADD


```

## -parameters

### -param UcxEndpoint: 
### -param NumberOfStreams: 
### -param UcxStaticStreamsInit: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
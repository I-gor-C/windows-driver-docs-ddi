---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_PURGE
title: EVT_UCX_ENDPOINT_PURGE
author: windows-driver-content
description: 
ms.assetid: e6cca799-8483-4e77-8aea-47659be78252
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

# EVT_UCX_ENDPOINT_PURGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ENDPOINT_PURGE EvtUcxEndpointPurge; 

// Definition

VOID EvtUcxEndpointPurge 
(
	UCXCONTROLLER UcxController
	UCXENDPOINT UcxEndpoint
)
{...}

EVT_UCX_ENDPOINT_PURGE PFN_UCX_ENDPOINT_PURGE


```

## -parameters

### -param UcxController: 
### -param UcxEndpoint: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
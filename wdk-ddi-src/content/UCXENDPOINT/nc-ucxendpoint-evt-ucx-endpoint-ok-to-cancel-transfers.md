---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
title: EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
author: windows-driver-content
description: 
ms.assetid: cd5f79f4-4d61-4556-b10a-116d8b76ddbb
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

# EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS EvtUcxEndpointOkToCancelTransfers; 

// Definition

VOID EvtUcxEndpointOkToCancelTransfers 
(
	UCXENDPOINT UcxEndpoint
)
{...}

EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS PFN_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS


```

## -parameters

### -param UcxEndpoint: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
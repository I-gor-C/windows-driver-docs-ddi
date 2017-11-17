---
UID: NC.ucxendpoint.EVT_UCX_DEFAULT_ENDPOINT_UPDATE
title: EVT_UCX_DEFAULT_ENDPOINT_UPDATE
author: windows-driver-content
description: 
ms.assetid: 64cb67ed-7fe5-42cf-846f-fe58856b5cce
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

# EVT_UCX_DEFAULT_ENDPOINT_UPDATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_DEFAULT_ENDPOINT_UPDATE EvtUcxDefaultEndpointUpdate; 

// Definition

VOID EvtUcxDefaultEndpointUpdate 
(
	UCXCONTROLLER UcxController
	WDFREQUEST Request
)
{...}

EVT_UCX_DEFAULT_ENDPOINT_UPDATE PFN_UCX_DEFAULT_ENDPOINT_UPDATE


```

## -parameters

### -param UcxController: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
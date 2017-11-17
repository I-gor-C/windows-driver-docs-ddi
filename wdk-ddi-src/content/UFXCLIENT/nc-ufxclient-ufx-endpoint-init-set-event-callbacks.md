---
UID: NC.ufxclient.UFX_ENDPOINT_INIT_SET_EVENT_CALLBACKS
title: UFX_ENDPOINT_INIT_SET_EVENT_CALLBACKS
author: windows-driver-content
description: 
ms.assetid: 3a255048-dc2f-4c45-88a9-f82f9fafc2ec
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxclient.h
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

# UFX_ENDPOINT_INIT_SET_EVENT_CALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_ENDPOINT_INIT_SET_EVENT_CALLBACKS UfxEndpointInitSetEventCallbacks; 

// Definition

VOID UfxEndpointInitSetEventCallbacks 
(
	PUFX_GLOBALS 
	PUFXENDPOINT_INIT EndpointInit
	PUFX_ENDPOINT_CALLBACKS Callbacks
)
{...}

UFX_ENDPOINT_INIT_SET_EVENT_CALLBACKS PFN_UFX_ENDPOINT_INIT_SET_CALLBACKS


```

## -parameters

### -param : 
### -param EndpointInit: 
### -param Callbacks: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
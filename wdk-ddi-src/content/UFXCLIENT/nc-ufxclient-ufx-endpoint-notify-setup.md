---
UID: NC.ufxclient.UFX_ENDPOINT_NOTIFY_SETUP
title: UFX_ENDPOINT_NOTIFY_SETUP
author: windows-driver-content
description: 
ms.assetid: 69033d94-d431-442a-b19a-0772d707427d
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

# UFX_ENDPOINT_NOTIFY_SETUP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_ENDPOINT_NOTIFY_SETUP UfxEndpointNotifySetup; 

// Definition

VOID UfxEndpointNotifySetup 
(
	PUFX_GLOBALS 
	UFXENDPOINT UfxEndpoint
	PUSB_DEFAULT_PIPE_SETUP_PACKET SetupInfo
)
{...}

UFX_ENDPOINT_NOTIFY_SETUP PFN_UFX_ENDPOINT_NOTIFY_SETUP


```

## -parameters

### -param : 
### -param UfxEndpoint: 
### -param SetupInfo: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.W_MINIPORT_SHUTDOWN_HANDLER
title: W_MINIPORT_SHUTDOWN_HANDLER
author: windows-driver-content
description: 
ms.assetid: d03434be-1913-4a5d-8fb7-0588e02c3c8e
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

# W_MINIPORT_SHUTDOWN_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_MINIPORT_SHUTDOWN_HANDLER WMiniportShutdownHandler; 

// Definition

VOID WMiniportShutdownHandler 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_MINIPORT_SHUTDOWN_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
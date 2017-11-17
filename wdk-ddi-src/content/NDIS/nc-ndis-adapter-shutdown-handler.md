---
UID: NC.ndis.ADAPTER_SHUTDOWN_HANDLER
title: ADAPTER_SHUTDOWN_HANDLER
author: windows-driver-content
description: 
ms.assetid: 99c1451d-9d40-4934-9d79-5c2ffa23512a
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

# ADAPTER_SHUTDOWN_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ADAPTER_SHUTDOWN_HANDLER AdapterShutdownHandler; 

// Definition

VOID AdapterShutdownHandler 
(
	PVOID ShutdownContext
)
{...}

ADAPTER_SHUTDOWN_HANDLER 


```

## -parameters

### -param ShutdownContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
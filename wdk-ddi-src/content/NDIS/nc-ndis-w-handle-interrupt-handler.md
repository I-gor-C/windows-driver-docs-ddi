---
UID: NC.ndis.W_HANDLE_INTERRUPT_HANDLER
title: W_HANDLE_INTERRUPT_HANDLER
author: windows-driver-content
description: 
ms.assetid: e2f11c7e-2366-4e74-a065-dacdc8e1d45c
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

# W_HANDLE_INTERRUPT_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_HANDLE_INTERRUPT_HANDLER WHandleInterruptHandler; 

// Definition

VOID WHandleInterruptHandler 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_HANDLE_INTERRUPT_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
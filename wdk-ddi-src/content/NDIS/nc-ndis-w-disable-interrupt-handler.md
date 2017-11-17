---
UID: NC.ndis.W_DISABLE_INTERRUPT_HANDLER
title: W_DISABLE_INTERRUPT_HANDLER
author: windows-driver-content
description: 
ms.assetid: 376b337b-1d16-40de-b8b5-7b3fe3398512
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

# W_DISABLE_INTERRUPT_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_DISABLE_INTERRUPT_HANDLER WDisableInterruptHandler; 

// Definition

VOID WDisableInterruptHandler 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_DISABLE_INTERRUPT_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.W_ENABLE_INTERRUPT_HANDLER
title: W_ENABLE_INTERRUPT_HANDLER
author: windows-driver-content
description: 
ms.assetid: bea0904f-ebcc-4bf0-b86b-1f7f3ba7bbb6
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

# W_ENABLE_INTERRUPT_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_ENABLE_INTERRUPT_HANDLER WEnableInterruptHandler; 

// Definition

VOID WEnableInterruptHandler 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_ENABLE_INTERRUPT_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
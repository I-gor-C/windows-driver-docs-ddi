---
UID: NC.ndis.W_ISR_HANDLER
title: W_ISR_HANDLER
author: windows-driver-content
description: 
ms.assetid: f0880063-3c0b-4a47-8d63-d3d54f1773f3
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

# W_ISR_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_ISR_HANDLER WIsrHandler; 

// Definition

VOID WIsrHandler 
(
	PBOOLEAN InterruptRecognized
	PBOOLEAN QueueMiniportHandleInterrupt
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_ISR_HANDLER 


```

## -parameters

### -param InterruptRecognized: 
### -param QueueMiniportHandleInterrupt: 
### -param MiniportAdapterContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.tdikrnl.TDI_NET_READY_HANDLER
title: TDI_NET_READY_HANDLER
author: windows-driver-content
description: 
ms.assetid: 3efa7cf6-54d6-4e93-b0ea-3503162bc577
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tdikrnl.h
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

# TDI_NET_READY_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_NET_READY_HANDLER TdiNetReadyHandler; 

// Definition

VOID TdiNetReadyHandler 
(
	NTSTATUS ProviderStatus
)
{...}

TDI_NET_READY_HANDLER 


```

## -parameters

### -param ProviderStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
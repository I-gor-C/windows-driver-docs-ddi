---
UID: NC.netioddk.NPI_CLIENT_CLEANUP_BINDING_CONTEXT_FN
title: NPI_CLIENT_CLEANUP_BINDING_CONTEXT_FN
author: windows-driver-content
description: 
ms.assetid: ca428123-de6a-4a5e-96e9-0715788e238c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netioddk.h
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

# NPI_CLIENT_CLEANUP_BINDING_CONTEXT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NPI_CLIENT_CLEANUP_BINDING_CONTEXT_FN NpiClientCleanupBindingContextFn; 

// Definition

VOID NpiClientCleanupBindingContextFn 
(
	PVOID ClientBindingContext
)
{...}

NPI_CLIENT_CLEANUP_BINDING_CONTEXT_FN 


```

## -parameters

### -param ClientBindingContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.netioddk.NPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN
title: NPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN
author: windows-driver-content
description: 
ms.assetid: 509b6cb6-8113-42b5-a942-6b51acf1b59d
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

# NPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN NpiProviderCleanupBindingContextFn; 

// Definition

VOID NpiProviderCleanupBindingContextFn 
(
	PVOID ProviderBindingContext
)
{...}

NPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN 


```

## -parameters

### -param ProviderBindingContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
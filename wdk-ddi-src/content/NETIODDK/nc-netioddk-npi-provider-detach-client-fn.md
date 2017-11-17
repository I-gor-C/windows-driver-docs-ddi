---
UID: NC.netioddk.NPI_PROVIDER_DETACH_CLIENT_FN
title: NPI_PROVIDER_DETACH_CLIENT_FN
author: windows-driver-content
description: 
ms.assetid: 0fe961d6-6db1-4356-911d-3275ac96d1aa
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

# NPI_PROVIDER_DETACH_CLIENT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NPI_PROVIDER_DETACH_CLIENT_FN NpiProviderDetachClientFn; 

// Definition

NTSTATUS NpiProviderDetachClientFn 
(
	PVOID ProviderBindingContext
)
{...}

NPI_PROVIDER_DETACH_CLIENT_FN 


```

## -parameters

### -param ProviderBindingContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
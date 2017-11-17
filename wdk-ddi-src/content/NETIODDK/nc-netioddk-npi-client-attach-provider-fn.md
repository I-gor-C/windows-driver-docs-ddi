---
UID: NC.netioddk.NPI_CLIENT_ATTACH_PROVIDER_FN
title: NPI_CLIENT_ATTACH_PROVIDER_FN
author: windows-driver-content
description: 
ms.assetid: 848c891e-4539-4f61-8ae8-0e7373d6d7c7
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

# NPI_CLIENT_ATTACH_PROVIDER_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NPI_CLIENT_ATTACH_PROVIDER_FN NpiClientAttachProviderFn; 

// Definition

NTSTATUS NpiClientAttachProviderFn 
(
	HANDLE NmrBindingHandle
	PVOID ClientContext
	PNPI_REGISTRATION_INSTANCE ProviderRegistrationInstance
)
{...}

NPI_CLIENT_ATTACH_PROVIDER_FN 


```

## -parameters

### -param NmrBindingHandle: 
### -param ClientContext: 
### -param ProviderRegistrationInstance: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
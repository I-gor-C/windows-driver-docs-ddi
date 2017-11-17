---
UID: NC.ntifs.IMPERSONATE_SECURITY_CONTEXT_FN
title: IMPERSONATE_SECURITY_CONTEXT_FN
author: windows-driver-content
description: 
ms.assetid: b2153f30-da2a-418f-86cc-f90abb1cdb5d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# IMPERSONATE_SECURITY_CONTEXT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IMPERSONATE_SECURITY_CONTEXT_FN ImpersonateSecurityContextFn; 

// Definition

SECURITY_STATUS ImpersonateSecurityContextFn 
(
	PCtxtHandle 
)
{...}

IMPERSONATE_SECURITY_CONTEXT_FN 


```

## -parameters

### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
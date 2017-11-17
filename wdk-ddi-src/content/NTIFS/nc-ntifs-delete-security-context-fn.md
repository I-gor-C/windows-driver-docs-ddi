---
UID: NC.ntifs.DELETE_SECURITY_CONTEXT_FN
title: DELETE_SECURITY_CONTEXT_FN
author: windows-driver-content
description: 
ms.assetid: c1edffe0-2502-433b-a60f-64948b406e45
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

# DELETE_SECURITY_CONTEXT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DELETE_SECURITY_CONTEXT_FN DeleteSecurityContextFn; 

// Definition

SECURITY_STATUS DeleteSecurityContextFn 
(
	PCtxtHandle 
)
{...}

DELETE_SECURITY_CONTEXT_FN 


```

## -parameters

### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
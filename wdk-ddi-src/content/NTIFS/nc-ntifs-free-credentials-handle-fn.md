---
UID: NC.ntifs.FREE_CREDENTIALS_HANDLE_FN
title: FREE_CREDENTIALS_HANDLE_FN
author: windows-driver-content
description: 
ms.assetid: 1cd831ac-648d-4222-9c29-739fb7f1eced
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

# FREE_CREDENTIALS_HANDLE_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FREE_CREDENTIALS_HANDLE_FN FreeCredentialsHandleFn; 

// Definition

SECURITY_STATUS FreeCredentialsHandleFn 
(
	PCredHandle 
)
{...}

FREE_CREDENTIALS_HANDLE_FN 


```

## -parameters

### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
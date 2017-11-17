---
UID: NC.ntifs.QUERY_SECURITY_CONTEXT_TOKEN_FN
title: QUERY_SECURITY_CONTEXT_TOKEN_FN
author: windows-driver-content
description: 
ms.assetid: b3ea6f05-8e42-4b41-9b58-109ff4ad4289
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

# QUERY_SECURITY_CONTEXT_TOKEN_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

QUERY_SECURITY_CONTEXT_TOKEN_FN QuerySecurityContextTokenFn; 

// Definition

SECURITY_STATUS QuerySecurityContextTokenFn 
(
	PCtxtHandle 
	 void **
)
{...}

QUERY_SECURITY_CONTEXT_TOKEN_FN 


```

## -parameters

### -param : 
### -param **: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
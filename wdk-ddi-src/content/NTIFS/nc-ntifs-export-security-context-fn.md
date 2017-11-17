---
UID: NC.ntifs.EXPORT_SECURITY_CONTEXT_FN
title: EXPORT_SECURITY_CONTEXT_FN
author: windows-driver-content
description: 
ms.assetid: 9d90ce55-191f-4211-8e85-e63bf4f7bbb0
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

# EXPORT_SECURITY_CONTEXT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXPORT_SECURITY_CONTEXT_FN ExportSecurityContextFn; 

// Definition

SECURITY_STATUS ExportSecurityContextFn 
(
	PCtxtHandle 
	ULONG 
	PSecBuffer 
	 void **
)
{...}

EXPORT_SECURITY_CONTEXT_FN 


```

## -parameters

### -param : 
### -param : 
### -param : 
### -param **: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
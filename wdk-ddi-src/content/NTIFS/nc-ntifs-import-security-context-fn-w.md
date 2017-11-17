---
UID: NC.ntifs.IMPORT_SECURITY_CONTEXT_FN_W
title: IMPORT_SECURITY_CONTEXT_FN_W
author: windows-driver-content
description: 
ms.assetid: fe50bdf1-0a83-47e9-8257-b1a814b61c50
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

# IMPORT_SECURITY_CONTEXT_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IMPORT_SECURITY_CONTEXT_FN_W ImportSecurityContextFnW; 

// Definition

SECURITY_STATUS ImportSecurityContextFnW 
(
	PSECURITY_STRING 
	SEC_WCHAR *
	PSecBuffer 
	VOID *
	PCtxtHandle 
)
{...}

IMPORT_SECURITY_CONTEXT_FN_W 


```

## -parameters

### -param : 
### -param *: 
### -param : 
### -param *: 
### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
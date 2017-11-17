---
UID: NC.ntifs.INITIALIZE_SECURITY_CONTEXT_FN_W
title: INITIALIZE_SECURITY_CONTEXT_FN_W
author: windows-driver-content
description: 
ms.assetid: 6e235de4-0a8b-4bb0-af78-3d7b292e783a
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

# INITIALIZE_SECURITY_CONTEXT_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

INITIALIZE_SECURITY_CONTEXT_FN_W InitializeSecurityContextFnW; 

// Definition

SECURITY_STATUS InitializeSecurityContextFnW 
(
	PCredHandle 
	PCtxtHandle 
	PSECURITY_STRING 
	SEC_WCHAR *
	 unsigned long
	 unsigned long
	 unsigned long
	PSecBufferDesc 
	 unsigned long
	PCtxtHandle 
	PSecBufferDesc 
	 unsigned long *
	PTimeStamp 
)
{...}

INITIALIZE_SECURITY_CONTEXT_FN_W 


```

## -parameters

### -param : 
### -param : 
### -param : 
### -param *: 
### -param long: 
### -param long: 
### -param long: 
### -param : 
### -param long: 
### -param : 
### -param : 
### -param *: 
### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
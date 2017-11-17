---
UID: NC.ntifs.ACQUIRE_CREDENTIALS_HANDLE_FN_W
title: ACQUIRE_CREDENTIALS_HANDLE_FN_W
author: windows-driver-content
description: 
ms.assetid: c22cba6c-f1a8-48d7-9907-43995a6a3583
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

# ACQUIRE_CREDENTIALS_HANDLE_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ACQUIRE_CREDENTIALS_HANDLE_FN_W AcquireCredentialsHandleFnW; 

// Definition

SECURITY_STATUS AcquireCredentialsHandleFnW 
(
	PSECURITY_STRING 
	PSECURITY_STRING 
	SEC_WCHAR *
	SEC_WCHAR *
	 unsigned long
	 void *
	 void *
	SEC_GET_KEY_FN 
	 void *
	PCredHandle 
	PTimeStamp 
)
{...}

ACQUIRE_CREDENTIALS_HANDLE_FN_W 


```

## -parameters

### -param : 
### -param : 
### -param *: 
### -param *: 
### -param long: 
### -param *: 
### -param *: 
### -param : 
### -param *: 
### -param : 
### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
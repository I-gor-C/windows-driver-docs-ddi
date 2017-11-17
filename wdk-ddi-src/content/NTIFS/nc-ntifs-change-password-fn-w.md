---
UID: NC.ntifs.CHANGE_PASSWORD_FN_W
title: CHANGE_PASSWORD_FN_W
author: windows-driver-content
description: 
ms.assetid: 5c32c820-481c-42d1-bede-b12a7adb2355
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

# CHANGE_PASSWORD_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CHANGE_PASSWORD_FN_W ChangePasswordFnW; 

// Definition

SECURITY_STATUS ChangePasswordFnW 
(
	SEC_WCHAR *
	SEC_WCHAR *
	SEC_WCHAR *
	SEC_WCHAR *
	SEC_WCHAR *
	BOOLEAN 
	 unsigned long
	PSecBufferDesc 
)
{...}

CHANGE_PASSWORD_FN_W 


```

## -parameters

### -param *: 
### -param *: 
### -param *: 
### -param *: 
### -param *: 
### -param : 
### -param long: 
### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
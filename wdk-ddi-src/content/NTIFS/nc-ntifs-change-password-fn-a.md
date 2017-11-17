---
UID: NC.ntifs.CHANGE_PASSWORD_FN_A
title: CHANGE_PASSWORD_FN_A
author: windows-driver-content
description: 
ms.assetid: 5bfeb292-b3f8-4ad0-b763-40c261ebcfeb
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

# CHANGE_PASSWORD_FN_A callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CHANGE_PASSWORD_FN_A ChangePasswordFnA; 

// Definition

SECURITY_STATUS ChangePasswordFnA 
(
	SEC_CHAR *
	SEC_CHAR *
	SEC_CHAR *
	SEC_CHAR *
	SEC_CHAR *
	BOOLEAN 
	 unsigned long
	PSecBufferDesc 
)
{...}

CHANGE_PASSWORD_FN_A 


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
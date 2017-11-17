---
UID: NC.ntifs.ADD_CREDENTIALS_FN_A
title: ADD_CREDENTIALS_FN_A
author: windows-driver-content
description: 
ms.assetid: 8603d5ae-96a9-4220-9ac5-884cf83063c4
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

# ADD_CREDENTIALS_FN_A callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ADD_CREDENTIALS_FN_A AddCredentialsFnA; 

// Definition

SECURITY_STATUS AddCredentialsFnA 
(
	PCredHandle 
	SEC_CHAR *
	SEC_CHAR *
	 unsigned long
	 void *
	SEC_GET_KEY_FN 
	 void *
	PTimeStamp 
)
{...}

ADD_CREDENTIALS_FN_A 


```

## -parameters

### -param : 
### -param *: 
### -param *: 
### -param long: 
### -param *: 
### -param : 
### -param *: 
### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
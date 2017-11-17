---
UID: NC.ntifs.SET_CREDENTIALS_ATTRIBUTES_FN_W
title: SET_CREDENTIALS_ATTRIBUTES_FN_W
author: windows-driver-content
description: 
ms.assetid: aa468ade-89a7-4490-82e9-c193000da38c
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

# SET_CREDENTIALS_ATTRIBUTES_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SET_CREDENTIALS_ATTRIBUTES_FN_W SetCredentialsAttributesFnW; 

// Definition

SECURITY_STATUS SetCredentialsAttributesFnW 
(
	PCredHandle 
	 unsigned long
	 void *
	 unsigned long
)
{...}

SET_CREDENTIALS_ATTRIBUTES_FN_W 


```

## -parameters

### -param : 
### -param long: 
### -param *: 
### -param long: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
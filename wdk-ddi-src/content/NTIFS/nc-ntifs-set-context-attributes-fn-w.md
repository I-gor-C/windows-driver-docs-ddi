---
UID: NC.ntifs.SET_CONTEXT_ATTRIBUTES_FN_W
title: SET_CONTEXT_ATTRIBUTES_FN_W
author: windows-driver-content
description: 
ms.assetid: d103b209-6982-44f2-8f1c-6d5204963be8
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

# SET_CONTEXT_ATTRIBUTES_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SET_CONTEXT_ATTRIBUTES_FN_W SetContextAttributesFnW; 

// Definition

SECURITY_STATUS SetContextAttributesFnW 
(
	PCtxtHandle 
	 unsigned long
	 void *
	 unsigned long
)
{...}

SET_CONTEXT_ATTRIBUTES_FN_W 


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
---
UID: NC.ntifs.QUERY_CONTEXT_ATTRIBUTES_FN_W
title: QUERY_CONTEXT_ATTRIBUTES_FN_W
author: windows-driver-content
description: 
ms.assetid: 40704a8a-04d4-424e-9279-0be934920a9d
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

# QUERY_CONTEXT_ATTRIBUTES_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

QUERY_CONTEXT_ATTRIBUTES_FN_W QueryContextAttributesFnW; 

// Definition

SECURITY_STATUS QueryContextAttributesFnW 
(
	PCtxtHandle 
	 unsigned long
	 void *
)
{...}

QUERY_CONTEXT_ATTRIBUTES_FN_W 


```

## -parameters

### -param : 
### -param long: 
### -param *: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
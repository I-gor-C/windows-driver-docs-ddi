---
UID: NC.wdfobject.PFN_GET_UNIQUE_CONTEXT_TYPE
title: PFN_GET_UNIQUE_CONTEXT_TYPE
author: windows-driver-content
description: 
ms.assetid: 44daf961-f9f3-4449-bfdf-5c739dccaf3e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfobject.h
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

# PFN_GET_UNIQUE_CONTEXT_TYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_GET_UNIQUE_CONTEXT_TYPE PfnGetUniqueContextType; 

// Definition

PCWDF_OBJECT_CONTEXT_TYPE_INFO PfnGetUniqueContextType 
(
	 VOID
)
{...}

PFN_GET_UNIQUE_CONTEXT_TYPE 


```

## -parameters

### -param VOID: 



## -returns

Returns PCWDF_OBJECT_CONTEXT_TYPE_INFO that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
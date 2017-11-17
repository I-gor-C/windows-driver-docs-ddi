---
UID: NC.ks.PFNKSDELETEALLOCATOR
title: PFNKSDELETEALLOCATOR
author: windows-driver-content
description: 
ms.assetid: 8bf2f400-28ed-4b29-b35a-e3b1d393faba
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSDELETEALLOCATOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDELETEALLOCATOR Pfnksdeleteallocator; 

// Definition

VOID Pfnksdeleteallocator 
(
	PVOID Context
)
{...}

PFNKSDELETEALLOCATOR 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
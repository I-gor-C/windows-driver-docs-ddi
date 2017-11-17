---
UID: NC.wdm.FREE_FUNCTION
title: FREE_FUNCTION
author: windows-driver-content
description: 
ms.assetid: deeb2aad-7d5f-4d60-9222-30989a3ec962
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# FREE_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FREE_FUNCTION FreeFunction; 

// Definition

VOID FreeFunction 
(
	__drv_freesMem(Mem)PVOID Buffer
)
{...}

FREE_FUNCTION PFREE_FUNCTION


```

## -parameters

### -param Buffer: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
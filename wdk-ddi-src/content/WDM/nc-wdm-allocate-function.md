---
UID: NC.wdm.ALLOCATE_FUNCTION
title: ALLOCATE_FUNCTION
author: windows-driver-content
description: 
ms.assetid: bba4d2f1-92a3-4de1-9550-3e2f45e9fe72
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

# ALLOCATE_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ALLOCATE_FUNCTION AllocateFunction; 

// Definition

PVOID AllocateFunction 
(
	POOL_TYPE PoolType
	SIZE_T NumberOfBytes
	ULONG Tag
)
{...}

ALLOCATE_FUNCTION PALLOCATE_FUNCTION


```

## -parameters

### -param PoolType: 
### -param NumberOfBytes: 
### -param Tag: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
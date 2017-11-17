---
UID: NC.ks.PFNALLOCATOR_FREEFRAME
title: PFNALLOCATOR_FREEFRAME
author: windows-driver-content
description: 
ms.assetid: 94562159-982c-40dd-9996-a15dd9e2850f
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

# PFNALLOCATOR_FREEFRAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNALLOCATOR_FREEFRAME PfnallocatorFreeframe; 

// Definition

VOID PfnallocatorFreeframe 
(
	PFILE_OBJECT FileObject
	PVOID Frame
)
{...}

PFNALLOCATOR_FREEFRAME 


```

## -parameters

### -param FileObject: 
### -param Frame: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
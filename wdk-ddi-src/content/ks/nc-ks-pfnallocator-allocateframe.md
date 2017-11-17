---
UID: NC.ks.PFNALLOCATOR_ALLOCATEFRAME
title: PFNALLOCATOR_ALLOCATEFRAME
author: windows-driver-content
description: 
ms.assetid: 27fd2133-f8e5-4dfa-85d9-eb4a3a2b4074
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

# PFNALLOCATOR_ALLOCATEFRAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNALLOCATOR_ALLOCATEFRAME PfnallocatorAllocateframe; 

// Definition

NTSTATUS PfnallocatorAllocateframe 
(
	PFILE_OBJECT FileObject
	PVOID *Frame
)
{...}

PFNALLOCATOR_ALLOCATEFRAME 


```

## -parameters

### -param FileObject: 
### -param *Frame: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
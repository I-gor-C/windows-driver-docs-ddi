---
UID: NC.ntifs.RTL_HEAP_COMMIT_ROUTINE
title: RTL_HEAP_COMMIT_ROUTINE
author: windows-driver-content
description: 
ms.assetid: f1faff82-7739-4d48-b880-1f0253af8659
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

# RTL_HEAP_COMMIT_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_HEAP_COMMIT_ROUTINE RtlHeapCommitRoutine; 

// Definition

_IRQL_requires_same_ NTSTATUS RtlHeapCommitRoutine 
(
	PVOID Base
	PVOID * CommitAddress
	PSIZE_T CommitSize
)
{...}

RTL_HEAP_COMMIT_ROUTINE PRTL_HEAP_COMMIT_ROUTINE


```

## -parameters

### -param Base: 
### -param CommitAddress: 
### -param CommitSize: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
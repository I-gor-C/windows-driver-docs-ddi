---
UID: NC.wdbgexts.PWINDBG_READ_PROCESS_MEMORY_ROUTINE32
title: PWINDBG_READ_PROCESS_MEMORY_ROUTINE32
author: windows-driver-content
description: 
ms.assetid: 3b239bd2-e947-466d-a6fc-a8ae0560b034
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_READ_PROCESS_MEMORY_ROUTINE32 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_READ_PROCESS_MEMORY_ROUTINE32 PwindbgReadProcessMemoryRoutine32; 

// Definition

ULONG PwindbgReadProcessMemoryRoutine32 
(
	ULONG offset
	PVOID lpBuffer
	ULONG cb
	PULONG lpcbBytesRead
)
{...}

PWINDBG_READ_PROCESS_MEMORY_ROUTINE32 


```

## -parameters

### -param offset: 
### -param lpBuffer: 
### -param cb: 
### -param lpcbBytesRead: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
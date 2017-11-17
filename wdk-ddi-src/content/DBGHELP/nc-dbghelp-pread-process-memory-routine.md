---
UID: NC.dbghelp.PREAD_PROCESS_MEMORY_ROUTINE
title: PREAD_PROCESS_MEMORY_ROUTINE
author: windows-driver-content
description: 
ms.assetid: f83689db-c970-4851-8749-dcfdff596d97
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# PREAD_PROCESS_MEMORY_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREAD_PROCESS_MEMORY_ROUTINE PreadProcessMemoryRoutine; 

// Definition

BOOL PreadProcessMemoryRoutine 
(
	HANDLE hProcess
	DWORD lpBaseAddress
	PVOID lpBuffer
	DWORD nSize
	PDWORD lpNumberOfBytesRead
)
{...}

PREAD_PROCESS_MEMORY_ROUTINE 


```

## -parameters

### -param hProcess: 
### -param lpBaseAddress: 
### -param lpBuffer: 
### -param nSize: 
### -param lpNumberOfBytesRead: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
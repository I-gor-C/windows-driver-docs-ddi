---
UID: NC.wdbgexts.PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE64
title: PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE64
author: windows-driver-content
description: 
ms.assetid: 7a494415-a469-4159-9792-2faad52a75ed
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

# PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE64 PwindbgWriteProcessMemoryRoutine64; 

// Definition

ULONG PwindbgWriteProcessMemoryRoutine64 
(
	ULONG64 offset
	LPCVOID lpBuffer
	ULONG cb
	PULONG lpcbBytesWritten
)
{...}

PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE64 


```

## -parameters

### -param offset: 
### -param lpBuffer: 
### -param cb: 
### -param lpcbBytesWritten: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
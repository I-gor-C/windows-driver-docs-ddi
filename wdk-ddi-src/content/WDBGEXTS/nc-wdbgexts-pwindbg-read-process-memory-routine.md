---
UID: NC.wdbgexts.PWINDBG_READ_PROCESS_MEMORY_ROUTINE
title: PWINDBG_READ_PROCESS_MEMORY_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 82e59cc6-1494-4dd3-8c30-ec70373519ba
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

# PWINDBG_READ_PROCESS_MEMORY_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_READ_PROCESS_MEMORY_ROUTINE PwindbgReadProcessMemoryRoutine; 

// Definition

ULONG PwindbgReadProcessMemoryRoutine 
(
	ULONG_PTR offset
	PVOID lpBuffer
	ULONG cb
	PULONG lpcbBytesRead
)
{...}

PWINDBG_READ_PROCESS_MEMORY_ROUTINE 


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
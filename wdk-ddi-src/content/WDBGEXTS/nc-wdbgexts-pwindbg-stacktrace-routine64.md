---
UID: NC.wdbgexts.PWINDBG_STACKTRACE_ROUTINE64
title: PWINDBG_STACKTRACE_ROUTINE64
author: windows-driver-content
description: 
ms.assetid: 2989c759-9dce-4457-a16c-d56dff1ace09
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

# PWINDBG_STACKTRACE_ROUTINE64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_STACKTRACE_ROUTINE64 PwindbgStacktraceRoutine64; 

// Definition

ULONG PwindbgStacktraceRoutine64 
(
	ULONG64 FramePointer
	ULONG64 StackPointer
	ULONG64 ProgramCounter
	PEXTSTACKTRACE64 StackFrames
	ULONG Frames
)
{...}

PWINDBG_STACKTRACE_ROUTINE64 


```

## -parameters

### -param FramePointer: 
### -param StackPointer: 
### -param ProgramCounter: 
### -param StackFrames: 
### -param Frames: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdbgexts.PWINDBG_STACKTRACE_ROUTINE32
title: PWINDBG_STACKTRACE_ROUTINE32
author: windows-driver-content
description: 
ms.assetid: bead0173-82d4-4da6-90ba-fc841bc03571
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

# PWINDBG_STACKTRACE_ROUTINE32 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_STACKTRACE_ROUTINE32 PwindbgStacktraceRoutine32; 

// Definition

ULONG PwindbgStacktraceRoutine32 
(
	ULONG FramePointer
	ULONG StackPointer
	ULONG ProgramCounter
	PEXTSTACKTRACE32 StackFrames
	ULONG Frames
)
{...}

PWINDBG_STACKTRACE_ROUTINE32 


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
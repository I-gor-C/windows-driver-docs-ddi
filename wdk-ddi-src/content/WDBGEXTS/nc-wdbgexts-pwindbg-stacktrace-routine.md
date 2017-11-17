---
UID: NC.wdbgexts.PWINDBG_STACKTRACE_ROUTINE
title: PWINDBG_STACKTRACE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: e8883f4e-ed8e-495a-be61-240bee939d8b
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

# PWINDBG_STACKTRACE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_STACKTRACE_ROUTINE PwindbgStacktraceRoutine; 

// Definition

ULONG PwindbgStacktraceRoutine 
(
	ULONG FramePointer
	ULONG StackPointer
	ULONG ProgramCounter
	PEXTSTACKTRACE StackFrames
	ULONG Frames
)
{...}

PWINDBG_STACKTRACE_ROUTINE 


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
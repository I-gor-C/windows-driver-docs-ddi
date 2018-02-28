---
UID: NC:wdbgexts.PWINDBG_STACKTRACE_ROUTINE
title: PWINDBG_STACKTRACE_ROUTINE
author: windows-driver-content
description: The PWINDBG_STACKTRACE_ROUTINE (StackTrace) function retrieves a stack trace for the process being debugged. Returns the number of frames read into the buffer pointed to by StackFrames.
old-location: debugger\stacktrace.htm
old-project: debugger
ms.assetid: 689d99a2-6971-4098-84fb-4c40dc2bbaac
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: PWINDBG_STACKTRACE_ROUTINE, StackTrace, StackTrace callback function [Windows Debugging], WdbgExts_Ref_5ccc4adf-2b59-4373-8e4a-3bc8847c5749.xml, debugger.stacktrace, wdbgexts/StackTrace
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	wdbgexts.h
api_name:
-	StackTrace
product: Windows
targetos: Windows
req.typenames: VPCI_WRITE_BLOCK_INPUT, *PVPCI_WRITE_BLOCK_INPUT
req.product: Windows 10 or later.
---


# PWINDBG_STACKTRACE_ROUTINE callback function
The <b>PWINDBG_STACKTRACE_ROUTINE</b>  (<b>StackTrace</b>) function retrieves a stack trace for the process being debugged. Returns the number of frames read into the buffer pointed to by <i>StackFrames</i>.

## Syntax

```
PWINDBG_STACKTRACE_ROUTINE PwindbgStacktraceRoutine;

ULONG PwindbgStacktraceRoutine(
  ULONG FramePointer,
  ULONG StackPointer,
  ULONG ProgramCounter,
  PEXTSTACKTRACE StackFrames,
  ULONG Frames
)
{...}
```

## Parameters

`FramePointer`

Specifies the frame pointer. If no specific value is desired, this should simply be set to zero.

`StackPointer`

Specifies the stack pointer. If no specific value is desired, this should simply be set to zero.

`ProgramCounter`

Specifies the instruction pointer. If no specific value is desired, this should simply be set to zero.

`StackFrames`

Receives the stack information. <i>StackFrames</i> must be a pointer to a buffer that is large enough to hold the number of stack frames specified by <i>Frames</i>. The stack frames are stored in the following data structure:

<pre class="syntax" xml:space="preserve"><code>typedef struct _tagEXTSTACKTRACE {
    ULONG       FramePointer;
    ULONG       ProgramCounter;
    ULONG       ReturnAddress;
    ULONG       Args[4];
} EXTSTACKTRACE, *PEXTSTACKTRACE;</code></pre>

`Frames`

Specifies the maximum number of frames that will fit into the buffer.


## Return Value

The actual number of frames written to the buffer pointed to by <i>StackFrames</i>.

## Remarks

For a WdbgExts extension, include Wdbgexts.h. For 

a DbgEng extension, include Wdbgexts.h before 

Dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for 

details.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | wdbgexts.h (include Wdbgexts.h, Dbgeng.h) |
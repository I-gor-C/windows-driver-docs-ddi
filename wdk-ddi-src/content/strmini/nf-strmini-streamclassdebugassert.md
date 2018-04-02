---
UID: NF:strmini.StreamClassDebugAssert
title: StreamClassDebugAssert function
author: windows-driver-content
description: A minidriver can use the StreamClassDebugAssert routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger.
old-location: stream\streamclassdebugassert.htm
old-project: stream
ms.assetid: df9b3231-4c43-4d4b-b128-e8d6a9f21b17
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: StreamClassDebugAssert, StreamClassDebugAssert routine [Streaming Media Devices], strclass-routines_6f9302e6-592f-4097-830c-83b05a54d335.xml, stream.streamclassdebugassert, strmini/StreamClassDebugAssert
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: strmini.h
req.include-header: Strmini.h
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
req.lib: Stream.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Stream.lib
-	Stream.dll
api_name:
-	StreamClassDebugAssert
product:
- Windows
targetos: Windows
req.typenames: STREAM_PRIORITY, *PSTREAM_PRIORITY
req.product: Windows 10 or later.
---


# StreamClassDebugAssert function
A minidriver can use the <b>StreamClassDebugAssert</b> routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger.

## Syntax

```
__analysis_noreturn VOID STREAMAPI StreamClassDebugAssert(
  IN PCHAR File,
  IN ULONG Line,
  IN PCHAR AssertText,
  IN ULONG AssertValue
);
```

## Parameters

`File`

Pointer to a <b>NULL</b>-terminated string containing the file name in which the assert occurred.

`Line`

Specifies the line number of the assert.

`AssertText`

Pointer to a <b>NULL</b>-terminated string containing text to be printed in the debug message.

`AssertValue`

Specifies a value to be printed in the debug message.


## Return Value

None

## Remarks

When running a checked version of the class driver, asserts are recognized, and result in a debug message and breakpoint. When running a free version of the class driver, asserts are ignored. For more information, see <a href="https://msdn.microsoft.com/544b922b-58e4-4cbb-a76c-d8e13ae17e55">Stream Class Debugging</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | strmini.h (include Strmini.h) |
| **Library** | Stream.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543626">DbgBreakPoint</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568235">StreamClassDebugPrint</a>
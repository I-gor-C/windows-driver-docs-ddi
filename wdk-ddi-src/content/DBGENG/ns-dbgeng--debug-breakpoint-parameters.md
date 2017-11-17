---
UID: NS.dbgeng._DEBUG_BREAKPOINT_PARAMETERS
title: DEBUG_BREAKPOINT_PARAMETERS
author: windows-driver-content
description: The DEBUG_BREAKPOINT_PARAMETERS structure contains most of the parameters for describing a breakpoint.
old-location: debugger\debug_breakpoint_parameters.htm
ms.assetid: e5c87c1c-8195-4476-84bc-5f18ad83d149
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_BREAKPOINT_PARAMETERS
req.alt-loc: DbgEng.h
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
ms.keywords: DEBUG_BREAKPOINT_PARAMETERS, DEBUG_BREAKPOINT_PARAMETERS, *PDEBUG_BREAKPOINT_PARAMETERS
req.iface: IDebugSystemObjects4
---

# DEBUG_BREAKPOINT_PARAMETERS structure



## -description
<p>The DEBUG_BREAKPOINT_PARAMETERS structure contains most of the parameters for describing a breakpoint.</p>


## -syntax

````
typedef struct _DEBUG_BREAKPOINT_PARAMETERS {
  ULONG64 Offset;
  ULONG   Id;
  ULONG   BreakType;
  ULONG   ProcType;
  ULONG   Flags;
  ULONG   DataSize;
  ULONG   DataAccessType;
  ULONG   PassCount;
  ULONG   CurrentPassCount;
  ULONG   MatchThread;
  ULONG   CommandSize;
  ULONG   OffsetExpressionSize;
} DEBUG_BREAKPOINT_PARAMETERS, *PDEBUG_BREAKPOINT_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Offset</b>

<dd>
<p>The location in the target's memory address space that will trigger the breakpoint.  If the breakpoint is deferred (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546791">GetFlags</a>), <b>Offset</b> is DEBUG_INVALID_OFFSET.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff548008">GetOffset</a>.</p>
</dd>

### -field <b>Id</b>

<dd>
<p>The breakpoint ID.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff546827">GetId</a>.</p>
</dd>

### -field <b>BreakType</b>

<dd>
<p>Specifies if the breakpoint is a software breakpoint or a processor breakpoint.  See <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a>.</p>
</dd>

### -field <b>ProcType</b>

<dd>
<p>The processor type for which the breakpoint is set.  See <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The flags for the breakpoint.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff546791">GetFlags</a>.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>The size, in bytes, of the memory block whose access will trigger the breakpoint.  If the type of the breakpoint is not a data breakpoint, this is zero.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff546557">GetDataParameters</a>.</p>
</dd>

### -field <b>DataAccessType</b>

<dd>
<p>The type of access that will trigger the breakpoint.  If the type of the breakpoint is not a data breakpoint, this is zero.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff546557">GetDataParameters</a>.</p>
</dd>

### -field <b>PassCount</b>

<dd>
<p>The number of times the target will hit the breakpoint before it is triggered.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff548104">GetPassCount</a>.</p>
</dd>

### -field <b>CurrentPassCount</b>

<dd>
<p>The remaining number of times that the target will hit the breakpoint before it is triggered.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff545769">GetCurrentPassCount</a>.</p>
</dd>

### -field <b>MatchThread</b>

<dd>
<p>The engine thread ID of the thread that can trigger this breakpoint.  If any thread can trigger this breakpoint, <b>MatchThread</b> is DEBUG_ANY_ID.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff547074">GetMatchThreadId</a>.</p>
</dd>

### -field <b>CommandSize</b>

<dd>
<p>The size, in characters, of the command string that will be executed when the breakpoint is triggered.  If no command is set, <b>CommandSize</b> is zero.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff545677">GetCommand</a>.</p>
</dd>

### -field <b>OffsetExpressionSize</b>

<dd>
<p>The size, in characters, of the expression string that evaluates to the location in the target's memory address space where the breakpoint is triggered.  If no expression string is set, <b>OffsetExpressionSize</b> is zero.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff548048">GetOffsetExpression</a>.</p>
</dd>
</dl>

## -remarks
<p>For an overview of how to use breakpoints, and a description of all breakpoint-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538928">Breakpoints</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>
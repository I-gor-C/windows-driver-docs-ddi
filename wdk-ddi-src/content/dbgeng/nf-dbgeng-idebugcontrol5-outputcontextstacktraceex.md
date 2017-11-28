---
UID: NF.dbgeng.IDebugControl5.OutputContextStackTraceEx
title: IDebugControl5::OutputContextStackTraceEx
author: windows-driver-content
description: The OutputContextStackTraceEx method prints the call stack specified by an array of stack frames and corresponding register contexts.
old-location: debugger\idebugcontrol5_outputcontextstacktraceex.htm
old-project: debugger
ms.assetid: B0C1E602-83CE-4F4E-9198-B1B1CDAFF4BF
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl5, OutputContextStackTraceEx, IDebugControl5::OutputContextStackTraceEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl5.OutputContextStackTraceEx
req.alt-loc: dbgeng.h
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
req.iface: IDebugControl5
---

# IDebugControl5::OutputContextStackTraceEx method



## -description
<p>The OutputContextStackTraceEx method prints the call stack specified by an array of stack frames and corresponding register contexts. The OutputContextStackTraceEx method provides inline frame support. For more information about working with inline functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406275">Debugging Optimized Code and Inline Functions</a>.</p>


## -syntax

````
HRESULT OutputContextStackTraceEx(
  [in] ULONG                 OutputControl,
  [in] PDEBUG_STACK_FRAME_EX Frames,
  [in] ULONG                 FramesSize,
  [in] PVOID                 FrameContexts,
  [in] ULONG                 FrameContextsSize,
  [in] ULONG                 FrameContextsEntrySize,
  [in] ULONG                 Flags
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies where to send the output.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.</p>
</dd>

### -param <i>Frames</i> [in]

<dd>
<p>Specifies the array of stack frames to output.  The number of elements in this array is <i>FramesSize</i>.  If <i>Frames</i> is <b>NULL</b>, the current stack frame is used.</p>
</dd>

### -param <i>FramesSize</i> [in]

<dd>
<p>Specifies the number of frames to output.</p>
</dd>

### -param <i>FrameContexts</i> [in]

<dd>
<p>Specifies the register context for each frame in the stack.  The entries in this array correspond to the entries in the <i>Frames</i> array.  The type of the thread context is the CONTEXT structure for the target's effective processor.</p>
</dd>

### -param <i>FrameContextsSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the memory pointed to by <i>FrameContexts</i>.  The number of stack frames must equal the number of contexts, and <i>FrameContextsSize</i> must equal <i>FramesSize</i> multiplied by <i>FrameContextsEntrySize</i>.</p>
</dd>

### -param <i>FrameContextsEntrySize</i> [in]

<dd>
<p>Specifies the size, in bytes, of each frame context in <i>FrameContexts</i>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies bit flags that determine what information to output for each frame.  <i>Flags</i> can be any combination of values from the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_STACK_ARGUMENTS</p>
</td>
<td>
<p>Displays the first three pieces of stack memory at the frame of each call.  On platforms where arguments are passed on the stack, and the code for the frame uses stack arguments, these values will be the arguments to the function.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_FUNCTION_INFO</p>
</td>
<td>
<p>Displays information about the function that corresponds to the frame.  This includes calling convention and frame pointer omission (FPO) information.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_SOURCE_LINE</p>
</td>
<td>
<p>Displays source line information for each frame of the stack trace.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_FRAME_ADDRESSES</p>
</td>
<td>
<p>Displays the return address, previous frame address, and other relevant addresses for each frame.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_COLUMN_NAMES</p>
</td>
<td>
<p>Displays column names.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_NONVOLATILE_REGISTERS</p>
</td>
<td>
<p>Displays the non-volatile register context for each frame.  This is only meaningful for some platforms.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_FRAME_NUMBERS</p>
</td>
<td>
<p>Displays frame numbers.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_PARAMETERS</p>
</td>
<td>
<p>Displays parameter names and values as given in symbol information.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_FRAME_ADDRESSES_RA_ONLY</p>
</td>
<td>
<p>Displays just the return address in the stack frame addresses.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_FRAME_MEMORY_USAGE</p>
</td>
<td>
<p>Displays the number of bytes that separate the frames.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STACK_PARAMETERS_NEWLINE</p>
</td>
<td>
<p>Displays each parameter and its type and value on a new line.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn818562">IDebugControl5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl5::OutputContextStackTraceEx method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.dbgeng.IDebugControl3.OutputStackTrace
title: IDebugControl3::OutputStackTrace
author: windows-driver-content
description: The OutputStackTrace method outputs either the supplied stack frame or the current stack frames.
old-location: debugger\outputstacktrace.htm
ms.assetid: 207f289c-347c-4ae7-9bbd-7c4a04d19e24
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.OutputStackTrace,IDebugControl2.OutputStackTrace,IDebugControl3.OutputStackTrace
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
ms.keywords: IDebugControl3, OutputStackTrace, IDebugControl3::OutputStackTrace
req.iface: IDebugControl3
---

# IDebugControl3::OutputStackTrace method



## -description
<p>The <b>OutputStackTrace</b> method outputs either the supplied stack frame or the current stack frames.</p>


## -syntax

````
HRESULT OutputStackTrace(
  [in]           ULONG              OutputControl,
  [in, optional] PDEBUG_STACK_FRAME Frames,
  [in]           ULONG              FramesSize,
  [in]           ULONG              Flags
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies where to send the output.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.</p>
</dd>

### -param <i>Frames</i> [in, optional]

<dd>
<p>Specifies the array of stack frames to output.  The number of elements in this array is <i>FramesSize</i>.  If <i>Frames</i> is <b>NULL</b>, the current stack frames are used.</p>
</dd>

### -param <i>FramesSize</i> [in]

<dd>
<p>Specifies the number of frames to output.</p>
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
<p>Displays the first three pieces of stack memory at the frame of each call.  On platforms where parameters are passed on the stack, and the code for the frame uses stack arguments, these values will be the arguments to the function.</p>
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
<p>Displays just the return address in stack frame addresses.</p>
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
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The array of stack frames can be obtained using <a href="https://msdn.microsoft.com/library/windows/hardware/ff548425">GetStackTrace</a>.</p>

<p>The array of stack frames can be obtained using <a href="https://msdn.microsoft.com/library/windows/hardware/ff548425">GetStackTrace</a>.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545748">GetContextStackTrace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548425">GetStackTrace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1061015f-cb0c-490b-b256-e0dedb659f22">k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::OutputStackTrace method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

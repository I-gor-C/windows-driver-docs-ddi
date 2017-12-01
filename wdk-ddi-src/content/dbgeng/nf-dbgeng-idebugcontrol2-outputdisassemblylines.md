---
UID: NF.dbgeng.IDebugControl2.OutputDisassemblyLines
title: IDebugControl2::OutputDisassemblyLines
author: windows-driver-content
description: The OutputDisassemblyLines method disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks.
old-location: debugger\outputdisassemblylines.htm
old-project: debugger
ms.assetid: fb69e052-1033-457d-bafb-bf4be4ea5966
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, OutputDisassemblyLines, IDebugControl2::OutputDisassemblyLines
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.OutputDisassemblyLines,IDebugControl2.OutputDisassemblyLines,IDebugControl3.OutputDisassemblyLines
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
req.iface: IDebugControl2
---

# IDebugControl2::OutputDisassemblyLines method



## -description
<p>The <b>OutputDisassemblyLines</b> method disassembles several processor instructions and sends the resulting assembly instructions to the <a href="debugger.using_input_and_output#output_callbacks#output_callbacks">output callbacks</a>.</p>


## -syntax

````
HRESULT OutputDisassemblyLines(
  [in]            ULONG    OutputControl,
  [in]            ULONG    PreviousLines,
  [in]            ULONG    TotalLines,
  [in]            ULONG64  Offset,
  [in]            ULONG    Flags,
  [out, optional] PULONG   OffsetLine,
  [out, optional] PULONG64 StartOffset,
  [out, optional] PULONG64 EndOffset,
  [out, optional] PULONG64 LineOffsets
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies the output control that determines which client's output callbacks receive the output.  For possible values, see <a href="debugger.debug_outctl_xxx">DEBUG_OUTCTL_XXX</a>.  For more information about output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>
</dd>

### -param <i>PreviousLines</i> [in]

<dd>
<p>Specifies the number of lines of instructions before the instruction at <i>Offset</i> to include in the output.  Typically, each instruction is output on a single line.  However, some instructions can take up several lines of output; this can cause the number of lines output before the instruction at <i>Offset</i> to be greater than <i>PreviousLines</i>.</p>
</dd>

### -param <i>TotalLines</i> [in]

<dd>
<p>Specifies the total number of lines of instructions to include in the output.  Typically, each instruction is output on a single line.  However, some instructions can take up several lines of output; this can cause the number of lines output to be greater than <i>TotalLines</i>.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's memory of the instructions to disassemble.  The disassembly output will start <i>PreviousLines</i> lines before these processor instructions.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies the bit-flags that affect the behavior of this method.  The following table lists the bits that can be set.</p>
<table>
<tr>
<th>Bit-Flag</th>
<th>Effect when set</th>
</tr>
<tr>
<td>
<p>DEBUG_DISASM_EFFECTIVE_ADDRESS</p>
</td>
<td>
<p>Compute the effective address of each instruction from the current register information and output it.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DISASM_MATCHING_SYMBOLS</p>
</td>
<td>
<p>If the address of an instruction has an exact symbol match, output the symbol.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DISASM_SOURCE_LINE_NUMBER</p>
</td>
<td>
<p>Include the source line number of each instruction in the output.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DISASM_SOURCE_FILE_NAME</p>
</td>
<td>
<p>Include the source file name in the output.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>OffsetLine</i> [out, optional]

<dd>
<p>Receives the line number in the output that contains the instruction at <i>Offset</i>.  If <i>OffsetLine</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>StartOffset</i> [out, optional]

<dd>
<p>Receives the location in the target's memory of the first instruction included in the output.  If <i>StartOffset</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>EndOffset</i> [out, optional]

<dd>
<p>Receives the locaiton in the target's memory of the instruction that follows the last disassembled instruction.</p>
</dd>

### -param <i>LineOffsets</i> [out, optional]

<dd>
<p>Receives the locations in the target's memory of the instructions included in the output starting with the instruction at <i>Offset</i>.  <i>LineOffsets</i> is an array that contains <i>TotalLines</i> elements.</p>
<p><i>Offset</i> is the value of first entry in this array unless there was an error disassembling the instructions before this instruction. In this case, the first entry will contain DEBUG_ANY_ID and <i>Offset</i> will be placed in the second entry in the array (index one).</p>
<p>If the output for an instruction spans multiple lines, the element in the array that corresponds to the first line of the instruction will contain the address of the instruction. </p>
<p>If <i>LineOffsets</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The assembly language depends on the effective processor type of the target system.  For information about the assembly language, see the processor documentation.</p>

<p>For an overview of using assembly in debugger applications, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540661">Debugging in Assembly Mode</a>.  For more information about using assembly with the debugger engine API, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538127">Assembling and Disassembling Instructions</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.disassemble">Disassemble</a>
</dt>
<dt>
<a href="debugger.outputdisassembly">OutputDisassembly</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/933a308c-61d1-4ca4-89c1-5749ba1b41c1">u (Unassemble)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::OutputDisassemblyLines method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

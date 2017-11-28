---
UID: NF.dbgeng.IDebugControl2.OutputDisassembly
title: IDebugControl2::OutputDisassembly
author: windows-driver-content
description: The OutputDisassembly method disassembles a processor instruction and sends the disassembly to the output callbacks.
old-location: debugger\outputdisassembly.htm
old-project: debugger
ms.assetid: 2a9944a4-3885-4e83-b20e-040cffcbf85b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, OutputDisassembly, IDebugControl2::OutputDisassembly
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
req.alt-api: IDebugControl.OutputDisassembly,IDebugControl2.OutputDisassembly,IDebugControl3.OutputDisassembly
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

# IDebugControl2::OutputDisassembly method



## -description
<p>The <b>OutputDisassembly</b> method disassembles a processor instruction and sends the disassembly to the <a href="debugger.using_input_and_output#output_callbacks#output_callbacks">output callbacks</a>.</p>


## -syntax

````
HRESULT OutputDisassembly(
  [in]  ULONG    OutputControl,
  [in]  ULONG64  Offset,
  [in]  ULONG    Flags,
  [out] PULONG64 EndOffset
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies the output control that determines which client's output callbacks receive the output.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.  For more information about output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's memory of the instruction to disassemble.</p>
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
<p>Compute the effective address from the current register information and display it.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DISASM_MATCHING_SYMBOLS</p>
</td>
<td>
<p>If the address of the instruction has an exact symbol match, output the symbol.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DISASM_SOURCE_LINE_NUMBER</p>
</td>
<td>
<p>Include the source line number of the instruction in the output.</p>
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

### -param <i>EndOffset</i> [out]

<dd>
<p>Receives the location in the target's memory of the instruction that follows the disassembled instruction.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541948">Disassemble</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553216">OutputDisassemblyLines</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::OutputDisassembly method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

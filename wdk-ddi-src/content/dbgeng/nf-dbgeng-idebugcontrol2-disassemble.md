---
UID: NF.dbgeng.IDebugControl2.Disassemble
title: IDebugControl2::Disassemble
author: windows-driver-content
description: The Disassemble method disassembles a processor instruction in the target's memory.
old-location: debugger\disassemble.htm
old-project: debugger
ms.assetid: a512c846-6896-48ca-a234-b9a30a3bff06
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl2, Disassemble, IDebugControl2::Disassemble
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
req.alt-api: IDebugControl.Disassemble,IDebugControl2.Disassemble,IDebugControl3.Disassemble
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

# IDebugControl2::Disassemble method



## -description
<p>The <b>Disassemble</b>  method disassembles a processor instruction in the target's memory.</p>


## -syntax

````
HRESULT Disassemble(
  [in]            ULONG64  Offset,
  [in]            ULONG    Flags,
  [out, optional] PSTR     Buffer,
  [in]            ULONG    BufferSize,
  [out, optional] PULONG   DisassemblySize,
  [out]           PULONG64 EndOffset
);
````


## -parameters
<dl>

### -param Offset [in]

<dd>
<p>Specifies the location in the target's memory of the instruction to disassemble.</p>
</dd>

### -param Flags [in]

<dd>
<p>Specifies the bit-flags that affect the behavior of this method.  Currently the only flag that can be set is DEBUG_DISASM_EFFECTIVE_ADDRESS; when set, the engine will compute the effective address from the current register information and display it.</p>
</dd>

### -param Buffer [out, optional]

<dd>
<p>Receives the disassembled instruction.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size, in characters, of the <i>Buffer</i> buffer.</p>
</dd>

### -param DisassemblySize [out, optional]

<dd>
<p>Receives the size, in characters, of the disassembled instruction.  If <i>DisassemblySize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param EndOffset [out]

<dd>
<p>Receives the location in the target's memory of the instruction following the disassembled instruction.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, <i>Buffer</i> was too small to hold the disassembled instruction and the instruction was truncated to fit.</p>

<p> </p>

## -remarks
<p>The assembly language depends on the effective processor type of the target system.  For information about the assembly language, see the processor documentation.</p>

<p>The disassembly options--returned by <a href="debugger.getassemblyoptions">GetAssemblyOptions</a>--affect the operation of this method.</p>

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
<a href="debugger.assemble">Assemble</a>
</dt>
<dt>
<a href="debugger.getassemblyoptions">GetAssemblyOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/933a308c-61d1-4ca4-89c1-5749ba1b41c1">u (Unassemble)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::Disassemble method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

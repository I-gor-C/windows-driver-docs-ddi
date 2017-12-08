---
UID: NF.dbgeng.IDebugControl.Assemble
title: IDebugControl::Assemble
author: windows-driver-content
description: The Assemble method assembles a single processor instruction. The assembled instruction is placed in the target's memory.
old-location: debugger\assemble.htm
old-project: debugger
ms.assetid: 4d7d84e7-4fa4-4514-9d52-dbae5fed159b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl, Assemble, IDebugControl::Assemble
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
req.alt-api: IDebugControl.Assemble,IDebugControl2.Assemble,IDebugControl3.Assemble
req.alt-loc: Dbgeng.h
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
req.iface: IDebugControl
---

# IDebugControl::Assemble method



## -description
<p>The <b>Assemble</b> method assembles a single processor instruction.  The assembled instruction is placed in the target's memory.</p>


## -syntax

````
HRESULT Assemble(
  [in]  ULONG64  Offset,
  [in]  PCSTR    Instr,
  [out] PULONG64 EndOffset
);
````


## -parameters
<dl>

### -param Offset [in]

<dd>
<p>Specifies the location in the target's memory to place the assembled instruction.</p>
</dd>

### -param Instr [in]

<dd>
<p>Specifies the instruction to assemble.  The instruction is assembled according to the target's effective processor type (returned by <a href="debugger.seteffectiveprocessortype">SetEffectiveProcessorType</a>).</p>
</dd>

### -param EndOffset [out]

<dd>
<p>Receives the location in the target's memory immediately following the assembled instruction.  <i>EndOffset</i> can be used when assembling multiple instructions.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>The assembly language depends on the effective processor type of the target machine.  For information about the assembly language, see the processor documentation.</p>

<p>The assembly language options--returned by <a href="debugger.getassemblyoptions">GetAssemblyOptions</a>--affect the operation of this method.</p>

<p>For an overview of using assembly in debugger applications, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540661">Debugging in Assembly Mode</a>.  For more information about using assembly with the <a href="debugger.d#debugger_engine_api#debugger_engine_api"><i>debugger engine API</i></a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538127">Assembling and Disassembling Instructions</a>.</p>

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
<a href="debugger.getassemblyoptions">GetAssemblyOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::Assemble method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

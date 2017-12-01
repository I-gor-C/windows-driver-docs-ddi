---
UID: NF.dbgeng.IDebugControl3.AddAssemblyOptions
title: IDebugControl3::AddAssemblyOptions
author: windows-driver-content
description: The AddAssemblyOptions method turns on some of the assembly and disassembly options.
old-location: debugger\addassemblyoptions.htm
old-project: debugger
ms.assetid: 9274c3eb-a5c0-43a9-a9d4-541482ddace1
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl3, AddAssemblyOptions, IDebugControl3::AddAssemblyOptions
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
req.alt-api: IDebugControl3.AddAssemblyOptions
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
req.iface: IDebugControl3
---

# IDebugControl3::AddAssemblyOptions method



## -description
<p>The <b>AddAssemblyOptions</b> method turns on some of the assembly and disassembly options.</p>


## -syntax

````
HRESULT AddAssemblyOptions(
  [in] ULONG Options
);
````


## -parameters
<dl>

### -param <i>Options</i> [in]

<dd>
<p>Specifies the assembly and disassembly options to turn on.  <i>Options</i> is a bit-set that will be combined with the existing engine options using the bitwise OR operator.  For a description of the options, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541443">DEBUG_ASMOPT_XXX</a>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>These methods can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>For more information about using assembly with the <a href="debugger.d#debugger_engine_api#debugger_engine_api"><i>debugger engine API</i></a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538127">Assembling and Disassembling Instructions</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.removeassemblyoptions">RemoveAssemblyOptions</a>
</dt>
<dt>
<a href="debugger.setassemblyoptions">SetAssemblyOptions</a>
</dt>
<dt>
<a href="debugger.getassemblyoptions">GetAssemblyOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541443">DEBUG_ASMOPT_XXX</a>
</dt>
<dt>
<a href="debugger.assemble">Assemble</a>
</dt>
<dt>
<a href="debugger.disassemble">Disassemble</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562128">.asm (Change Disassembly Options)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl3::AddAssemblyOptions method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

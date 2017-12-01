---
UID: NF.dbgeng.IDebugControl3.GetTextMacro
title: IDebugControl3::GetTextMacro
author: windows-driver-content
description: The GetTextMacro method returns the value of a fixed-name alias.
old-location: debugger\gettextmacro.htm
old-project: debugger
ms.assetid: 980bcf7b-8e4a-4516-ab71-af60a1d8e99c
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl3, GetTextMacro, IDebugControl3::GetTextMacro
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
req.alt-api: IDebugControl.GetTextMacro,IDebugControl2.GetTextMacro,IDebugControl3.GetTextMacro
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
req.iface: IDebugControl3
---

# IDebugControl3::GetTextMacro method



## -description
<p>The <b>GetTextMacro</b> method returns the value of a fixed-name alias.</p>


## -syntax

````
HRESULT GetTextMacro(
  [in]            ULONG  Slot,
  [out, optional] PSTR   Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG MacroSize
);
````


## -parameters
<dl>

### -param <i>Slot</i> [in]

<dd>
<p>Specifies the number of the fixed-name alias.  <i>Slot</i> can take the values 0, 1, ..., 9, that represent the fixed-name aliases <b>$u0</b>, <b>$u1</b>, ..., <b>$u9</b>.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the value of the alias specified by <i>Slot</i>.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the <i>Buffer</i> buffer.</p>
</dd>

### -param <i>MacroSize</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the value of the alias.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Before executing commands or evaluating expressions, the debugger engine will replace the alias specified by <i>Slot</i> with the value of the alias (returned to the <i>Buffer</i> buffer).</p>

<p>For an overview of aliases used by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560047">Using Aliases</a>.  For more information about using aliases with the debugger engine API, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551041">Interacting with the Engine</a>.</p>

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
<a href="debugger.settextmacro">SetTextMacro</a>
</dt>
<dt>
<a href="debugger.gettextreplacement">GetTextReplacement</a>
</dt>
<dt>
<a href="debugger.getnumbertextreplacements">GetNumberTextReplacements</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554663">r (Registers)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetTextMacro method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

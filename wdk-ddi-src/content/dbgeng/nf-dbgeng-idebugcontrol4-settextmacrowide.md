---
UID: NF.dbgeng.IDebugControl4.SetTextMacroWide
title: IDebugControl4::SetTextMacroWide
author: windows-driver-content
description: The SetTextMacroWide method sets the value of a fixed-name alias.
old-location: debugger\settextmacrowide.htm
old-project: debugger
ms.assetid: 98e93636-33e3-4642-a4fb-8590a7a0e784
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl4, SetTextMacroWide, IDebugControl4::SetTextMacroWide
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
req.alt-api: IDebugControl4.SetTextMacroWide
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
req.iface: IDebugControl4
---

# IDebugControl4::SetTextMacroWide method



## -description
<p>The <b>SetTextMacroWide</b>  method sets the value of a fixed-name alias.</p>


## -syntax

````
HRESULT SetTextMacroWide(
  [in] ULONG  Slot,
  [in] PCWSTR Macro
);
````


## -parameters
<dl>

### -param Slot [in]

<dd>
<p>Specifies the number of the fixed-name alias.  <i>Slot</i> can take the values 0, 1, ..., 9, that represent the fixed-name aliases <b>$u0</b>, <b>$u1</b>, ..., <b>$u9</b>.</p>
</dd>

### -param Macro [in]

<dd>
<p>Specifies the new value of the alias specified by <i>Slot</i>.  The <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> makes a copy of this string.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Before executing commands or evaluating expressions, the debugger engine will replace the alias specified by <i>Slot</i> with the value of the alias (specified by <i>Macro</i>).</p>

<p>For an overview of aliases used by the debugger engine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560047">Using Aliases</a>.  For more information about using aliases with the debugger engine API, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551041">Interacting with the Engine</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>
</dt>
<dt>
<a href="debugger.gettextmacro">GetTextMacro</a>
</dt>
<dt>
<a href="debugger.settextreplacement">SetTextReplacement</a>
</dt>
<dt>
<a href="debugger.removetextreplacements">RemoveTextReplacements</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554663">r (Registers)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::SetTextMacroWide method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

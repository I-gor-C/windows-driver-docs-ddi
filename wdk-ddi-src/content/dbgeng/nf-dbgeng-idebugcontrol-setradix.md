---
UID: NF.dbgeng.IDebugControl.SetRadix
title: IDebugControl::SetRadix
author: windows-driver-content
description: The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.
old-location: debugger\setradix.htm
old-project: debugger
ms.assetid: 7346733d-2ac7-4eee-9f9c-ea6e1ee2ce5d
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl, SetRadix, IDebugControl::SetRadix
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
req.alt-api: IDebugControl.SetRadix,IDebugControl2.SetRadix,IDebugControl3.SetRadix
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
req.iface: IDebugControl
---

# IDebugControl::SetRadix method



## -description
<p>The <b>SetRadix</b> method sets the default radix (number base) used by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> when it evaluates and displays MASM expressions, and when it displays symbol information.</p>


## -syntax

````
HRESULT SetRadix(
  [in] ULONG Radix
);
````


## -parameters
<dl>

### -param <i>Radix</i> [in]

<dd>
<p>Specifies the new default radix.  The following table contains the possible values for the radix.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>8</p>
</td>
<td>
<p>Octal</p>
</td>
</tr>
<tr>
<td>
<p>10</p>
</td>
<td>
<p>Decimal</p>
</td>
</tr>
<tr>
<td>
<p>16</p>
</td>
<td>
<p>Hexadecimal</p>
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
<p>When the radix is changed, the engine notifies the event callbacks by passing the DEBUG_CES_RADIX flag to the <a href="debugger.idebugeventcallbacks_changeenginestate">IDebugEventCallbacks::ChangeEngineState</a> callback method.</p>

<p>For more information about the default radix, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560116">Using Input and Output</a>.</p>

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
<a href="debugger.getradix">GetRadix</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552287">n (Set Number Base)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetRadix method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

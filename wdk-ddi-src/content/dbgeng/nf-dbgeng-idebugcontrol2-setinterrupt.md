---
UID: NF.dbgeng.IDebugControl2.SetInterrupt
title: IDebugControl2::SetInterrupt
author: windows-driver-content
description: The SetInterrupt method registers a user interrupt or breaks into the debugger.
old-location: debugger\setinterrupt.htm
old-project: debugger
ms.assetid: d67119c7-ecbe-446c-8a4f-38d33e92a277
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, SetInterrupt, IDebugControl2::SetInterrupt
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
req.alt-api: IDebugControl.SetInterrupt,IDebugControl2.SetInterrupt,IDebugControl3.SetInterrupt
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

# IDebugControl2::SetInterrupt method



## -description
<p>The <b>SetInterrupt</b> method registers a user interrupt or breaks into the debugger.</p>


## -syntax

````
HRESULT SetInterrupt(
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies the type of interrupt to register.  <i>Flags</i> can take one of the values listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_INTERRUPT_ACTIVE</p>
</td>
<td>
<p>If the target is running, the engine will request a break into the debugger.  This request might time out. For more information, see the "Remarks" section.</p>
<p>Otherwise, when the target is suspended, the engine will register a user interrupt.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_INTERRUPT_PASSIVE</p>
</td>
<td>
<p>The engine will register a user interrupt.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_INTERRUPT_EXIT</p>
</td>
<td>
<p>If there is currently a <a href="debugger.waitforevent">WaitForEvent</a> call running, the engine will force it to return.  If there are any debugger commands causing execution in the target -- for example, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549693">g (Go)</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553496">p (Step)</a> -- the engine will force them to complete.  This does not force a break into the debugger, so the target might not be suspended. In which case, the <b>WaitForEvent</b> call will return E_PENDING.</p>
<p>Otherwise, when the target is suspended, register a user interrupt.</p>
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
<p>This method can be called at any time and from any thread.  Once the interrupt has been registered, this method returns immediately.</p>

<p>If <i>Flags</i> is DEBUG_INTERRUPT_ACTIVE, and the interrupt times out, the engine will generate a synthetic exception event.  This event will be sent to event callback's <a href="debugger.idebugeventcallbacks_exception">IDebugEventCallbacks::Exception</a> method.  The amount of time before the interrupt times out can be set using <a href="debugger.setinterrupttimeout">SetInterruptTimeout</a>.</p>

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
<a href="debugger.getinterrupt">GetInterrupt</a>
</dt>
<dt>
<a href="debugger.getinterrupttimeout">GetInterruptTimeout</a>
</dt>
<dt>
<a href="debugger.setinterrupttimeout">SetInterruptTimeout</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetInterrupt method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

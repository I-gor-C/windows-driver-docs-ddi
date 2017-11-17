---
UID: NF.dbgeng.IDebugControl3.WaitForEvent
title: IDebugControl3::WaitForEvent
author: windows-driver-content
description: The WaitForEvent method waits for an event that breaks into the debugger engine application.
old-location: debugger\waitforevent.htm
ms.assetid: b7038bcf-2469-4d5f-ac73-0c7835da23c3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h, Winbase.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.WaitForEvent,IDebugControl2.WaitForEvent,IDebugControl3.WaitForEvent
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
ms.keywords: IDebugControl3, WaitForEvent, IDebugControl3::WaitForEvent
req.iface: IDebugControl3
---

# IDebugControl3::WaitForEvent method



## -description
<p>    The <b>WaitForEvent</b> method waits for an event that breaks into the debugger engine application.</p>


## -syntax

````
HRESULT WaitForEvent(
  [in] ULONG Flags,
  [in] ULONG Timeout
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Set to zero.  There are currently no flags that can be used in this parameter.</p>
</dd>

### -param <i>Timeout</i> [in]

<dd>
<p>Specifies how many milliseconds to wait before this method will return.  If <i>Timeout</i> is INFINITE, this method will not return until an event that breaks into the debugger engine application occurs or an exit interrupt is issued.  If the current session has a live kernel target, <i>Timeout</i> must be set to INFINITE.</p>
</dd>
</dl>

## -returns
<p>This method may return other error values and the above error values may have additional meanings.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The time-out expired.</p><dl>
<dt><b>E_PENDING</b></dt>
</dl><p>An exit interrupt was issued.  The target is not available.</p><dl>
<dt><b>E_UNEXPECTED</b></dt>
</dl><p>Either there is an outstanding request for input, or none of the targets could generate events.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The engine is already waiting for an event.</p>

<p> </p>

## -remarks
<p>The method can be called only from the thread that started the debugger session.</p>

<p>When an event occurs, the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> will process the event and call the event callbacks. If one of these callbacks indicates that the event should break into the debugger engine application (by returning DEBUG_STATUS_BREAK), this method will return; otherwise, it will continue waiting for an event.  The event filters can also specify that an event should break into the debugger engine application.  For more information about event filters, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539287">Controlling Exceptions and Events</a>.</p>

<p>This method is not re-entrant.  Once it has been called, it cannot be called again on any client until it has returned.  In particular, it cannot be called from the event callbacks, including extensions and commands executed by the callbacks.</p>

<p>If none of the targets are capable of generating events -- for example, all the targets have exited -- this method will end the current session, discard the targets, and then return E_UNEXPECTED.</p>

<p>The constant INFINITE is defined in Winbase.h.</p>

<p>For more information about using <b>WaitForEvent</b> to control the execution flow of the debugger application and targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>. For details on the event callbacks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

<p>The method can be called only from the thread that started the debugger session.</p>

<p>When an event occurs, the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> will process the event and call the event callbacks. If one of these callbacks indicates that the event should break into the debugger engine application (by returning DEBUG_STATUS_BREAK), this method will return; otherwise, it will continue waiting for an event.  The event filters can also specify that an event should break into the debugger engine application.  For more information about event filters, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539287">Controlling Exceptions and Events</a>.</p>

<p>This method is not re-entrant.  Once it has been called, it cannot be called again on any client until it has returned.  In particular, it cannot be called from the event callbacks, including extensions and commands executed by the callbacks.</p>

<p>If none of the targets are capable of generating events -- for example, all the targets have exited -- this method will end the current session, discard the targets, and then return E_UNEXPECTED.</p>

<p>The constant INFINITE is defined in Winbase.h.</p>

<p>For more information about using <b>WaitForEvent</b> to control the execution flow of the debugger application and targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>. For details on the event callbacks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

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
<dt>Dbgeng.h (include Dbgeng.h or Winbase.h)</dt>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::WaitForEvent method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

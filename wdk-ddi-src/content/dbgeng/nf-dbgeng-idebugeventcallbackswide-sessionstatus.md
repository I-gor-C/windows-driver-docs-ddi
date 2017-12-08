---
UID: NF.dbgeng.IDebugEventCallbacksWide.SessionStatus
title: IDebugEventCallbacksWide::SessionStatus
author: windows-driver-content
description: The SessionStatus callback method is called by the engine when a change occurs in the debugger session.
old-location: debugger\idebugeventcallbackswide_sessionstatus.htm
old-project: debugger
ms.assetid: cc3ed4ef-5e2d-4865-8d6f-b140d6b5d7af
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugEventCallbacksWide, SessionStatus, IDebugEventCallbacksWide::SessionStatus
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
req.alt-api: IDebugEventCallbacksWide.SessionStatus
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
req.iface: IDebugEventCallbacksWide
---

# IDebugEventCallbacksWide::SessionStatus method



## -description
<p>The <b>SessionStatus</b> callback method is called by the engine when a change occurs in the debugger session.</p>


## -syntax

````
HRESULT SessionStatus(
  [in] ULONG Status
);
````


## -parameters
<dl>

### -param Status [in]

<dd>
<p>Specifies the new status of the debugger session.  The following table describes the possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_ACTIVE</p>
</td>
<td>
<p>A debugger session has started.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_END_SESSION_ACTIVE_TERMINATE</p>
</td>
<td>
<p>The session was ended by sending DEBUG_END_ACTIVE_TERMINATE to <a href="debugger.endsession">EndSession</a>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_END_SESSION_ACTIVE_DETACH</p>
</td>
<td>
<p>The session was ended by sending DEBUG_END_ACTIVE_DETACH to <b>EndSession</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_END_SESSION_PASSIVE</p>
</td>
<td>
<p>The session was ended by sending DEBUG_END_PASSIVE to <b>EndSession</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_END</p>
</td>
<td>
<p>The  target ran to completion, ending the session.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_REBOOT</p>
</td>
<td>
<p>The  target computer rebooted, ending the session.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_HIBERNATE</p>
</td>
<td>
<p>The  target computer went into hibernation, ending the session.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SESSION_FAILURE</p>
</td>
<td>
<p>The engine was unable to continue the session.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method's return value is ignored by the engine.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_SESSION_STATUS flag is set in the mask returned by <a href="debugger.idebugeventcallbackswide_getinterestmask">IDebugEventCallbacksWide::GetInterestMask</a>.</p>

<p>After the engine has notified all the event callbacks of the change in the session status, it will also notify any loaded <a href="debugger.introduction#extensions#extensions">extensions</a> that export the <a href="debugger.debugextensionnotify">DebugExtensionNotify</a> callback method.  The value that it passes to the extensions depends on the value of <i>Status</i>.  If <i>Status</i> is DEBUG_SESSION_ACTIVE, it passes DEBUG_SESSION_ACTIVE; otherwise, it passes DEBUG_SESSION_INACTIVE.</p>

<p>In the DEBUG_SESSION_ACTIVE case, the engine follows the debugger session change notification with a target state change notification by calling <a href="debugger.idebugeventcallbackswide_changedebuggeestate">IDebugEventCallbacksWide::ChangeDebuggeeState</a> on the event callbacks and passing DEBUG_CDS_ALL in the <i>Flags</i> parameter.  In all other cases, the engine precedes this notification with an engine state change notification by calling <a href="debugger.idebugeventcallbackswide_changeenginestate">IDebugEventCallbacksWide::ChangeEngineState</a> on the event callbacks and passing DEBUG_CES_EXECUTION_STATUS in the <i>Flags</i> parameter.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.  For information about debugger sessions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>.</p>

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
---
UID: NF.dbgeng.IDebugClient4.EndSession
title: IDebugClient4::EndSession
author: windows-driver-content
description: The EndSession method ends the current debugger session.
old-location: debugger\endsession.htm
old-project: debugger
ms.assetid: 521a0e4a-99c6-4ad4-886d-3fff9855e1fd
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient4, EndSession, IDebugClient4::EndSession
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
req.alt-api: IDebugClient.EndSession,IDebugClient2.EndSession,IDebugClient3.EndSession,IDebugClient4.EndSession,IDebugClient5.EndSession
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
req.iface: IDebugClient4
---

# IDebugClient4::EndSession method



## -description
<p>The <b>EndSession</b> method ends the current debugger session.</p>


## -syntax

````
HRESULT EndSession(
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies how to end the session.  <i>Flags</i> can be one of the following values:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_END_PASSIVE</p>
</td>
<td>
<p>Perform cleanup for the session.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_END_ACTIVE_TERMINATE</p>
</td>
<td>
<p>Attempt to terminate all user-mode targets before performing cleanup for the session.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_END_ACTIVE_DETACH</p>
</td>
<td>
<p>Attempt to disconnect from all targets before performing cleanup for the session.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_END_REENTRANT</p>
</td>
<td>
<p>Perform only the cleanup that doesn't require acquiring locks.  See Remarks section for details.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_END_DISCONNECT</p>
</td>
<td>
<p>Do not end the session.  Disconnect the client from the session and disable the client.</p>
<p>This flag is intended for when remote clients disconnect.  It generates a server message about the disconnection.</p>
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
<p>This method may be called at any time with <i>Flags</i> set to DEBUG_END_REENTRANT.  If, for example, the application needs to exit but another thread is using the engine, this method can be used to perform as much cleanup as possible.</p>

<p>Using DEBUG_END_REENTRANT may leave the engine in an indeterminate state. If this flag is used, no subsequent calls should be made to the engine.</p>

<p>For more information about debugger sessions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>.</p>

<p>This method may be called at any time with <i>Flags</i> set to DEBUG_END_REENTRANT.  If, for example, the application needs to exit but another thread is using the engine, this method can be used to perform as much cleanup as possible.</p>

<p>Using DEBUG_END_REENTRANT may leave the engine in an indeterminate state. If this flag is used, no subsequent calls should be made to the engine.</p>

<p>For more information about debugger sessions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>.</p>

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
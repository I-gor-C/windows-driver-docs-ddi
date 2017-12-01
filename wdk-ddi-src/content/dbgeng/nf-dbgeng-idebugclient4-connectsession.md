---
UID: NF.dbgeng.IDebugClient4.ConnectSession
title: IDebugClient4::ConnectSession
author: windows-driver-content
description: The ConnectSession method joins the client to an existing debugger session.
old-location: debugger\connectsession.htm
old-project: debugger
ms.assetid: 4531bf2f-ef3b-4d4f-b922-3a01a9468ac9
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient4, ConnectSession, IDebugClient4::ConnectSession
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
req.alt-api: IDebugClient.ConnectSession,IDebugClient2.ConnectSession,IDebugClient3.ConnectSession,IDebugClient4.ConnectSession,IDebugClient5.ConnectSession
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

# IDebugClient4::ConnectSession method



## -description
<p>The <b>ConnectSession</b> method joins the client to an existing debugger session.</p>


## -syntax

````
HRESULT ConnectSession(
  [in] ULONG Flags,
  [in] ULONG HistoryLimit
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-set of option flags for connecting to the session.  The possible values of these flags are:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_CONNECT_SESSION_NO_VERSION</p>
</td>
<td>
<p>Do not output the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>'s version to this client.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CONNECT_SESSION_NO_ANNOUNCE</p>
</td>
<td>
<p>Do not output a message notifying other clients that this client has connected.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>HistoryLimit</i> [in]

<dd>
<p>Specifies the maximum number of characters from the session's history to send to this client's output upon connection.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>When the client object connects to a session, the most recent output from the session is sent to the client.  If the session is currently waiting on input, the client object is given the opportunity to provide input.  Thus, the client object synchronizes with the session's input and output.</p>

<p>The client becomes a primary client and will appear among the list of clients in the output of the <a href="https://msdn.microsoft.com/a5f760d7-f454-49c5-853d-bcb545c0b05e">.clients</a> debugger command.</p>

<p>For more information about debugging clients, see Debugging Server and Debugging Client.  For more information about debugger sessions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient.md">IDebugClient</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="..\dbgeng\nf-dbgeng-debugconnect.md">DebugConnect</a>
</dt>
<dt>
<a href="debugger.startserver">StartServer</a>
</dt>
<dt>
<a href="debugger.outputservers">OutputServers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::ConnectSession method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

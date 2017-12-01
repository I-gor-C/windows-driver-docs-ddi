---
UID: NF.dbgeng.IDebugClient.StartProcessServer
title: IDebugClient::StartProcessServer
author: windows-driver-content
description: The StartProcessServer method starts a process server.
old-location: debugger\startprocessserver.htm
old-project: debugger
ms.assetid: dc0bade2-7781-4c08-aea5-0ff4809d3321
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient, StartProcessServer, IDebugClient::StartProcessServer
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
req.alt-api: IDebugClient.StartProcessServer,IDebugClient2.StartProcessServer,IDebugClient3.StartProcessServer,IDebugClient4.StartProcessServer,IDebugClient5.StartProcessServer
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
req.iface: IDebugClient
---

# IDebugClient::StartProcessServer method



## -description
<p>The <b>StartProcessServer</b> method starts a process server.</p>


## -syntax

````
HRESULT StartProcessServer(
  [in]           ULONG Flags,
  [in]           PCSTR Options,
  [in, optional] PVOID Reserved
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies the class of the targets that will be available through the process server.  This must be set to DEBUG_CLASS_USER_WINDOWS.</p>
</dd>

### -param <i>Options</i> [in]

<dd>
<p>Specifies the connections options for this process server.  These are the same options given to the <b>-t</b> option of the DbgSrv command line.  For details on the syntax of this string, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537832">Activating a Process Server</a>.</p>
</dd>

### -param <i>Reserved</i> [in, optional]

<dd>
<p>Set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The process server that is started will be accessible by remote clients through the transport specified in the <i>Options</i> parameter.</p>

<p>To stop the process server from the smart client, use the <a href="debugger.endprocessserver">EndProcessServer</a> method. To shut down the process server from the computer that it is running on, use Task Manager to end the process. If the instance of the debugger engine that used <b>StartProcessServer</b> is still running, it can use <a href="debugger.execute">Execute</a> to issue the debugger command <a href="https://msdn.microsoft.com/6be6c774-fe6b-4bd4-8174-55ef207db3e6">.endsrv 0</a>, which will end the process server (this is an exception to the usual behavior of <b>.endsrv</b>, which generally does not affect process servers). </p>

<p>For more information about process servers and remote debugging, see <a href="debugger.remote_targets#process_server_and_smart_client#process_server_and_smart_client">Process Servers, Kernel Connection Servers, and Smart Clients</a>.</p>

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
<a href="debugger.waitforprocessserverend">WaitForProcessServerEnd</a>
</dt>
<dt>
<a href="debugger.connectprocessserver">ConnectProcessServer</a>
</dt>
<dt>
<a href="debugger.endprocessserver">EndProcessServer</a>
</dt>
<dt>
<a href="debugger.disconnectprocessserver">DisconnectProcessServer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::StartProcessServer method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

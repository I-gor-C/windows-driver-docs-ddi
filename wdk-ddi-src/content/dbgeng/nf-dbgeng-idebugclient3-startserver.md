---
UID: NF.dbgeng.IDebugClient3.StartServer
title: IDebugClient3::StartServer
author: windows-driver-content
description: The StartServer method starts a debugging server.
old-location: debugger\startserver.htm
old-project: debugger
ms.assetid: 52b1c590-a62b-4e27-a267-1862cb76e6d4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient3, StartServer, IDebugClient3::StartServer
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
req.alt-api: IDebugClient.StartServer,IDebugClient2.StartServer,IDebugClient3.StartServer,IDebugClient4.StartServer,IDebugClient5.StartServer
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
req.iface: IDebugClient3
---

# IDebugClient3::StartServer method



## -description
<p>The <b>StartServer</b>  method starts a debugging server.</p>


## -syntax

````
HRESULT StartServer(
  [in] PCSTR Options
);
````


## -parameters
<dl>

### -param <i>Options</i> [in]

<dd>
<p>Specifies the connections options for this server.  These are the same options given to the <b>.server</b> debugger command or the WinDbg and CDB <b>-server</b> command-line option.  For details on the syntax of this string, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537823">Activating a Debugging Server</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The server that is started will be accessible by other <a href="https://msdn.microsoft.com/13F9D82A-4C04-425A-A063-B349DB5C8E08">debuggers</a> through the transport specified in the <i>Options</i> parameter.</p>

<p>For more information about debugging servers, see Debugging Server and Debugging Client.</p>

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
<a href="debugger.startprocessserver">StartProcessServer</a>
</dt>
<dt>
<a href="debugger.outputservers">OutputServers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::StartServer method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

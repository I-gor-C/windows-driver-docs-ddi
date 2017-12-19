---
UID: NF.dbgeng.IDebugClient5.ConnectProcessServerWide
title: IDebugClient5::ConnectProcessServerWide method
author: windows-driver-content
description: The ConnectProcessServerWide method connects to a process server.
old-location: debugger\connectprocessserverwide.htm
old-project: Debugger
ms.assetid: 42979da6-d044-4d52-858f-98871c3941bc
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugClient5, IDebugClient5::ConnectProcessServerWide, ConnectProcessServerWide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient5.ConnectProcessServerWide
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
---

# IDebugClient5::ConnectProcessServerWide method



## -description
The <b>ConnectProcessServerWide</b> method connects to a <a href="debugger.p#process_server#process_server"><i>process server</i></a>.



## -syntax

````
HRESULT ConnectProcessServerWide(
  [in]  PCWSTR   RemoteOptions,
  [out] PULONG64 Server
);
````


## -parameters

### -param RemoteOptions [in]

Specifies how the <a href="debugger.d#debugger_engine#debugger_engine"><i>debugger engine</i></a> will connect with the process server.  These are the same options passed to the <b>-premote</b> option on the WinDbg and CDB command lines.  For details on the syntax of this string, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537840">Activating a Smart Client</a>.


### -param Server [out]

Receives a handle for the process server.  This handle is used when creating or attaching to processes by using the process server.


## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
For more information about process servers and remote debugging, see <a href="debugger.remote_targets#process_server_and_smart_client#process_server_and_smart_client">Process Servers, Kernel Connection Servers, and Smart Clients</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.startprocessserver">StartProcessServer</a>
</dt>
<dt>
<a href="debugger.disconnectprocessserver">DisconnectProcessServer</a>
</dt>
<dt>
<a href="debugger.endprocessserver">EndProcessServer</a>
</dt>
<dt>
<a href="debugger.attachprocess">AttachProcess</a>
</dt>
<dt>
<a href="debugger.createprocess2">CreateProcess2</a>
</dt>
<dt>
<a href="debugger.createprocessandattach2">CreateProcessAndAttach2</a>
</dt>
<dt>
<a href="debugger.getrunningprocessdescription">GetRunningProcessDescription</a>
</dt>
<dt>
<a href="debugger.getrunningprocesssystemidbyexecutablename">GetRunningProcessSystemIdByExecutableName</a>
</dt>
<dt>
<a href="debugger.getrunningprocesssystemids">GetRunningProcessSystemIds</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugClient5::ConnectProcessServerWide method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


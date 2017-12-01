---
UID: NF.dbgeng.IDebugClient5.OutputServers
title: IDebugClient5::OutputServers
author: windows-driver-content
description: The OutputServers method lists the servers running on a given computer.
old-location: debugger\outputservers.htm
old-project: debugger
ms.assetid: cb08e0d9-8c4b-4b7f-be3d-4e7c87d7f3d4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient5, OutputServers, IDebugClient5::OutputServers
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
req.alt-api: IDebugClient.OutputServers,IDebugClient2.OutputServers,IDebugClient3.OutputServers,IDebugClient4.OutputServers,IDebugClient5.OutputServers
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
req.iface: IDebugClient5
---

# IDebugClient5::OutputServers method



## -description
<p>The <b>OutputServers</b>  method lists the servers running on a given computer.</p>


## -syntax

````
HRESULT OutputServers(
  [in] ULONG OutputControl,
  [in] PCSTR Machine,
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies the output control to use while outputting the servers. For possible values, see <a href="debugger.debug_outctl_xxx">DEBUG_OUTCTL_XXX</a>.</p>
</dd>

### -param <i>Machine</i> [in]

<dd>
<p>Specifies the name of the computer whose servers will be listed.  <i>Machine</i> has the following form:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>\\computername</pre>
</td>
</tr>
</table></span></div>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-set that determines which servers to output.  The possible bit flags are:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_SERVERS_DEBUGGER</p>
</td>
<td>
<p>Output the debugging servers on the computer.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SERVERS_PROCESS</p>
</td>
<td>
<p>Output the process servers on the computer.</p>
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
<p>For more information about remote debugging, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554401">Remote Debugging</a>.</p>

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
<a href="debugger.startserver">StartServer</a>
</dt>
<dt>
<a href="..\dbgeng\nf-dbgeng-debugconnect.md">DebugConnect</a>
</dt>
<dt>
<a href="debugger.startprocessserver">StartProcessServer</a>
</dt>
<dt>
<a href="debugger.connectprocessserver">ConnectProcessServer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::OutputServers method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

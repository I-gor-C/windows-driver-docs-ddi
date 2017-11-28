---
UID: NF.dbgeng.IDebugClient3.WaitForProcessServerEnd
title: IDebugClient3::WaitForProcessServerEnd
author: windows-driver-content
description: The WaitForProcessServerEnd method waits for a local process server to exit.
old-location: debugger\waitforprocessserverend.htm
old-project: debugger
ms.assetid: 19573307-0192-47bd-86a0-9c7721d16c5e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient3, WaitForProcessServerEnd, IDebugClient3::WaitForProcessServerEnd
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h, Winbase.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient2.WaitForProcessServerEnd,IDebugClient3.WaitForProcessServerEnd,IDebugClient4.WaitForProcessServerEnd,IDebugClient5.WaitForProcessServerEnd
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

# IDebugClient3::WaitForProcessServerEnd method



## -description
<p>The <b>WaitForProcessServerEnd</b> method waits for a local process server to exit.</p>


## -syntax

````
HRESULT WaitForProcessServerEnd(
  [in] ULONG Timeout
);
````


## -parameters
<dl>

### -param <i>Timeout</i> [in]

<dd>
<p>Specifies how long in milliseconds to wait for a process server to exit.  If <i>Timeout</i> is INFINITE, this method will not return until a process server has ended.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>A time-out occurred -- <i>Timeout</i> milliseconds passed without a local process server exiting.</p>

<p> </p>

## -remarks
<p>This method will only wait for the first local process server to end.  After a process server has ended, subsequent calls to this method will return immediately.</p>

<p>For more information about process servers and remote debugging, see <a href="debugger.remote_targets#process_server_and_smart_client#process_server_and_smart_client">Process Servers, Kernel Connection Servers, and Smart Clients</a>.</p>

<p>The constant INFINITE is defined in Winbase.h.</p>

<p>This method will only wait for the first local process server to end.  After a process server has ended, subsequent calls to this method will return immediately.</p>

<p>For more information about process servers and remote debugging, see <a href="debugger.remote_targets#process_server_and_smart_client#process_server_and_smart_client">Process Servers, Kernel Connection Servers, and Smart Clients</a>.</p>

<p>The constant INFINITE is defined in Winbase.h.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550481">IDebugClient2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550488">IDebugClient3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558810">StartProcessServer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542993">EndProcessServer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient2::WaitForProcessServerEnd method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

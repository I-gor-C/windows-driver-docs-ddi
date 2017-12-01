---
UID: NF.dbgeng.IDebugSystemObjects2.GetEventThread
title: IDebugSystemObjects2::GetEventThread
author: windows-driver-content
description: The GetEventThread method returns the engine thread ID for the thread on which the last event occurred.
old-location: debugger\geteventthread.htm
old-project: debugger
ms.assetid: 7a28c9bd-480e-4864-b7ff-9ff0dc1d04ad
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects2, GetEventThread, IDebugSystemObjects2::GetEventThread
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
req.alt-api: IDebugSystemObjects.GetEventThread,IDebugSystemObjects2.GetEventThread,IDebugSystemObjects3.GetEventThread,IDebugSystemObjects4.GetEventThread
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
req.iface: IDebugSystemObjects2
---

# IDebugSystemObjects2::GetEventThread method



## -description
<p>The <b>GetEventThread</b> method returns the engine thread ID for the thread on which the last event occurred.</p>


## -syntax

````
HRESULT GetEventThread(
  [out] PULONG Id
);
````


## -parameters
<dl>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine thread ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, the engine thread ID for the virtual thread representing the processor on which the event occurred is returned.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details about debugger engine events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

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
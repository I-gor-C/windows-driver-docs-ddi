---
UID: NF.dbgeng.IDebugEventCallbacks.ExitThread
title: IDebugEventCallbacks::ExitThread
author: windows-driver-content
description: The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target.
old-location: debugger\idebugeventcallbacks_exitthread.htm
old-project: debugger
ms.assetid: 03ff46cb-dfc5-409a-b652-bef8f2b37b59
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugEventCallbacks, ExitThread, IDebugEventCallbacks::ExitThread
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
req.alt-api: IDebugEventCallbacks.ExitThread
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
req.iface: IDebugEventCallbacks
---

# IDebugEventCallbacks::ExitThread method



## -description
<p>The <b>ExitThread</b> callback method is called by the engine when an exit-threaddebugging event occurs in the target.</p>


## -syntax

````
HRESULT ExitThread(
  [in] ULONG ExitCode
);
````


## -parameters
<dl>

### -param <i>ExitCode</i> [in]

<dd>
<p>Specifies the exit code for the thread.</p>
</dd>
</dl>

## -returns
<p>This method returns a <a href="debugger.debug_status_xxx">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_EXIT_THREAD flag is set in the mask returned by <a href="debugger.idebugeventcallbacks_getinterestmask">IDebugEventCallbacks::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.  For information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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
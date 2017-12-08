---
UID: NF.dbgeng.IDebugSystemObjects2.SetCurrentProcessId
title: IDebugSystemObjects2::SetCurrentProcessId
author: windows-driver-content
description: The SetCurrentProcessId method makes the specified process the current process.
old-location: debugger\setcurrentprocessid.htm
old-project: debugger
ms.assetid: 65129c6e-5c69-409b-95f5-07b98a494533
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects2, SetCurrentProcessId, IDebugSystemObjects2::SetCurrentProcessId
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
req.alt-api: IDebugSystemObjects.SetCurrentProcessId,IDebugSystemObjects2.SetCurrentProcessId,IDebugSystemObjects3.SetCurrentProcessId,IDebugSystemObjects4.SetCurrentProcessId
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

# IDebugSystemObjects2::SetCurrentProcessId method



## -description
<p>The <b>SetCurrentProcessId</b> method makes the specified process the current process.</p>


## -syntax

````
HRESULT SetCurrentProcessId(
  [in] ULONG Id
);
````


## -parameters
<dl>

### -param Id [in]

<dd>
<p>Specifies the engine process ID for the process that is to become the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No process with the given process ID was found.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>No suitable candidate for the current thread could be found in the process.</p>

<p> </p>

## -remarks
<p>This method also changes the current thread, and may change the current target and current computer.</p>

<p>If the process is changed, the callback <a href="debugger.idebugeventcallbacks_changeenginestate">IDebugEventCallbacks::ChangeEngineState</a> will be called with the DEBUG_CES_CURRENT_THREAD bit set.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on monitoring events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

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
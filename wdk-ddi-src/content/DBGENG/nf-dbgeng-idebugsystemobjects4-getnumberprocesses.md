---
UID: NF.dbgeng.IDebugSystemObjects4.GetNumberProcesses
title: IDebugSystemObjects4::GetNumberProcesses
author: windows-driver-content
description: The GetNumberProcesses method returns the number of processes for the current target.
old-location: debugger\getnumberprocesses.htm
ms.assetid: bf0c750f-0e29-42d9-a127-953e3d49b969
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSystemObjects.GetNumberProcesses,IDebugSystemObjects2.GetNumberProcesses,IDebugSystemObjects3.GetNumberProcesses,IDebugSystemObjects4.GetNumberProcesses
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
ms.keywords: IDebugSystemObjects4, GetNumberProcesses, IDebugSystemObjects4::GetNumberProcesses
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetNumberProcesses method



## -description
<p>The <b>GetNumberProcesses</b> method returns the number of <a href="debugger.controlling_threads_and_processes#processes#processes">processes</a> for the current target.</p>


## -syntax

````
HRESULT GetNumberProcesses(
  [out] PULONG Number
);
````


## -parameters
<dl>

### -param <i>Number</i> [out]

<dd>
<p>Receives the number of processes.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, there is only a single virtual process representing the kernel.</p>

<p>In user-mode debugging, the number of processes changes with the create-process and exit-process debugging <a href="debugger.events#events#events">events</a>.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>In kernel-mode debugging, there is only a single virtual process representing the kernel.</p>

<p>In user-mode debugging, the number of processes changes with the create-process and exit-process debugging <a href="debugger.events#events#events">events</a>.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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
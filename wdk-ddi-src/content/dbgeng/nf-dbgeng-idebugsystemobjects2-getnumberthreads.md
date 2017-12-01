---
UID: NF.dbgeng.IDebugSystemObjects2.GetNumberThreads
title: IDebugSystemObjects2::GetNumberThreads
author: windows-driver-content
description: The GetNumberThreads method returns the number of threads in the current process.
old-location: debugger\getnumberthreads.htm
old-project: debugger
ms.assetid: f56da2d0-4c4c-4302-a87b-c672dec25d9f
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects2, GetNumberThreads, IDebugSystemObjects2::GetNumberThreads
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
req.alt-api: IDebugSystemObjects.GetNumberThreads,IDebugSystemObjects2.GetNumberThreads,IDebugSystemObjects3.GetNumberThreads,IDebugSystemObjects4.GetNumberThreads
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

# IDebugSystemObjects2::GetNumberThreads method



## -description
<p>The <b>GetNumberThreads</b> method returns the number of <a href="debugger.controlling_threads_and_processes#threads#threads">threads</a> in the current process.</p>


## -syntax

````
HRESULT GetNumberThreads(
  [out] PULONG Number
);
````


## -parameters
<dl>

### -param <i>Number</i> [out]

<dd>
<p>Receives the number of threads in the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, there is a virtual thread representing each processor.</p>

<p>In user-mode debugging, the number of threads changes with the <a href="debugger.idebugeventcallbacks_createthread">IDebugEventCallbacks::CreateThread</a> and <a href="debugger.idebugeventcallbacks_exitthread">IDebugEventCallbacks::ExitThread</a> events.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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
---
UID: NF.dbgeng.IDebugSystemObjects3.GetTotalNumberThreads
title: IDebugSystemObjects3::GetTotalNumberThreads
author: windows-driver-content
description: The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.
old-location: debugger\gettotalnumberthreads.htm
old-project: debugger
ms.assetid: dce67b78-a5e0-4664-b183-f462bcd773c8
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects3, GetTotalNumberThreads, IDebugSystemObjects3::GetTotalNumberThreads
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
req.alt-api: IDebugSystemObjects.GetTotalNumberThreads,IDebugSystemObjects2.GetTotalNumberThreads,IDebugSystemObjects3.GetTotalNumberThreads,IDebugSystemObjects4.GetTotalNumberThreads
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
req.iface: IDebugSystemObjects3
---

# IDebugSystemObjects3::GetTotalNumberThreads method



## -description
<p>The <b>GetTotalNumberThreads</b> method returns the total number of <a href="debugger.controlling_threads_and_processes#threads#threads">threads</a> for all the <a href="debugger.controlling_threads_and_processes#processes#processes">processes</a> in the current target, in addition to the largest number of threads in any process for the current target.</p>


## -syntax

````
HRESULT GetTotalNumberThreads(
  [out] PULONG Total,
  [out] PULONG LargestProcess
);
````


## -parameters
<dl>

### -param <i>Total</i> [out]

<dd>
<p>Receives the total number of threads for all the processes in the current target.</p>
</dd>

### -param <i>LargestProcess</i> [out]

<dd>
<p>Receives the largest number of threads in any process for the current target.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
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
---
UID: NF.dbgeng.IDebugSystemObjects.GetThreadIdsByIndex
title: IDebugSystemObjects::GetThreadIdsByIndex
author: windows-driver-content
description: The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process.
old-location: debugger\getthreadidsbyindex.htm
old-project: debugger
ms.assetid: d671ea6e-19cb-4a90-b345-ea544c9561cd
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects, GetThreadIdsByIndex, IDebugSystemObjects::GetThreadIdsByIndex
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
req.alt-api: IDebugSystemObjects.GetThreadIdsByIndex,IDebugSystemObjects2.GetThreadIdsByIndex,IDebugSystemObjects3.GetThreadIdsByIndex,IDebugSystemObjects4.GetThreadIdsByIndex
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
req.iface: IDebugSystemObjects
---

# IDebugSystemObjects::GetThreadIdsByIndex method



## -description
<p>The <b>GetThreadIdsByIndex</b> method returns the engine and system thread IDs for the specified <a href="debugger.controlling_threads_and_processes#threads#threads">threads</a> in the current process.</p>


## -syntax

````
HRESULT GetThreadIdsByIndex(
  [in]            ULONG  Start,
  [in]            ULONG  Count,
  [out, optional] PULONG Ids,
  [out, optional] PULONG SysIds
);
````


## -parameters
<dl>

### -param <i>Start</i> [in]

<dd>
<p>Specifies the index of the first thread whose IDs are requested.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of threads whose IDs are requested.</p>
</dd>

### -param <i>Ids</i> [out, optional]

<dd>
<p>Receives the engine thread IDs.  If <i>Ids</i> is <b>NULL</b>, this information is not returned; otherwise, <i>Ids</i> is treated as an array of <i>Count</i> ULONG valuess.</p>
</dd>

### -param <i>SysIds</i> [out, optional]

<dd>
<p>Receives the system thread IDs.  If <i>SysIds</i> is <b>NULL</b>, this information is not returned; otherwise, <i>SysIds</i> is treated as an array of <i>Count</i> ULONG values.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The index of the first thread is zero.  The index of the last thread is the number of threads returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff547992">GetNumberThreads</a> minus one.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>The index of the first thread is zero.  The index of the last thread is the number of threads returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff547992">GetNumberThreads</a> minus one.</p>

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
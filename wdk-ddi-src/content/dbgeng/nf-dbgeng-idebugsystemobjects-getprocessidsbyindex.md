---
UID: NF.dbgeng.IDebugSystemObjects.GetProcessIdsByIndex
title: IDebugSystemObjects::GetProcessIdsByIndex
author: windows-driver-content
description: The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target.
old-location: debugger\getprocessidsbyindex.htm
old-project: debugger
ms.assetid: 2ae042c5-9c2a-4de4-817c-c9b97f979684
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects, GetProcessIdsByIndex, IDebugSystemObjects::GetProcessIdsByIndex
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
req.alt-api: IDebugSystemObjects.GetProcessIdsByIndex,IDebugSystemObjects2.GetProcessIdsByIndex,IDebugSystemObjects3.GetProcessIdsByIndex,IDebugSystemObjects4.GetProcessIdsByIndex
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

# IDebugSystemObjects::GetProcessIdsByIndex method



## -description
<p>The <b>GetProcessIdsByIndex</b> method returns the engine process ID and system process ID for the specified <a href="debugger.controlling_threads_and_processes#processes#processes">processes</a> in the current target.</p>


## -syntax

````
HRESULT GetProcessIdsByIndex(
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
<p>Specifies the index of the first process whose ID is requested.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of processes whose IDs are requested.</p>
</dd>

### -param <i>Ids</i> [out, optional]

<dd>
<p>Receives the engine process IDs.  If <i>Ids</i> is <b>NULL</b>, this information is not returned; otherwise, <i>Ids</i> is treated as an array of <i>Count</i> ULONG values.</p>
</dd>

### -param <i>SysIds</i> [out, optional]

<dd>
<p>Receives the system process IDs.  If <i>SysIds</i> is <b>NULL</b>, this information is not returned; otherwise, <i>SysIds</i> is treated as an array of <i>Count</i> ULONG values.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The index of the first process is zero.  The index of the last process is the number of processes returned by <a href="debugger.getnumberprocesses">GetNumberProcesses</a> minus one.</p>

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
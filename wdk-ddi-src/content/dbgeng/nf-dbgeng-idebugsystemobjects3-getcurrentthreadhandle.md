---
UID: NF.dbgeng.IDebugSystemObjects3.GetCurrentThreadHandle
title: IDebugSystemObjects3::GetCurrentThreadHandle
author: windows-driver-content
description: The GetCurrentThreadHandle method returns the system handle for the current thread.
old-location: debugger\getcurrentthreadhandle.htm
old-project: debugger
ms.assetid: edbda821-8016-48db-a2f5-7f615428da0c
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects3, GetCurrentThreadHandle, IDebugSystemObjects3::GetCurrentThreadHandle
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
req.alt-api: IDebugSystemObjects.GetCurrentThreadHandle,IDebugSystemObjects2.GetCurrentThreadHandle,IDebugSystemObjects3.GetCurrentThreadHandle,IDebugSystemObjects4.GetCurrentThreadHandle
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

# IDebugSystemObjects3::GetCurrentThreadHandle method



## -description
<p>The <b>GetCurrentThreadHandle</b> method returns the system handle for the current thread.</p>


## -syntax

````
HRESULT GetCurrentThreadHandle(
  [out] PULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>Handle</i> [out]

<dd>
<p>Receives the current thread's system handle.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, an artificial handle is created because the threads are virtual threads.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on system handles, see <a href="wdkgloss.h#wdkgloss.handle#wdkgloss.handle"><i>Handles</i></a>.</p>

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
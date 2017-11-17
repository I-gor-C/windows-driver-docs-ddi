---
UID: NF.dbgeng.IDebugSystemObjects4.GetCurrentThreadHandle
title: IDebugSystemObjects4::GetCurrentThreadHandle
author: windows-driver-content
description: The GetCurrentThreadHandle method returns the system handle for the current thread.
old-location: debugger\getcurrentthreadhandle.htm
ms.assetid: edbda821-8016-48db-a2f5-7f615428da0c
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
ms.keywords: IDebugSystemObjects4, GetCurrentThreadHandle, IDebugSystemObjects4::GetCurrentThreadHandle
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetCurrentThreadHandle method



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
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, an artificial handle is created because the threads are virtual threads.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on system handles, see <a href="wdkgloss.h#wdkgloss.handle#wdkgloss.handle"><i>Handles</i></a>.</p>

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
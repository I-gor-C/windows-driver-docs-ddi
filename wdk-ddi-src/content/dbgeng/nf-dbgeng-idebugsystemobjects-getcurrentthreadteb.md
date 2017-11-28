---
UID: NF.dbgeng.IDebugSystemObjects.GetCurrentThreadTeb
title: IDebugSystemObjects::GetCurrentThreadTeb
author: windows-driver-content
description: The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread.
old-location: debugger\getcurrentthreadteb.htm
old-project: debugger
ms.assetid: f5acd64c-c5a8-4977-8059-cc0bd12ef0c0
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects, GetCurrentThreadTeb, IDebugSystemObjects::GetCurrentThreadTeb
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
req.alt-api: IDebugSystemObjects.GetCurrentThreadTeb,IDebugSystemObjects2.GetCurrentThreadTeb,IDebugSystemObjects3.GetCurrentThreadTeb,IDebugSystemObjects4.GetCurrentThreadTeb
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

# IDebugSystemObjects::GetCurrentThreadTeb method



## -description
<p>The <b>GetCurrentThreadTeb</b> method returns the location of the thread environment block (TEB) for the current thread.</p>


## -syntax

````
HRESULT GetCurrentThreadTeb(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location in the target's virtual address space of the TEB for the current thread.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In user-mode debugging, this method provides the same information as <a href="https://msdn.microsoft.com/library/windows/hardware/ff545894">GetCurrentThreadDataOffset</a>.</p>

<p>In kernel-mode debugging, the location returned is of the TEB structure of the system thread that was executing on the processor represented by the current thread when the last event occurred.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the TEB structure, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In user-mode debugging, this method provides the same information as <a href="https://msdn.microsoft.com/library/windows/hardware/ff545894">GetCurrentThreadDataOffset</a>.</p>

<p>In kernel-mode debugging, the location returned is of the TEB structure of the system thread that was executing on the processor represented by the current thread when the last event occurred.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the TEB structure, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
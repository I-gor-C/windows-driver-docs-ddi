---
UID: NF.dbgeng.IDebugSystemObjects.GetCurrentThreadDataOffset
title: IDebugSystemObjects::GetCurrentThreadDataOffset
author: windows-driver-content
description: The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread.
old-location: debugger\getcurrentthreaddataoffset.htm
old-project: debugger
ms.assetid: 7837c049-fdca-4f90-9f38-2ec91ed8703b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects, GetCurrentThreadDataOffset, IDebugSystemObjects::GetCurrentThreadDataOffset
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
req.alt-api: IDebugSystemObjects.GetCurrentThreadDataOffset,IDebugSystemObjects2.GetCurrentThreadDataOffset,IDebugSystemObjects3.GetCurrentThreadDataOffset,IDebugSystemObjects4.GetCurrentThreadDataOffset
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

# IDebugSystemObjects::GetCurrentThreadDataOffset method



## -description
<p>The <b>GetCurrentThreadDataOffset</b> method returns the location of the system data structure for the current thread.</p>


## -syntax

````
HRESULT GetCurrentThreadDataOffset(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location of the system data structure for the current thread.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In user-mode debugging, the location returned is of the thread environment block (TEB) for the current thread.  This is the same location returned by <a href="debugger.getcurrentthreadteb">GetCurrentThreadTeb</a>.</p>

<p>In kernel-mode debugging, the location returned is of the KTHREAD structure of the system thread that was executing on the processor represented by the current thread when the last event occurred.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KTHREAD and TEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
---
UID: NF.dbgeng.IDebugSystemObjects2.GetThreadIdByHandle
title: IDebugSystemObjects2::GetThreadIdByHandle
author: windows-driver-content
description: The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle.
old-location: debugger\getthreadidbyhandle.htm
old-project: debugger
ms.assetid: 80962f29-9a11-456b-b083-bd0f4e26e954
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects2, GetThreadIdByHandle, IDebugSystemObjects2::GetThreadIdByHandle
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
req.alt-api: IDebugSystemObjects.GetThreadIdByHandle,IDebugSystemObjects2.GetThreadIdByHandle,IDebugSystemObjects3.GetThreadIdByHandle,IDebugSystemObjects4.GetThreadIdByHandle
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

# IDebugSystemObjects2::GetThreadIdByHandle method



## -description
<p>The <b>GetThreadIdByHandle</b> method returns the engine thread ID for the specified thread.  The thread is specified by its system handle.</p>


## -syntax

````
HRESULT GetThreadIdByHandle(
  [in]  ULONG64 Handle,
  [out] PULONG  Id
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the system handle of the thread whose thread ID is requested.</p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine thread ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, because the handle is an artificial handle for a processor,  this method returns the engine thread ID for the virtual thread representing that processor.</p>

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
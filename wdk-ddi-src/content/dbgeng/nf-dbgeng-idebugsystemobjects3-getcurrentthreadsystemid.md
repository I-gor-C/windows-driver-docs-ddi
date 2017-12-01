---
UID: NF.dbgeng.IDebugSystemObjects3.GetCurrentThreadSystemId
title: IDebugSystemObjects3::GetCurrentThreadSystemId
author: windows-driver-content
description: The GetCurrentThreadSystemId method returns the system thread ID of the current thread.
old-location: debugger\getcurrentthreadsystemid.htm
old-project: debugger
ms.assetid: b2e4d14c-a97f-4f57-b0ce-5a52a82c1690
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects3, GetCurrentThreadSystemId, IDebugSystemObjects3::GetCurrentThreadSystemId
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
req.alt-api: IDebugSystemObjects.GetCurrentThreadSystemId,IDebugSystemObjects2.GetCurrentThreadSystemId,IDebugSystemObjects3.GetCurrentThreadSystemId,IDebugSystemObjects4.GetCurrentThreadSystemId
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

# IDebugSystemObjects3::GetCurrentThreadSystemId method



## -description
<p>The <b>GetCurrentThreadSystemId</b> method returns the system thread ID of the current thread.</p>


## -syntax

````
HRESULT GetCurrentThreadSystemId(
  [out] PULONG SysId
);
````


## -parameters
<dl>

### -param <i>SysId</i> [out]

<dd>
<p>Receives the system thread ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The target is a kernel-mode target.</p>

<p> </p>

## -remarks
<p>This method is only available in user-mode debugging.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p></p>
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
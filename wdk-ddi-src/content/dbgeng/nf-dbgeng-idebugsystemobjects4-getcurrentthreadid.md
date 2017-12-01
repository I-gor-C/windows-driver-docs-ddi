---
UID: NF.dbgeng.IDebugSystemObjects4.GetCurrentThreadId
title: IDebugSystemObjects4::GetCurrentThreadId
author: windows-driver-content
description: The GetCurrentThreadId method returns the engine thread ID for the current thread.
old-location: debugger\getcurrentthreadid.htm
old-project: debugger
ms.assetid: 7062c962-2e82-40e3-81ea-97ac0948e501
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects4, GetCurrentThreadId, IDebugSystemObjects4::GetCurrentThreadId
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
req.alt-api: IDebugSystemObjects.GetCurrentThreadId,IDebugSystemObjects2.GetCurrentThreadId,IDebugSystemObjects3.GetCurrentThreadId,IDebugSystemObjects4.GetCurrentThreadId
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
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetCurrentThreadId method



## -description
<p>The <b>GetCurrentThreadId</b> method returns the engine thread ID for the current thread.</p>


## -syntax

````
HRESULT GetCurrentThreadId(
  [out] PULONG Id
);
````


## -parameters
<dl>

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
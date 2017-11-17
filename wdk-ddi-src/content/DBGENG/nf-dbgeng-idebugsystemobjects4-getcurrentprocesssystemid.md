---
UID: NF.dbgeng.IDebugSystemObjects4.GetCurrentProcessSystemId
title: IDebugSystemObjects4::GetCurrentProcessSystemId
author: windows-driver-content
description: The GetCurrentProcessSystemId method returns the system process ID of the current process.
old-location: debugger\getcurrentprocesssystemid.htm
ms.assetid: 850f2f86-af0d-414a-99d7-d081753c591f
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
req.alt-api: IDebugSystemObjects.GetCurrentProcessSystemId,IDebugSystemObjects2.GetCurrentProcessSystemId,IDebugSystemObjects3.GetCurrentProcessSystemId,IDebugSystemObjects4.GetCurrentProcessSystemId
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
ms.keywords: IDebugSystemObjects4, GetCurrentProcessSystemId, IDebugSystemObjects4::GetCurrentProcessSystemId
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetCurrentProcessSystemId method



## -description
<p>The <b>GetCurrentProcessSystemId</b> method returns the system process ID of the current process.</p>


## -syntax

````
HRESULT GetCurrentProcessSystemId(
  [out] PULONG SysId
);
````


## -parameters
<dl>

### -param <i>SysId</i> [out]

<dd>
<p>Receives the system process ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The target is a kernel-mode target.</p>

<p> </p>

## -remarks
<p>This method is only available in user-mode debugging.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>This method is only available in user-mode debugging.</p>

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
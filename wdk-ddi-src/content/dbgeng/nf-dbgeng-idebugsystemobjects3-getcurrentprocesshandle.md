---
UID: NF.dbgeng.IDebugSystemObjects3.GetCurrentProcessHandle
title: IDebugSystemObjects3::GetCurrentProcessHandle
author: windows-driver-content
description: The GetCurrentProcessHandle method returns the system handle for the current process.
old-location: debugger\getcurrentprocesshandle2.htm
old-project: debugger
ms.assetid: 87f60064-5722-4b4e-af9b-f1d9009a7551
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects3, GetCurrentProcessHandle, IDebugSystemObjects3::GetCurrentProcessHandle
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
req.alt-api: IDebugSystemObjects.GetCurrentProcessHandle,IDebugSystemObjects2.GetCurrentProcessHandle,IDebugSystemObjects3.GetCurrentProcessHandle,IDebugSystemObjects4.GetCurrentProcessHandle
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

# IDebugSystemObjects3::GetCurrentProcessHandle method



## -description
<p>The <b>GetCurrentProcessHandle</b> method returns the system handle for the current process.</p>


## -syntax

````
HRESULT GetCurrentProcessHandle(
  [out] PULONG64 Handle
);
````


## -parameters
<dl>

### -param Handle [out]

<dd>
<p>Receives the system handle of the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, the only process in the target is the virtual process created for the kernel.  In this case, an artificial handle is created.  The artificial handle can only be used with the debugger engine API.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on system handles, see <a href="wdkgloss.h#wdkgloss.handle#wdkgloss.handle"><i>Handles</i></a>.</p>

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
---
UID: NF.dbgeng.IDebugSystemObjects.GetProcessIdByHandle
title: IDebugSystemObjects::GetProcessIdByHandle
author: windows-driver-content
description: The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle.
old-location: debugger\getprocessidbyhandle.htm
old-project: debugger
ms.assetid: 6920cbd3-0a20-4d38-8538-85f46d0f0d5b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects, GetProcessIdByHandle, IDebugSystemObjects::GetProcessIdByHandle
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
req.alt-api: IDebugSystemObjects.GetProcessIdByHandle,IDebugSystemObjects2.GetProcessIdByHandle,IDebugSystemObjects3.GetProcessIdByHandle,IDebugSystemObjects4.GetProcessIdByHandle
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

# IDebugSystemObjects::GetProcessIdByHandle method



## -description
<p>The <b>GetProcessIdByHandle</b> method returns the engine process ID for the specified process.  The process is specified by its system handle.</p>


## -syntax

````
HRESULT GetProcessIdByHandle(
  [in]  ULONG64 Handle,
  [out] PULONG  Id
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the handle of the process whose process ID is requested.  This handle must be a process handle previously retrieved from the debugger engine.</p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine process ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on system handles, see <a href="wdkgloss.h#wdkgloss.handle#wdkgloss.handle"><i>Handles</i></a>.</p>

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
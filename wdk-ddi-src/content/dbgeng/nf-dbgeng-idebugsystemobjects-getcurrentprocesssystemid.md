---
UID: NF.dbgeng.IDebugSystemObjects.GetCurrentProcessSystemId
title: IDebugSystemObjects::GetCurrentProcessSystemId
author: windows-driver-content
description: The GetCurrentProcessSystemId method returns the system process ID of the current process.
old-location: debugger\getcurrentprocesssystemid.htm
old-project: debugger
ms.assetid: 850f2f86-af0d-414a-99d7-d081753c591f
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects, GetCurrentProcessSystemId, IDebugSystemObjects::GetCurrentProcessSystemId
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
req.iface: IDebugSystemObjects
---

# IDebugSystemObjects::GetCurrentProcessSystemId method



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
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The target is a kernel-mode target.</p>

<p> </p>

## -remarks
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
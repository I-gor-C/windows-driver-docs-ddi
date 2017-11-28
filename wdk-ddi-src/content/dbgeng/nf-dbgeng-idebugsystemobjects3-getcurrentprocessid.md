---
UID: NF.dbgeng.IDebugSystemObjects3.GetCurrentProcessId
title: IDebugSystemObjects3::GetCurrentProcessId
author: windows-driver-content
description: The GetCurrentProcessId method returns the engine process ID for the current process.
old-location: debugger\getcurrentprocessid.htm
old-project: debugger
ms.assetid: 5b256ccb-8f03-4936-8e03-9955c81384a5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects3, GetCurrentProcessId, IDebugSystemObjects3::GetCurrentProcessId
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
req.alt-api: IDebugSystemObjects.GetCurrentProcessId,IDebugSystemObjects2.GetCurrentProcessId,IDebugSystemObjects3.GetCurrentProcessId,IDebugSystemObjects4.GetCurrentProcessId
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

# IDebugSystemObjects3::GetCurrentProcessId method



## -description
<p>The <b>GetCurrentProcessId</b> method returns the engine process ID for the current process.</p>


## -syntax

````
HRESULT GetCurrentProcessId(
  [out] PULONG Id
);
````


## -parameters
<dl>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine process ID for the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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
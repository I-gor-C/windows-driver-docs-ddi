---
UID: NF.dbgeng.IDebugSystemObjects4.GetCurrentProcessPeb
title: IDebugSystemObjects4::GetCurrentProcessPeb
author: windows-driver-content
description: The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process.
old-location: debugger\getcurrentprocesspeb.htm
old-project: debugger
ms.assetid: fa1e2915-3cb5-4634-a8fb-0d2d565c1c00
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects4, GetCurrentProcessPeb, IDebugSystemObjects4::GetCurrentProcessPeb
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
req.alt-api: IDebugSystemObjects.GetCurrentProcessPeb,IDebugSystemObjects2.GetCurrentProcessPeb,IDebugSystemObjects3.GetCurrentProcessPeb,IDebugSystemObjects4.GetCurrentProcessPeb
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

# IDebugSystemObjects4::GetCurrentProcessPeb method



## -description
<p>The <b>GetCurrentProcessPeb</b> method returns the process environment block (PEB) of the current process.</p>


## -syntax

````
HRESULT GetCurrentProcessPeb(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location in the target's virtual address space of the PEB of the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In user-mode debugging, this method provides the same information as <a href="debugger.getcurrentprocessdataoffset">GetCurrentProcessDataOffset</a>.</p>

<p>In kernel-mode debugging, the location returned is that of the PEB structure for the system process in which the last event occurred.</p>

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
---
UID: NF.dbgeng.IDebugSystemObjects4.GetProcessIdByPeb
title: IDebugSystemObjects4::GetProcessIdByPeb
author: windows-driver-content
description: The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB).
old-location: debugger\getprocessidbypeb.htm
ms.assetid: 2ee2b610-30c7-4932-b8f6-df5040a5bad8
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
req.alt-api: IDebugSystemObjects.GetProcessIdByPeb,IDebugSystemObjects2.GetProcessIdByPeb,IDebugSystemObjects3.GetProcessIdByPeb,IDebugSystemObjects4.GetProcessIdByPeb
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
ms.keywords: IDebugSystemObjects4, GetProcessIdByPeb, IDebugSystemObjects4::GetProcessIdByPeb
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetProcessIdByPeb method



## -description
<p>The <b>GetProcessIdByPeb</b> method returns the engine process ID for the specified process.  The process is specified by its process environment block (PEB).</p>


## -syntax

````
HRESULT GetProcessIdByPeb(
  [in]  ULONG64 Offset,
  [out] PULONG  Id
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space of the PEB of the process whose process ID is requested.</p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine process ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The target is a kernel-mode target.  This method is currently not available in kernel-mode debugging.</p>

<p> </p>

## -remarks
<p>This method is not available in kernel-mode debugging.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>This method is not available in kernel-mode debugging.</p>

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
---
UID: NF.dbgeng.IDebugClient5.GetExitCode
title: IDebugClient5::GetExitCode
author: windows-driver-content
description: The GetExitCode method returns the exit code of the current process if that process has already run through to completion.
old-location: debugger\getexitcode.htm
ms.assetid: faa5cc0f-a99c-42fb-ab8f-a37c31bc4dde
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
req.alt-api: IDebugClient.GetExitCode,IDebugClient2.GetExitCode,IDebugClient3.GetExitCode,IDebugClient4.GetExitCode,IDebugClient5.GetExitCode
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
ms.keywords: IDebugClient5, GetExitCode, IDebugClient5::GetExitCode
req.iface: IDebugClient5
---

# IDebugClient5::GetExitCode method



## -description
<p>The <b>GetExitCode</b> method returns the exit code of the current process if that process has already run through to completion.</p>


## -syntax

````
HRESULT GetExitCode(
  [out] PULONG Code
);
````


## -parameters
<dl>

### -param <i>Code</i> [out]

<dd>
<p>Receives the exit code of the process.  If the process is still running, <i>Code</i> will be set to STILL_ACTIVE.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The process is still running.</p>

<p> </p>

## -remarks
<p>This method is available only for live user-mode debugging.</p>

<p>This method is available only for live user-mode debugging.</p>

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
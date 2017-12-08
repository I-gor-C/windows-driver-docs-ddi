---
UID: NF.dbgeng.IDebugSystemObjects2.GetProcessIdBySystemId
title: IDebugSystemObjects2::GetProcessIdBySystemId
author: windows-driver-content
description: The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID.
old-location: debugger\getprocessidbysystemid.htm
old-project: debugger
ms.assetid: 7260f0ea-5e8b-4b08-8c8f-70216ffe54a9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects2, GetProcessIdBySystemId, IDebugSystemObjects2::GetProcessIdBySystemId
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
req.alt-api: IDebugSystemObjects.GetProcessIdBySystemId,IDebugSystemObjects2.GetProcessIdBySystemId,IDebugSystemObjects3.GetProcessIdBySystemId,IDebugSystemObjects4.GetProcessIdBySystemId
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
req.iface: IDebugSystemObjects2
---

# IDebugSystemObjects2::GetProcessIdBySystemId method



## -description
<p>The <b>GetProcessIdBySystemId</b> method returns the engine process ID for a process specified by its system process ID.</p>


## -syntax

````
HRESULT GetProcessIdBySystemId(
  [in]  ULONG  SysId,
  [out] PULONG Id
);
````


## -parameters
<dl>

### -param SysId [in]

<dd>
<p>Specifies the system process ID.</p>
</dd>

### -param Id [out]

<dd>
<p>Receives the engine process ID.</p>
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
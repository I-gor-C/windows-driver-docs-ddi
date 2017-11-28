---
UID: NF.dbgeng.IDebugSystemObjects3.GetThreadIdBySystemId
title: IDebugSystemObjects3::GetThreadIdBySystemId
author: windows-driver-content
description: The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID.
old-location: debugger\getthreadidbysystemid.htm
old-project: debugger
ms.assetid: 2dcb7703-df66-4795-bf59-d0851c4ccf0f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects3, GetThreadIdBySystemId, IDebugSystemObjects3::GetThreadIdBySystemId
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
req.alt-api: IDebugSystemObjects.GetThreadIdBySystemId,IDebugSystemObjects2.GetThreadIdBySystemId,IDebugSystemObjects3.GetThreadIdBySystemId,IDebugSystemObjects4.GetThreadIdBySystemId
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

# IDebugSystemObjects3::GetThreadIdBySystemId method



## -description
<p>The <b>GetThreadIdBySystemId</b> method returns the engine thread ID for the specified thread.  The thread is specified by its system thread ID.</p>


## -syntax

````
HRESULT GetThreadIdBySystemId(
  [in]  ULONG  SysId,
  [out] PULONG Id
);
````


## -parameters
<dl>

### -param <i>SysId</i> [in]

<dd>
<p>Specifies the system thread ID.</p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine thread ID.</p>
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

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>This method is only available in user-mode debugging.</p>

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
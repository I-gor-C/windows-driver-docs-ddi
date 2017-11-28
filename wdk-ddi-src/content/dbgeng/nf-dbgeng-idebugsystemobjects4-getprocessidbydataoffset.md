---
UID: NF.dbgeng.IDebugSystemObjects4.GetProcessIdByDataOffset
title: IDebugSystemObjects4::GetProcessIdByDataOffset
author: windows-driver-content
description: The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset.
old-location: debugger\getprocessidbydataoffset.htm
old-project: debugger
ms.assetid: a2c094f4-f54d-4c3c-95e7-75df717db8cc
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects4, GetProcessIdByDataOffset, IDebugSystemObjects4::GetProcessIdByDataOffset
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
req.alt-api: IDebugSystemObjects.GetProcessIdByDataOffset,IDebugSystemObjects2.GetProcessIdByDataOffset,IDebugSystemObjects3.GetProcessIdByDataOffset,IDebugSystemObjects4.GetProcessIdByDataOffset
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

# IDebugSystemObjects4::GetProcessIdByDataOffset method



## -description
<p>The <b>GetProcessIdByDataOffset</b> method returns the engine process ID for the specified process.  The process is specified by its data offset.</p>


## -syntax

````
HRESULT GetProcessIdByDataOffset(
  [in]  ULONG64 Offset,
  [out] PULONG  Id
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space of the data offset of the process.</p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine process ID for the process.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The current target is a kernel-mode target.  This method is currently not available in kernel-mode debugging.</p>

<p> </p>

## -remarks
<p>This method is currently not available in kernel-mode debugging.</p>

<p>In user-mode debugging, this method behaves the same as <a href="https://msdn.microsoft.com/library/windows/hardware/ff548150">GetProcessIdByPeb</a>.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>This method is currently not available in kernel-mode debugging.</p>

<p>In user-mode debugging, this method behaves the same as <a href="https://msdn.microsoft.com/library/windows/hardware/ff548150">GetProcessIdByPeb</a>.</p>

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
---
UID: NF.dbgeng.IDebugSystemObjects3.GetImplicitThreadDataOffset
title: IDebugSystemObjects3::GetImplicitThreadDataOffset
author: windows-driver-content
description: The GetImplicitThreadDataOffset method returns the implicit thread for the current process.
old-location: debugger\getimplicitthreaddataoffset.htm
old-project: debugger
ms.assetid: fe7a1afe-dc87-412c-9e35-4a1af05f9474
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects3, GetImplicitThreadDataOffset, IDebugSystemObjects3::GetImplicitThreadDataOffset
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
req.alt-api: IDebugSystemObjects2.GetImplicitThreadDataOffset,IDebugSystemObjects3.GetImplicitThreadDataOffset,IDebugSystemObjects4.GetImplicitThreadDataOffset
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

# IDebugSystemObjects3::GetImplicitThreadDataOffset method



## -description
<p>The <b>GetImplicitThreadDataOffset</b> method returns the implicit thread for the current process.</p>


## -syntax

````
HRESULT GetImplicitThreadDataOffset(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location in the target's memory address space of the data structure of the system thread that is the implicit thread for the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, the data structure is the KTHREAD structure for the process.</p>

<p>In user-mode debugging, the data structure is the thread environment block (TEB) for the process.</p>

<p>For more information about the implicit thread, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KTHREAD structure and TEB, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In kernel-mode debugging, the data structure is the KTHREAD structure for the process.</p>

<p>In user-mode debugging, the data structure is the thread environment block (TEB) for the process.</p>

<p>For more information about the implicit thread, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KTHREAD structure and TEB, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
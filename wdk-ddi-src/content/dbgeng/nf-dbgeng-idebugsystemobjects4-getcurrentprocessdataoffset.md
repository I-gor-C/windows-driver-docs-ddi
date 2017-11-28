---
UID: NF.dbgeng.IDebugSystemObjects4.GetCurrentProcessDataOffset
title: IDebugSystemObjects4::GetCurrentProcessDataOffset
author: windows-driver-content
description: The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process.
old-location: debugger\getcurrentprocessdataoffset.htm
old-project: debugger
ms.assetid: a71190ac-0368-40bd-a19d-82a27986a9b3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects4, GetCurrentProcessDataOffset, IDebugSystemObjects4::GetCurrentProcessDataOffset
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
req.alt-api: IDebugSystemObjects.GetCurrentProcessDataOffset,IDebugSystemObjects2.GetCurrentProcessDataOffset,IDebugSystemObjects3.GetCurrentProcessDataOffset,IDebugSystemObjects4.GetCurrentProcessDataOffset
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

# IDebugSystemObjects4::GetCurrentProcessDataOffset method



## -description
<p>The <b>GetCurrentProcessDataOffset</b> method returns the location of the system data structure describing the current process.</p>


## -syntax

````
HRESULT GetCurrentProcessDataOffset(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location in the target's virtual address space of the system data structure describing the current process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In user-mode debugging, the location returned is of the process environment block (PEB) for the current process.  This is the same location returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff545839">GetCurrentProcessPeb</a>.</p>

<p>In kernel-mode debugging, the location returned is of the KPROCESS structure for the system process in which the last event occurred.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details about the PEB and KPROCESS structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In user-mode debugging, the location returned is of the process environment block (PEB) for the current process.  This is the same location returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff545839">GetCurrentProcessPeb</a>.</p>

<p>In kernel-mode debugging, the location returned is of the KPROCESS structure for the system process in which the last event occurred.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details about the PEB and KPROCESS structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
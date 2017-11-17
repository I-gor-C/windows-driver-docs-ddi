---
UID: NF.dbgeng.IDebugSystemObjects4.GetImplicitProcessDataOffset
title: IDebugSystemObjects4::GetImplicitProcessDataOffset
author: windows-driver-content
description: The GetImplicitProcessDataOffset method returns the implicit process for the current target.
old-location: debugger\getimplicitprocessdataoffset.htm
ms.assetid: 20a11f3b-cc49-4080-ac4c-b8e18d4b2f73
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
req.alt-api: IDebugSystemObjects2.GetImplicitProcessDataOffset,IDebugSystemObjects3.GetImplicitProcessDataOffset,IDebugSystemObjects4.GetImplicitProcessDataOffset
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
ms.keywords: IDebugSystemObjects4, GetImplicitProcessDataOffset, IDebugSystemObjects4::GetImplicitProcessDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetImplicitProcessDataOffset method



## -description
<p>The <b>GetImplicitProcessDataOffset</b> method returns the implicit process for the current target.</p>


## -syntax

````
HRESULT GetImplicitProcessDataOffset(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location in the target's memory address space of the data structure of the system process that is the implicit process for the current target.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, the data structure is the KPROCESS structure for the process.</p>

<p>In user-mode debugging, the data structure is the process environment block (PEB) for the process.</p>

<p>For more information about the implicit process, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KPROCESS and PEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In kernel-mode debugging, the data structure is the KPROCESS structure for the process.</p>

<p>In user-mode debugging, the data structure is the process environment block (PEB) for the process.</p>

<p>For more information about the implicit process, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KPROCESS and PEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
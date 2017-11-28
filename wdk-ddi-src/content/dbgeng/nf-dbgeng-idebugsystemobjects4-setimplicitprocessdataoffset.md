---
UID: NF.dbgeng.IDebugSystemObjects4.SetImplicitProcessDataOffset
title: IDebugSystemObjects4::SetImplicitProcessDataOffset
author: windows-driver-content
description: The SetImplicitProcessDataOffset method sets the implicit process for the current target.
old-location: debugger\setimplicitprocessdataoffset.htm
old-project: debugger
ms.assetid: 2a09341d-a580-4817-9103-29d8c36b81e3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects4, SetImplicitProcessDataOffset, IDebugSystemObjects4::SetImplicitProcessDataOffset
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
req.alt-api: IDebugSystemObjects2.SetImplicitProcessDataOffset,IDebugSystemObjects3.SetImplicitProcessDataOffset,IDebugSystemObjects4.SetImplicitProcessDataOffset
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

# IDebugSystemObjects4::SetImplicitProcessDataOffset method



## -description
<p>The <b>SetImplicitProcessDataOffset</b> method sets the implicit process for the current target.</p>


## -syntax

````
HRESULT SetImplicitProcessDataOffset(
  [in] ULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's memory address space of the data structure of the system process that is to become the implicit process for the current target.  If this is zero, the implicit process for the current target is set to the default implicit process.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>In kernel-mode debugging, the data structure is the KPROCESS structure for the process.</p>

<p>In user-mode debugging, the data structure is the process environment block (PEB) for the process.</p>

<p>For more information about the current implicit process, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KPROCESS and PEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In kernel-mode debugging, the data structure is the KPROCESS structure for the process.</p>

<p>In user-mode debugging, the data structure is the process environment block (PEB) for the process.</p>

<p>For more information about the current implicit process, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on the KPROCESS and PEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
---
UID: NF.dbgeng.IDebugControl2.GetNearInstruction
title: IDebugControl2::GetNearInstruction
author: windows-driver-content
description: The GetNearInstruction method returns the location of a processor instruction relative to a given location.
old-location: debugger\getnearinstruction.htm
old-project: debugger
ms.assetid: 76387681-cac6-4c35-9095-28942a856c30
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl2, GetNearInstruction, IDebugControl2::GetNearInstruction
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
req.alt-api: IDebugControl.GetNearInstruction,IDebugControl2.GetNearInstruction,IDebugControl3.GetNearInstruction
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
req.iface: IDebugControl2
---

# IDebugControl2::GetNearInstruction method



## -description
<p>The <b>GetNearInstruction</b> method returns the location of a processor instruction relative to a given location.</p>


## -syntax

````
HRESULT GetNearInstruction(
  [in]  ULONG64  Offset,
  [in]  LONG     Delta,
  [out] PULONG64 NearOffset
);
````


## -parameters
<dl>

### -param Offset [in]

<dd>
<p>Specifies the location in the process's virtual address space from which to start looking for the desired instruction.</p>
</dd>

### -param Delta [in]

<dd>
<p>Specifies the number of instructions from <i>Offset</i> of the desired instruction.  If <i>Delta</i> is negative, the returned offset is before <i>Offset</i> (see the Remarks section for more information).</p>
</dd>

### -param NearOffset [out]

<dd>
<p>Receives the location in the process's virtual address space of the instruction that is <i>Delta</i> instructions away from <i>Offset</i>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>On some architectures, like x86 and x64, the size of an instruction may vary.  On these architectures, when <i>Delta</i> is negative, the desired instruction location might not be uniquely defined.  In this case, the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> will search backward from <i>Offset</i> until it encounters a location such that there are the <i>Delta</i> number of instructions between that location and <i>Offset</i>.</p>

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
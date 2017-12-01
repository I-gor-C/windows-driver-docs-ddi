---
UID: NF.dbgeng.IDebugControl.GetReturnOffset
title: IDebugControl::GetReturnOffset
author: windows-driver-content
description: The GetReturnOffset method returns the return address for the current function.
old-location: debugger\getreturnoffset.htm
old-project: debugger
ms.assetid: 65d72369-7ace-4d3d-a15c-6322c0066470
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl, GetReturnOffset, IDebugControl::GetReturnOffset
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
req.alt-api: IDebugControl.GetReturnOffset,IDebugControl2.GetReturnOffset,IDebugControl3.GetReturnOffset
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
req.iface: IDebugControl
---

# IDebugControl::GetReturnOffset method



## -description
<p>The <b>GetReturnOffset</b> method returns the return address for the current function.</p>


## -syntax

````
HRESULT GetReturnOffset(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the return address.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The return address is the location in the process's virtual address space of the instruction that will be executed when the current function returns.</p>

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
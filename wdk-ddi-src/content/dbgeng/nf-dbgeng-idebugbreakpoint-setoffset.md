---
UID: NF.dbgeng.IDebugBreakpoint.SetOffset
title: IDebugBreakpoint::SetOffset
author: windows-driver-content
description: The SetOffset method sets the location that triggers a breakpoint.
old-location: debugger\setoffset.htm
old-project: debugger
ms.assetid: 25898500-f16e-4838-854f-5eb299727e2b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugBreakpoint, SetOffset, IDebugBreakpoint::SetOffset
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
req.alt-api: IDebugBreakpoint.SetOffset,IDebugBreakpoint2.SetOffset
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
req.iface: IDebugBreakpoint
---

# IDebugBreakpoint::SetOffset method



## -description
<p>The <b>SetOffset</b> method sets the location that triggers a breakpoint.</p>


## -syntax

````
HRESULT SetOffset(
  [in] ULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>The location on the target that triggers the breakpoint.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_UNEXPECTED</b></dt>
</dl><p>The breakpoint is deferred.</p>

<p> </p>

<p>This method can also return other error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>For more information about how to use breakpoints, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a>.</p>

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
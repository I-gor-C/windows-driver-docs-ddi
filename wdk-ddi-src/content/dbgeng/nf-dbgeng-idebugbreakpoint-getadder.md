---
UID: NF.dbgeng.IDebugBreakpoint.GetAdder
title: IDebugBreakpoint::GetAdder
author: windows-driver-content
description: The GetAdder method returns the client that owns the breakpoint.
old-location: debugger\getadder.htm
old-project: debugger
ms.assetid: f57abfc5-d6ae-474b-bea9-bfc53dff7f57
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugBreakpoint, GetAdder, IDebugBreakpoint::GetAdder
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
req.alt-api: IDebugBreakpoint.GetAdder,IDebugBreakpoint2.GetAdder
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

# IDebugBreakpoint::GetAdder method



## -description
<p>The <b>GetAdder</b> method returns the client that owns the breakpoint.</p>


## -syntax

````
HRESULT GetAdder(
  [out] PDEBUG_CLIENT *Adder
);
````


## -parameters
<dl>

### -param Adder [out]

<dd>
<p>An <a href="..\dbgeng\nn-dbgeng-idebugclient.md">IDebugClient</a> interface pointer to the client object that added the breakpoint.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.</p>

## -remarks
<p>The client that owns the breakpoint is the client that created the breakpoint by using the <a href="debugger.addbreakpoint">AddBreakpoint</a> method.  A breakpoint might not have an owner. If a breakpoint does not have an owner, <i>Adder</i> is set to <b>NULL</b>.</p>

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
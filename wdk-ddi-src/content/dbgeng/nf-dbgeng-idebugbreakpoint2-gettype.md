---
UID: NF.dbgeng.IDebugBreakpoint2.GetType
title: IDebugBreakpoint2::GetType
author: windows-driver-content
description: The GetType method returns the type of the breakpoint and the type of the processor that a breakpoint is set for.
old-location: debugger\gettype.htm
old-project: debugger
ms.assetid: c6aa6560-3183-4e3a-a625-80d1c5072af5
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugBreakpoint2, GetType, IDebugBreakpoint2::GetType
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
req.alt-api: IDebugBreakpoint.GetType,IDebugBreakpoint2.GetType
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
req.iface: IDebugBreakpoint2
---

# IDebugBreakpoint2::GetType method



## -description
<p>The <b>GetType</b> method returns the type of the breakpoint and the type of the processor that a breakpoint is set for.</p>


## -syntax

````
HRESULT GetType(
  [out] PULONG BreakType,
  [out] PULONG ProcType
);
````


## -parameters
<dl>

### -param <i>BreakType</i> [out]

<dd>
<p>The type of the breakpoint.  The type can be one of the following  values.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_BREAKPOINT_CODE</p>
</td>
<td>
<p>Software breakpoint</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_BREAKPOINT_DATA</p>
</td>
<td>
<p>Processor breakpoint</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ProcType</i> [out]

<dd>
<p>The type of the processor that the breakpoint is set for.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>If changes are made to the breakpoint, the processor type might change.</p>

<p>The <a href="debugger.getparameters">GetParameters</a> method also returns the information that is returned in <i>BreakType</i> and <i>ProcType</i>.</p>

<p>For more information about breakpoint types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538928">Breakpoints</a>.</p>

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
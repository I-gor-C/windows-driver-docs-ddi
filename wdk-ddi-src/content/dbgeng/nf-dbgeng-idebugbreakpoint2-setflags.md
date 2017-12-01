---
UID: NF.dbgeng.IDebugBreakpoint2.SetFlags
title: IDebugBreakpoint2::SetFlags
author: windows-driver-content
description: The SetFlags method sets the flags for a breakpoint.
old-location: debugger\setflags.htm
old-project: debugger
ms.assetid: 126741ba-b373-466e-986d-44e33c841eee
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugBreakpoint2, SetFlags, IDebugBreakpoint2::SetFlags
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
req.alt-api: IDebugBreakpoint.SetFlags,IDebugBreakpoint2.SetFlags
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

# IDebugBreakpoint2::SetFlags method



## -description
<p>The <b>SetFlags</b> method sets the flags for a breakpoint.</p>


## -syntax

````
HRESULT SetFlags(
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>The new flags for the breakpoint.  <i>Flags</i> is a bit field. It replaces the existing flag bits.  For more information about the flag bit field and an explanation of each flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.  You cannot change the DEBUG_BREAKPOINT_DEFERRED flag in the engine. This bit in <i>Flags</i> must always be zero.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>For more information about breakpoint properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.</p>

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
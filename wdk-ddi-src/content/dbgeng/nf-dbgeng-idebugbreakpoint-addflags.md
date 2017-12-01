---
UID: NF.dbgeng.IDebugBreakpoint.AddFlags
title: IDebugBreakpoint::AddFlags
author: windows-driver-content
description: The AddFlags method adds flags to a breakpoint.
old-location: debugger\addflags.htm
old-project: debugger
ms.assetid: 92161111-5e02-4a97-9656-9a297e9ea1af
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugBreakpoint, AddFlags, IDebugBreakpoint::AddFlags
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
req.alt-api: IDebugBreakpoint.AddFlags,IDebugBreakpoint2.AddFlags
req.alt-loc: Dbgeng.h
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

# IDebugBreakpoint::AddFlags method



## -description
<p>The <b>AddFlags</b> method adds flags to a <a href="debugger.b#breakpoint#breakpoint">breakpoint</a>.</p>


## -syntax

````
HRESULT AddFlags(
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Additional flags to add to the breakpoint.  <i>Flags</i> is a bit field that is combined together with the existing flags by using a bitwise OR.  For more information about the flag bit field and an explanation of each flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.  You cannot modify the DEBUG_BREAKPOINT_DEFERRED flag in the <a href="debugger.e#engine#engine">engine</a>. This bit in <i>Flags</i> must always be zero.</p>
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
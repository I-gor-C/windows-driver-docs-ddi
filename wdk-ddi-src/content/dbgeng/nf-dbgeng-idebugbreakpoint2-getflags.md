---
UID: NF.dbgeng.IDebugBreakpoint2.GetFlags
title: IDebugBreakpoint2::GetFlags
author: windows-driver-content
description: The GetFlags method returns the flags for a breakpoint.
old-location: debugger\getflags.htm
old-project: debugger
ms.assetid: 0137a872-63e9-4630-86fa-accfaa9b6d6b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugBreakpoint2, GetFlags, IDebugBreakpoint2::GetFlags
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
req.alt-api: IDebugBreakpoint.GetFlags,IDebugBreakpoint2.GetFlags
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

# IDebugBreakpoint2::GetFlags method



## -description
<p>The <b>GetFlags</b> method returns the flags for a breakpoint.</p>


## -syntax

````
HRESULT GetFlags(
  [out] PULONG Flags
);
````


## -parameters
<dl>

### -param <i>Flags</i> [out]

<dd>
<p>The breakpoint's flags.  For more information about the flag bit field and an explanation of each flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>The <a href="debugger.getparameters">GetParameters</a> method also returns the breakpoint's flags.</p>

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
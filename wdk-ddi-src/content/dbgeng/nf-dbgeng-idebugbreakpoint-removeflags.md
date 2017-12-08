---
UID: NF.dbgeng.IDebugBreakpoint.RemoveFlags
title: IDebugBreakpoint::RemoveFlags
author: windows-driver-content
description: The RemoveFlags method removes flags from a breakpoint.
old-location: debugger\removeflags.htm
old-project: debugger
ms.assetid: 60538544-6baf-4d23-a65f-5c5e82bd6f11
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugBreakpoint, RemoveFlags, IDebugBreakpoint::RemoveFlags
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
req.alt-api: IDebugBreakpoint.RemoveFlags,IDebugBreakpoint2.RemoveFlags
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

# IDebugBreakpoint::RemoveFlags method



## -description
<p>The <b>RemoveFlags</b> method removes flags from a breakpoint.</p>


## -syntax

````
HRESULT RemoveFlags(
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param Flags [in]

<dd>
<p>Flags to remove from the breakpoint.  <i>Flags</i> is a bit field. The new value of the flags in the engine is the old value and not the value of <i>Flags</i>.  For more information about the flag bit field and an explanation of each flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.  You cannot modify the DEBUG_BREAKPOINT_DEFERRED flag in the engine. This bit in <i>Flags</i> must always be zero.</p>
</dd>
</dl>

## -returns
<p><b>RemoveFlags</b> might return one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.</p>

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
---
UID: NF.dbgeng.IDebugBreakpoint2.GetMatchThreadId
title: IDebugBreakpoint2::GetMatchThreadId
author: windows-driver-content
description: The GetMatchThreadId method returns the engine thread ID of the thread that can trigger a breakpoint.
old-location: debugger\getmatchthreadid.htm
ms.assetid: 0f0f7248-de85-4757-8006-48444af8edac
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugBreakpoint.GetMatchThreadId,IDebugBreakpoint2.GetMatchThreadId
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
ms.keywords: IDebugBreakpoint2, GetMatchThreadId, IDebugBreakpoint2::GetMatchThreadId
req.iface: IDebugBreakpoint2
---

# IDebugBreakpoint2::GetMatchThreadId method



## -description
<p>The <b>GetMatchThreadId</b> method returns the engine thread ID of the thread that can trigger a breakpoint.</p>


## -syntax

````
HRESULT GetMatchThreadId(
  [out] PULONG Id
);
````


## -parameters
<dl>

### -param <i>Id</i> [out]

<dd>
<p>The engine thread ID of the thread that can trigger this breakpoint.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No specific thread has been set for this breakpoint. Any thread can trigger the breakpoint.</p>

<p> </p>

<p>This method can also return other error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.</p>

## -remarks
<p>If you have set a thread for the breakpoint, the breakpoint can be triggered only if that thread hits the breakpoint.  If you have not set a thread , any thread can trigger the breakpoint and <i>Id</i> receives <b>NULL</b>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff548095">GetParameters</a> method also returns the engine thread ID of the thread that can trigger the breakpoint.</p>

<p>For more information about breakpoint properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.</p>

<p>If you have set a thread for the breakpoint, the breakpoint can be triggered only if that thread hits the breakpoint.  If you have not set a thread , any thread can trigger the breakpoint and <i>Id</i> receives <b>NULL</b>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff548095">GetParameters</a> method also returns the engine thread ID of the thread that can trigger the breakpoint.</p>

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
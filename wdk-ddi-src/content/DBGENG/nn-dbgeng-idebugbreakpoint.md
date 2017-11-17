---
UID: NN.dbgeng.IDebugBreakpoint
title: IDebugBreakpoint
author: windows-driver-content
description: IDebugBreakpoint interface
old-location: debugger\idebugbreakpoint.htm
ms.assetid: ad4bcabb-304e-4427-9b0d-2e22429e8cdd
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugBreakpoint
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugBreakpoint interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugBreakpoint</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugBreakpoint</b> also has these types of members:</p>

<p>The <b>IDebugBreakpoint</b> interface has these methods.</p>

<p>Adds flags to a breakpoint.</p>

<p>Returns the client that owns the breakpoint.</p>

<p>Returns the command string that is executed when a breakpoint is triggered.
</p>

<p>Returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered.</p>

<p>Returns the parameters for a processor breakpoint.</p>

<p>Returns the flags for a breakpoint.</p>

<p>Returns a breakpoint ID, which is the engine's unique identifier for a breakpoint.</p>

<p>Returns the engine thread ID of the thread that can trigger a breakpoint.
</p>

<p>Returns the location that triggers a breakpoint.</p>

<p>Returns the expression string that evaluates to the location that triggers a breakpoint.
</p>

<p>Returns the parameters for a breakpoint.</p>

<p>Returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered.</p>

<p>Returns the type of the breakpoint and the type of the processor that a breakpoint is set for.
</p>

<p>Removes flags from a breakpoint.
</p>

<p>Sets the command that is executed when a breakpoint is triggered.
</p>

<p>Sets the parameters for a processor breakpoint.</p>

<p>Sets the flags for a breakpoint.
</p>

<p>Sets the engine thread ID of the thread that can trigger a breakpoint.
</p>

<p>Sets the location that triggers a breakpoint.</p>

<p>Sets an expression string that evaluates to the location that triggers a breakpoint.
</p>

<p>Sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered.
</p>

<p> </p>

## -members
<p>The <b>IDebugBreakpoint</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537903">AddFlags</a>
</td>
<td align="left" width="63%">
<p>Adds flags to a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545576">GetAdder</a>
</td>
<td align="left" width="63%">
<p>Returns the client that owns the breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545677">GetCommand</a>
</td>
<td align="left" width="63%">
<p>Returns the command string that is executed when a breakpoint is triggered.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545769">GetCurrentPassCount</a>
</td>
<td align="left" width="63%">
<p>Returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546557">GetDataParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters for a processor breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546791">GetFlags</a>
</td>
<td align="left" width="63%">
<p>Returns the flags for a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546827">GetId</a>
</td>
<td align="left" width="63%">
<p>Returns a breakpoint ID, which is the engine's unique identifier for a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547074">GetMatchThreadId</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID of the thread that can trigger a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548008">GetOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the location that triggers a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548048">GetOffsetExpression</a>
</td>
<td align="left" width="63%">
<p>Returns the expression string that evaluates to the location that triggers a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548095">GetParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters for a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548104">GetPassCount</a>
</td>
<td align="left" width="63%">
<p>Returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a>
</td>
<td align="left" width="63%">
<p>Returns the type of the breakpoint and the type of the processor that a breakpoint is set for.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554504">RemoveFlags</a>
</td>
<td align="left" width="63%">
<p>Removes flags from a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556632">SetCommand</a>
</td>
<td align="left" width="63%">
<p>Sets the command that is executed when a breakpoint is triggered.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556655">SetDataParameters</a>
</td>
<td align="left" width="63%">
<p>Sets the parameters for a processor breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556703">SetFlags</a>
</td>
<td align="left" width="63%">
<p>Sets the flags for a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556735">SetMatchThreadId</a>
</td>
<td align="left" width="63%">
<p>Sets the engine thread ID of the thread that can trigger a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556741">SetOffset</a>
</td>
<td align="left" width="63%">
<p>Sets the location that triggers a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556745">SetOffsetExpression</a>
</td>
<td align="left" width="63%">
<p>Sets an expression string that evaluates to the location that triggers a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556759">SetPassCount</a>
</td>
<td align="left" width="63%">
<p>Sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered.
</p>
</td>
</tr>
</table><p>Adds flags to a breakpoint.</p>

<p>Returns the client that owns the breakpoint.</p>

<p>Returns the command string that is executed when a breakpoint is triggered.
</p>

<p>Returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered.</p>

<p>Returns the parameters for a processor breakpoint.</p>

<p>Returns the flags for a breakpoint.</p>

<p>Returns a breakpoint ID, which is the engine's unique identifier for a breakpoint.</p>

<p>Returns the engine thread ID of the thread that can trigger a breakpoint.
</p>

<p>Returns the location that triggers a breakpoint.</p>

<p>Returns the expression string that evaluates to the location that triggers a breakpoint.
</p>

<p>Returns the parameters for a breakpoint.</p>

<p>Returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered.</p>

<p>Returns the type of the breakpoint and the type of the processor that a breakpoint is set for.
</p>

<p>Removes flags from a breakpoint.
</p>

<p>Sets the command that is executed when a breakpoint is triggered.
</p>

<p>Sets the parameters for a processor breakpoint.</p>

<p>Sets the flags for a breakpoint.
</p>

<p>Sets the engine thread ID of the thread that can trigger a breakpoint.
</p>

<p>Sets the location that triggers a breakpoint.</p>

<p>Sets an expression string that evaluates to the location that triggers a breakpoint.
</p>

<p>Sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered.
</p>

<p> </p>

## -remarks
<p>Although <b>IDebugBreakpoint</b> implements the <b>IUnknown</b> interface, the <b>IUnknown::AddRef</b> and <b>IUnknown::Release</b> methods are not used to control the lifetime of the breakpoint. Instead, an <b>IDebugBreakpoint</b> object is deleted after the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff554487">RemoveBreakpoint</a> is called.</p>

<p>Although <b>IDebugBreakpoint</b> implements the <b>IUnknown</b> interface, the <b>IUnknown::AddRef</b> and <b>IUnknown::Release</b> methods are not used to control the lifetime of the breakpoint. Instead, an <b>IDebugBreakpoint</b> object is deleted after the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff554487">RemoveBreakpoint</a> is called.</p>

## -requirements
<table>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549822">IDebugBreakpoint2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

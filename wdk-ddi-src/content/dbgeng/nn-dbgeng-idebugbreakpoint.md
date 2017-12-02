---
UID: NN.dbgeng.IDebugBreakpoint
title: IDebugBreakpoint
author: windows-driver-content
description: IDebugBreakpoint interface
old-location: debugger\idebugbreakpoint.htm
old-project: debugger
ms.assetid: ad4bcabb-304e-4427-9b0d-2e22429e8cdd
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
<a href="debugger.addflags">AddFlags</a>
</td>
<td align="left" width="63%">
<p>Adds flags to a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getadder">GetAdder</a>
</td>
<td align="left" width="63%">
<p>Returns the client that owns the breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcommand">GetCommand</a>
</td>
<td align="left" width="63%">
<p>Returns the command string that is executed when a breakpoint is triggered.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentpasscount">GetCurrentPassCount</a>
</td>
<td align="left" width="63%">
<p>Returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getdataparameters">GetDataParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters for a processor breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getflags">GetFlags</a>
</td>
<td align="left" width="63%">
<p>Returns the flags for a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getid">GetId</a>
</td>
<td align="left" width="63%">
<p>Returns a breakpoint ID, which is the engine's unique identifier for a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmatchthreadid">GetMatchThreadId</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID of the thread that can trigger a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffset">GetOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the location that triggers a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetexpression">GetOffsetExpression</a>
</td>
<td align="left" width="63%">
<p>Returns the expression string that evaluates to the location that triggers a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getparameters">GetParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters for a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getpasscount">GetPassCount</a>
</td>
<td align="left" width="63%">
<p>Returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettype">GetType</a>
</td>
<td align="left" width="63%">
<p>Returns the type of the breakpoint and the type of the processor that a breakpoint is set for.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removeflags">RemoveFlags</a>
</td>
<td align="left" width="63%">
<p>Removes flags from a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setcommand">SetCommand</a>
</td>
<td align="left" width="63%">
<p>Sets the command that is executed when a breakpoint is triggered.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setdataparameters">SetDataParameters</a>
</td>
<td align="left" width="63%">
<p>Sets the parameters for a processor breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setflags">SetFlags</a>
</td>
<td align="left" width="63%">
<p>Sets the flags for a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setmatchthreadid">SetMatchThreadId</a>
</td>
<td align="left" width="63%">
<p>Sets the engine thread ID of the thread that can trigger a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setoffset">SetOffset</a>
</td>
<td align="left" width="63%">
<p>Sets the location that triggers a breakpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setoffsetexpression">SetOffsetExpression</a>
</td>
<td align="left" width="63%">
<p>Sets an expression string that evaluates to the location that triggers a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setpasscount">SetPassCount</a>
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
<p>Although <b>IDebugBreakpoint</b> implements the <b>IUnknown</b> interface, the <b>IUnknown::AddRef</b> and <b>IUnknown::Release</b> methods are not used to control the lifetime of the breakpoint. Instead, an <b>IDebugBreakpoint</b> object is deleted after the method <a href="debugger.removebreakpoint">RemoveBreakpoint</a> is called.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint2.md">IDebugBreakpoint2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint interface%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

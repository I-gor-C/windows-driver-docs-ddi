---
UID: NN.dbgeng.IDebugBreakpoint2
title: IDebugBreakpoint2
author: windows-driver-content
description: IDebugBreakpoint2 interface
old-location: debugger\idebugbreakpoint2.htm
old-project: debugger
ms.assetid: 097c10e1-fd83-4a3d-8193-873644370e35
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DebugCreateEx
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
req.alt-api: IDebugBreakpoint2
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
---

# IDebugBreakpoint2 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugBreakpoint2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugbreakpoint.md">IDebugBreakpoint</a>. <b>IDebugBreakpoint2</b> also has these types of members:

The <b>IDebugBreakpoint2</b> interface has these methods.

Returns the command string that is executed when a breakpoint is triggered.


Returns the expression string that evaluates to the location that triggers a breakpoint.


 Sets the command that is executed when a breakpoint is triggered.


 Sets an expression string that evaluates to the location that triggers a breakpoint.


 

## -members
The <b>IDebugBreakpoint2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcommandwide">GetCommandWide</a>
</td>
<td align="left" width="63%">
Returns the command string that is executed when a breakpoint is triggered.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetexpressionwide">GetOffsetExpressionWide</a>
</td>
<td align="left" width="63%">
Returns the expression string that evaluates to the location that triggers a breakpoint.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setcommandwide">SetCommandWide</a>
</td>
<td align="left" width="63%">
 Sets the command that is executed when a breakpoint is triggered.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setoffsetexpressionwide">SetOffsetExpressionWide</a>
</td>
<td align="left" width="63%">
 Sets an expression string that evaluates to the location that triggers a breakpoint.

</td>
</tr>
</table>Returns the command string that is executed when a breakpoint is triggered.


Returns the expression string that evaluates to the location that triggers a breakpoint.


 Sets the command that is executed when a breakpoint is triggered.


 Sets an expression string that evaluates to the location that triggers a breakpoint.


 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
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
<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint.md">IDebugBreakpoint</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint2 interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

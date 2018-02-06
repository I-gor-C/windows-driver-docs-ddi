---
UID: NN:dbgeng.IDebugBreakpoint2
title: IDebugBreakpoint2
author: windows-driver-content
description: IDebugBreakpoint2 interface
old-location: debugger\idebugbreakpoint2.htm
old-project: debugger
ms.assetid: 097c10e1-fd83-4a3d-8193-873644370e35
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugbreakpoint2, IDebugBreakpoint2 interface [Windows Debugging], IDebugBreakpoint2 interface [Windows Debugging], described, IDebugBreakpoint2, dbgeng/IDebugBreakpoint2
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
-	IDebugBreakpoint2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugBreakpoint2 interface



## Methods

<p>The <b>IDebugBreakpoint2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugBreakpoint2.AddFlags](nf-dbgeng-idebugbreakpoint2-addflags.md) | The AddFlags method adds flags to a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetAdder](nf-dbgeng-idebugbreakpoint2-getadder.md) | The GetAdder method returns the client that owns the breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetCommand](nf-dbgeng-idebugbreakpoint2-getcommand.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [dbgeng.IDebugBreakpoint2.GetCommandWide](nf-dbgeng-idebugbreakpoint2-getcommandwide.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [dbgeng.IDebugBreakpoint2.GetCurrentPassCount](nf-dbgeng-idebugbreakpoint2-getcurrentpasscount.md) | The GetCurrentPassCount method returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [dbgeng.IDebugBreakpoint2.GetDataParameters](nf-dbgeng-idebugbreakpoint2-getdataparameters.md) | The GetDataParameters method returns the parameters for a processor breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetFlags](nf-dbgeng-idebugbreakpoint2-getflags.md) | The GetFlags method returns the flags for a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetId](nf-dbgeng-idebugbreakpoint2-getid.md) | The GetId method returns a breakpoint ID, which is the engine's unique identifier for a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetMatchThreadId](nf-dbgeng-idebugbreakpoint2-getmatchthreadid.md) | The GetMatchThreadId method returns the engine thread ID of the thread that can trigger a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetOffset](nf-dbgeng-idebugbreakpoint2-getoffset.md) | The GetOffset method returns the location that triggers a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetOffsetExpression](nf-dbgeng-idebugbreakpoint2-getoffsetexpression.md) | The GetOffsetExpression methods return the expression string that evaluates to the location that triggers a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetOffsetExpressionWide](nf-dbgeng-idebugbreakpoint2-getoffsetexpressionwide.md) | The GetOffsetExpressionWide method returns the expression string that evaluates to the location that triggers a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetParameters](nf-dbgeng-idebugbreakpoint2-getparameters.md) | The GetParameters method returns the parameters for a breakpoint. |
| [dbgeng.IDebugBreakpoint2.GetPassCount](nf-dbgeng-idebugbreakpoint2-getpasscount.md) | The GetPassCount method returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered. |
| [dbgeng.IDebugBreakpoint2.GetType](nf-dbgeng-idebugbreakpoint2-gettype.md) | The GetType method returns the type of the breakpoint and the type of the processor that a breakpoint is set for. |
| [dbgeng.IDebugBreakpoint2.RemoveFlags](nf-dbgeng-idebugbreakpoint2-removeflags.md) | The RemoveFlags method removes flags from a breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetCommand](nf-dbgeng-idebugbreakpoint2-setcommand.md) | The SetCommand method sets the command that is executed when a breakpoint is triggered. |
| [dbgeng.IDebugBreakpoint2.SetCommandWide](nf-dbgeng-idebugbreakpoint2-setcommandwide.md) | The SetCommandWide method sets the command that is executed when a breakpoint is triggered. |
| [dbgeng.IDebugBreakpoint2.SetDataParameters](nf-dbgeng-idebugbreakpoint2-setdataparameters.md) | The SetDataParameters method sets the parameters for a processor breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetFlags](nf-dbgeng-idebugbreakpoint2-setflags.md) | The SetFlags method sets the flags for a breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetMatchThreadId](nf-dbgeng-idebugbreakpoint2-setmatchthreadid.md) | The SetMatchThreadId method sets the engine thread ID of the thread that can trigger a breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetOffset](nf-dbgeng-idebugbreakpoint2-setoffset.md) | The SetOffset method sets the location that triggers a breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetOffsetExpression](nf-dbgeng-idebugbreakpoint2-setoffsetexpression.md) | The SetOffsetExpression methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetOffsetExpressionWide](nf-dbgeng-idebugbreakpoint2-setoffsetexpressionwide.md) | The SetOffsetExpressionWide methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [dbgeng.IDebugBreakpoint2.SetPassCount](nf-dbgeng-idebugbreakpoint2-setpasscount.md) | The SetPassCount method sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint.md">IDebugBreakpoint</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint2 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
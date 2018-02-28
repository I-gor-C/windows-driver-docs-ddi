---
UID: NN:dbgeng.IDebugBreakpoint
title: IDebugBreakpoint
author: windows-driver-content
description: IDebugBreakpoint interface
old-location: debugger\idebugbreakpoint.htm
old-project: debugger
ms.assetid: ad4bcabb-304e-4427-9b0d-2e22429e8cdd
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: ComOther_93345db9-13c0-4b46-be4a-d3fbb6039cc7.xml, IDebugBreakpoint, IDebugBreakpoint interface [Windows Debugging], IDebugBreakpoint interface [Windows Debugging], described, dbgeng/IDebugBreakpoint, debugger.idebugbreakpoint
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugBreakpoint
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugBreakpoint interface



## Methods

<p>The <b>IDebugBreakpoint</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugBreakpoint::AddFlags](nf-dbgeng-idebugbreakpoint-addflags.md) | The AddFlags method adds flags to a breakpoint. |
| [IDebugBreakpoint::GetAdder](nf-dbgeng-idebugbreakpoint-getadder.md) | The GetAdder method returns the client that owns the breakpoint. |
| [IDebugBreakpoint::GetCommand](nf-dbgeng-idebugbreakpoint-getcommand.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint::GetCurrentPassCount](nf-dbgeng-idebugbreakpoint-getcurrentpasscount.md) | The GetCurrentPassCount method returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [IDebugBreakpoint::GetDataParameters](nf-dbgeng-idebugbreakpoint-getdataparameters.md) | The GetDataParameters method returns the parameters for a processor breakpoint. |
| [IDebugBreakpoint::GetFlags](nf-dbgeng-idebugbreakpoint-getflags.md) | The GetFlags method returns the flags for a breakpoint. |
| [IDebugBreakpoint::GetId](nf-dbgeng-idebugbreakpoint-getid.md) | The GetId method returns a breakpoint ID, which is the engine's unique identifier for a breakpoint. |
| [IDebugBreakpoint::GetMatchThreadId](nf-dbgeng-idebugbreakpoint-getmatchthreadid.md) | The GetMatchThreadId method returns the engine thread ID of the thread that can trigger a breakpoint. |
| [IDebugBreakpoint::GetOffset](nf-dbgeng-idebugbreakpoint-getoffset.md) | The GetOffset method returns the location that triggers a breakpoint. |
| [IDebugBreakpoint::GetOffsetExpression](nf-dbgeng-idebugbreakpoint-getoffsetexpression.md) | The GetOffsetExpression methods return the expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugBreakpoint::GetParameters](nf-dbgeng-idebugbreakpoint-getparameters.md) | The GetParameters method returns the parameters for a breakpoint. |
| [IDebugBreakpoint::GetPassCount](nf-dbgeng-idebugbreakpoint-getpasscount.md) | The GetPassCount method returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered. |
| [IDebugBreakpoint::GetType](nf-dbgeng-idebugbreakpoint-gettype.md) | The GetType method returns the type of the breakpoint and the type of the processor that a breakpoint is set for. |
| [IDebugBreakpoint::RemoveFlags](nf-dbgeng-idebugbreakpoint-removeflags.md) | The RemoveFlags method removes flags from a breakpoint. |
| [IDebugBreakpoint::SetCommand](nf-dbgeng-idebugbreakpoint-setcommand.md) | The SetCommand method sets the command that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint::SetDataParameters](nf-dbgeng-idebugbreakpoint-setdataparameters.md) | The SetDataParameters method sets the parameters for a processor breakpoint. |
| [IDebugBreakpoint::SetFlags](nf-dbgeng-idebugbreakpoint-setflags.md) | The SetFlags method sets the flags for a breakpoint. |
| [IDebugBreakpoint::SetMatchThreadId](nf-dbgeng-idebugbreakpoint-setmatchthreadid.md) | The SetMatchThreadId method sets the engine thread ID of the thread that can trigger a breakpoint. |
| [IDebugBreakpoint::SetOffset](nf-dbgeng-idebugbreakpoint-setoffset.md) | The SetOffset method sets the location that triggers a breakpoint. |
| [IDebugBreakpoint::SetOffsetExpression](nf-dbgeng-idebugbreakpoint-setoffsetexpression.md) | The SetOffsetExpression methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugBreakpoint::SetPassCount](nf-dbgeng-idebugbreakpoint-setpasscount.md) | The SetPassCount method sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered. |

## Remarks

Although <b>IDebugBreakpoint</b> implements the <b>IUnknown</b> interface, the <b>IUnknown::AddRef</b> and <b>IUnknown::Release</b> methods are not used to control the lifetime of the breakpoint. Instead, an <b>IDebugBreakpoint</b> object is deleted after the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff554487">RemoveBreakpoint</a> is called.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint2.md">IDebugBreakpoint2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint interface%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
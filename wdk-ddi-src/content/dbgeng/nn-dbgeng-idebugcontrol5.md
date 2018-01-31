---
UID : NN:dbgeng.IDebugControl5
title : IDebugControl5
author : windows-driver-content
description : "."
old-location : debugger\idebugcontrol5.htm
old-project : debugger
ms.assetid : 6C358D49-970D-4687-B16E-7D1B44CB0A8E
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : debugger.idebugcontrol5, IDebugControl5 interface [Windows Debugging], IDebugControl5 interface [Windows Debugging], described, IDebugControl5, dbgeng/IDebugControl5
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dbgeng.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugControl5 interface



## Methods

<p>The <b>IDebugControl5</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugControl5.GetBreakpointByGuid](nf-dbgeng-idebugcontrol5-getbreakpointbyguid.md) | The GetBreakpointByGuid method returns the breakpoint with the specified breakpoint GUID. |
| [dbgeng.IDebugControl5.GetContextStackTraceEx](nf-dbgeng-idebugcontrol5-getcontextstacktraceex.md) | The GetContextStackTraceEx method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [dbgeng.IDebugControl5.GetStackTraceEx](nf-dbgeng-idebugcontrol5-getstacktraceex.md) | The GetStackTraceEx method returns the frames at the top of the specified call stack. The GetStackTraceEx method provides inline frame support. For more information about working with inline functions, see Debugging Optimized Code and Inline Functions. |
| [dbgeng.IDebugControl5.OutputContextStackTraceEx](nf-dbgeng-idebugcontrol5-outputcontextstacktraceex.md) | The OutputContextStackTraceEx method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [dbgeng.IDebugControl5.OutputStackTraceEx](nf-dbgeng-idebugcontrol5-outputstacktraceex.md) | The OutputStackTraceEx method outputs either the supplied stack frame or the current stack frames. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **DLL** |  |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>

<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>

<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>

<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl5 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
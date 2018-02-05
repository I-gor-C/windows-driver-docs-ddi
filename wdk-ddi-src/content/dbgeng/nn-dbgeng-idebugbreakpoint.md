---
UID : NN:dbgeng.IDebugBreakpoint
title : IDebugBreakpoint
author : windows-driver-content
description : IDebugBreakpoint interface
old-location : debugger\idebugbreakpoint.htm
old-project : debugger
ms.assetid : ad4bcabb-304e-4427-9b0d-2e22429e8cdd
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : debugger.idebugbreakpoint, IDebugBreakpoint interface [Windows Debugging], IDebugBreakpoint interface [Windows Debugging], described, IDebugBreakpoint, dbgeng/IDebugBreakpoint, ComOther_93345db9-13c0-4b46-be4a-d3fbb6039cc7.xml
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

# IDebugBreakpoint interface



## Methods

<p>The <b>IDebugBreakpoint</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |

## Remarks

Although <b>IDebugBreakpoint</b> implements the <b>IUnknown</b> interface, the <b>IUnknown::AddRef</b> and <b>IUnknown::Release</b> methods are not used to control the lifetime of the breakpoint. Instead, an <b>IDebugBreakpoint</b> object is deleted after the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff554487">RemoveBreakpoint</a> is called.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint2.md">IDebugBreakpoint2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
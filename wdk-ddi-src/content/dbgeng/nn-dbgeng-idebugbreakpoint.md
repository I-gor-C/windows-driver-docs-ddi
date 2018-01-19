---
UID : NN:dbgeng.IDebugBreakpoint
title : IDebugBreakpoint
author : windows-driver-content
description : IDebugBreakpoint interface
old-location : debugger\idebugbreakpoint.htm
old-project : debugger
ms.assetid : ad4bcabb-304e-4427-9b0d-2e22429e8cdd
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::SetImplicitThreadDataOffset, SetImplicitThreadDataOffset
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
req.alt-api : IDebugBreakpoint
req.alt-loc : dbgeng.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
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
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint2.md">IDebugBreakpoint2</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugBreakpoint interface%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
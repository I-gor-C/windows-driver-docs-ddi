---
UID: NN:dbgeng.IDebugRegisters
title: IDebugRegisters
author: windows-driver-content
description: IDebugRegisters interface
old-location: debugger\idebugregisters.htm
old-project: Debugger
ms.assetid: a2587ea7-20cd-43be-ba71-750e699ee0ce
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: debugger.idebugregisters, IDebugRegisters interface [Windows Debugging], IDebugRegisters interface [Windows Debugging], described, IDebugRegisters, dbgeng/IDebugRegisters, IDebugRegisters_ca710692-a977-4276-b779-2b66311938dc.xml
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
-	IDebugRegisters
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugRegisters interface



## Methods

<p>The <b>IDebugRegisters</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugRegisters.GetDescription](nf-dbgeng-idebugregisters-getdescription.md) | The GetDescription method returns the description of a register. |
| [dbgeng.IDebugRegisters.GetFrameOffset](nf-dbgeng-idebugregisters-getframeoffset.md) | The GetFrameOffset method returns the location of the stack frame for the current function. |
| [dbgeng.IDebugRegisters.GetIndexByName](nf-dbgeng-idebugregisters-getindexbyname.md) | The GetIndexByName method returns the index of the named register. |
| [dbgeng.IDebugRegisters.GetInstructionOffset](nf-dbgeng-idebugregisters-getinstructionoffset.md) | The GetInstructionOffset method returns the location of the current thread's current instruction. |
| [dbgeng.IDebugRegisters.GetNumberRegisters](nf-dbgeng-idebugregisters-getnumberregisters.md) | The GetNumberRegisters method returns the number of registers on the target computer. |
| [dbgeng.IDebugRegisters.GetStackOffset](nf-dbgeng-idebugregisters-getstackoffset.md) | The GetStackOffset method returns the current thread's current stack location. |
| [dbgeng.IDebugRegisters.GetValue](nf-dbgeng-idebugregisters-getvalue.md) | The GetValue method gets the value of one of the target's registers. |
| [dbgeng.IDebugRegisters.GetValues](nf-dbgeng-idebugregisters-getvalues.md) | The GetValues method gets the value of several of the target's registers. |
| [dbgeng.IDebugRegisters.OutputRegisters](nf-dbgeng-idebugregisters-outputregisters.md) | The OutputRegisters method formats and sends the target's registers to the clients as output. |
| [dbgeng.IDebugRegisters.SetValue](nf-dbgeng-idebugregisters-setvalue.md) | The SetValue method sets the value of one of the target's registers. |
| [dbgeng.IDebugRegisters.SetValues](nf-dbgeng-idebugregisters-setvalues.md) | The SetValues method sets the value of several of the target's registers. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugregisters2.md">IDebugRegisters2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugRegisters interface%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
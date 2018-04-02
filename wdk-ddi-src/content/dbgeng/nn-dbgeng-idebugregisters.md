---
UID: NN:dbgeng.IDebugRegisters
title: IDebugRegisters
author: windows-driver-content
description: IDebugRegisters interface
old-location: debugger\idebugregisters.htm
old-project: debugger
ms.assetid: a2587ea7-20cd-43be-ba71-750e699ee0ce
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugRegisters, IDebugRegisters interface [Windows Debugging], IDebugRegisters interface [Windows Debugging], described, IDebugRegisters_ca710692-a977-4276-b779-2b66311938dc.xml, dbgeng/IDebugRegisters, debugger.idebugregisters
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
req.lib: 
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
-	IDebugRegisters
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugRegisters interface



## Methods

<p>The <b>IDebugRegisters</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugRegisters::GetDescription](nf-dbgeng-idebugregisters-getdescription.md) | The GetDescription method returns the description of a register. |
| [IDebugRegisters::GetFrameOffset](nf-dbgeng-idebugregisters-getframeoffset.md) | The GetFrameOffset method returns the location of the stack frame for the current function. |
| [IDebugRegisters::GetIndexByName](nf-dbgeng-idebugregisters-getindexbyname.md) | The GetIndexByName method returns the index of the named register. |
| [IDebugRegisters::GetInstructionOffset](nf-dbgeng-idebugregisters-getinstructionoffset.md) | The GetInstructionOffset method returns the location of the current thread's current instruction. |
| [IDebugRegisters::GetNumberRegisters](nf-dbgeng-idebugregisters-getnumberregisters.md) | The GetNumberRegisters method returns the number of registers on the target computer. |
| [IDebugRegisters::GetStackOffset](nf-dbgeng-idebugregisters-getstackoffset.md) | The GetStackOffset method returns the current thread's current stack location. |
| [IDebugRegisters::GetValue](nf-dbgeng-idebugregisters-getvalue.md) | The GetValue method gets the value of one of the target's registers. |
| [IDebugRegisters::GetValues](nf-dbgeng-idebugregisters-getvalues.md) | The GetValues method gets the value of several of the target's registers. |
| [IDebugRegisters::OutputRegisters](nf-dbgeng-idebugregisters-outputregisters.md) | The OutputRegisters method formats and sends the target's registers to the clients as output. |
| [IDebugRegisters::SetValue](nf-dbgeng-idebugregisters-setvalue.md) | The SetValue method sets the value of one of the target's registers. |
| [IDebugRegisters::SetValues](nf-dbgeng-idebugregisters-setvalues.md) | The SetValues method sets the value of several of the target's registers. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550835">IDebugRegisters2</a>
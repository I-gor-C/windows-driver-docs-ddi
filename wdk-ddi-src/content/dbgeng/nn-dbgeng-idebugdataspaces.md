---
UID: NN:dbgeng.IDebugDataSpaces
title: IDebugDataSpaces
author: windows-driver-content
description: IDebugDataSpaces interface
old-location: debugger\idebugdataspaces.htm
old-project: debugger
ms.assetid: 9477821c-4f4f-4ea2-9968-d43f87c496b2
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugDataSpaces, IDebugDataSpaces interface [Windows Debugging], IDebugDataSpaces interface [Windows Debugging], described, IDebugDataSpaces_83f3a88c-f7e6-4b5c-a2b2-4e8bccef4281.xml, dbgeng/IDebugDataSpaces, debugger.idebugdataspaces
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
-	IDebugDataSpaces
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugDataSpaces interface



## Methods

<p>The <b>IDebugDataSpaces</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugDataSpaces::CheckLowMemory](nf-dbgeng-idebugdataspaces-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [IDebugDataSpaces::ReadBusData](nf-dbgeng-idebugdataspaces-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [IDebugDataSpaces::ReadControl](nf-dbgeng-idebugdataspaces-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [IDebugDataSpaces::ReadDebuggerData](nf-dbgeng-idebugdataspaces-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [IDebugDataSpaces::ReadIo](nf-dbgeng-idebugdataspaces-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [IDebugDataSpaces::ReadMsr](nf-dbgeng-idebugdataspaces-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [IDebugDataSpaces::ReadPhysical](nf-dbgeng-idebugdataspaces-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [IDebugDataSpaces::ReadPointersVirtual](nf-dbgeng-idebugdataspaces-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [IDebugDataSpaces::ReadProcessorSystemData](nf-dbgeng-idebugdataspaces-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [IDebugDataSpaces::ReadVirtual](nf-dbgeng-idebugdataspaces-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [IDebugDataSpaces::ReadVirtualUncached](nf-dbgeng-idebugdataspaces-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [IDebugDataSpaces::SearchVirtual](nf-dbgeng-idebugdataspaces-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [IDebugDataSpaces::WriteBusData](nf-dbgeng-idebugdataspaces-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [IDebugDataSpaces::WriteControl](nf-dbgeng-idebugdataspaces-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [IDebugDataSpaces::WriteIo](nf-dbgeng-idebugdataspaces-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [IDebugDataSpaces::WriteMsr](nf-dbgeng-idebugdataspaces-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [IDebugDataSpaces::WritePhysical](nf-dbgeng-idebugdataspaces-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [IDebugDataSpaces::WritePointersVirtual](nf-dbgeng-idebugdataspaces-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [IDebugDataSpaces::WriteVirtual](nf-dbgeng-idebugdataspaces-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [IDebugDataSpaces::WriteVirtualUncached](nf-dbgeng-idebugdataspaces-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550537">IDebugDataSpaces3</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550546">IDebugDataSpaces4</a>
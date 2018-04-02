---
UID: NN:dbgeng.IDebugDataSpaces3
title: IDebugDataSpaces3
author: windows-driver-content
description: IDebugDataSpaces3 interface
old-location: debugger\idebugdataspaces3.htm
old-project: debugger
ms.assetid: a5da1ed0-c4e6-4ab8-b581-64bc7d0519f2
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugDataSpaces3, IDebugDataSpaces3 interface [Windows Debugging], IDebugDataSpaces3 interface [Windows Debugging], described, dbgeng/IDebugDataSpaces3, debugger.idebugdataspaces3
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
-	IDebugDataSpaces3
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugDataSpaces3 interface



## Methods

<p>The <b>IDebugDataSpaces3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugDataSpaces3::CheckLowMemory](nf-dbgeng-idebugdataspaces3-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [IDebugDataSpaces3::EndEnumTagged](nf-dbgeng-idebugdataspaces3-endenumtagged.md) | The EndEnumTagged method releases the resources used by the specified enumeration. |
| [IDebugDataSpaces3::FillPhysical](nf-dbgeng-idebugdataspaces3-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces3::FillVirtual](nf-dbgeng-idebugdataspaces3-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces3::GetNextTagged](nf-dbgeng-idebugdataspaces3-getnexttagged.md) | The GetNextTagged method returns the GUID for the next block of tagged data in the enumeration. |
| [IDebugDataSpaces3::GetVirtualTranslationPhysicalOffsets](nf-dbgeng-idebugdataspaces3-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [IDebugDataSpaces3::ReadBusData](nf-dbgeng-idebugdataspaces3-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [IDebugDataSpaces3::ReadControl](nf-dbgeng-idebugdataspaces3-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [IDebugDataSpaces3::ReadDebuggerData](nf-dbgeng-idebugdataspaces3-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [IDebugDataSpaces3::ReadHandleData](nf-dbgeng-idebugdataspaces3-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [IDebugDataSpaces3::ReadImageNtHeaders](nf-dbgeng-idebugdataspaces3-readimagentheaders.md) | The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target. |
| [IDebugDataSpaces3::ReadIo](nf-dbgeng-idebugdataspaces3-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [IDebugDataSpaces3::ReadMsr](nf-dbgeng-idebugdataspaces3-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [IDebugDataSpaces3::ReadPhysical](nf-dbgeng-idebugdataspaces3-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [IDebugDataSpaces3::ReadPointersVirtual](nf-dbgeng-idebugdataspaces3-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [IDebugDataSpaces3::ReadProcessorSystemData](nf-dbgeng-idebugdataspaces3-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [IDebugDataSpaces3::ReadTagged](nf-dbgeng-idebugdataspaces3-readtagged.md) | The ReadTagged method reads the tagged data that might be associated with a debugger session. |
| [IDebugDataSpaces3::ReadVirtual](nf-dbgeng-idebugdataspaces3-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [IDebugDataSpaces3::ReadVirtualUncached](nf-dbgeng-idebugdataspaces3-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [IDebugDataSpaces3::SearchVirtual](nf-dbgeng-idebugdataspaces3-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [IDebugDataSpaces3::StartEnumTagged](nf-dbgeng-idebugdataspaces3-startenumtagged.md) | The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session. |
| [IDebugDataSpaces3::VirtualToPhysical](nf-dbgeng-idebugdataspaces3-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [IDebugDataSpaces3::WriteBusData](nf-dbgeng-idebugdataspaces3-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [IDebugDataSpaces3::WriteControl](nf-dbgeng-idebugdataspaces3-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [IDebugDataSpaces3::WriteIo](nf-dbgeng-idebugdataspaces3-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [IDebugDataSpaces3::WriteMsr](nf-dbgeng-idebugdataspaces3-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [IDebugDataSpaces3::WritePhysical](nf-dbgeng-idebugdataspaces3-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [IDebugDataSpaces3::WritePointersVirtual](nf-dbgeng-idebugdataspaces3-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [IDebugDataSpaces3::WriteVirtual](nf-dbgeng-idebugdataspaces3-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [IDebugDataSpaces3::WriteVirtualUncached](nf-dbgeng-idebugdataspaces3-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550528">IDebugDataSpaces</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550546">IDebugDataSpaces4</a>
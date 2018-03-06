---
UID: NN:dbgeng.IDebugDataSpaces2
title: IDebugDataSpaces2
author: windows-driver-content
description: IDebugDataSpaces2 interface
old-location: debugger\idebugdataspaces2.htm
old-project: debugger
ms.assetid: a8548f9c-5cb6-4a13-b37c-da28d316b8e1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IDebugDataSpaces2, IDebugDataSpaces2 interface [Windows Debugging], IDebugDataSpaces2 interface [Windows Debugging], described, dbgeng/IDebugDataSpaces2, debugger.idebugdataspaces2
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
-	IDebugDataSpaces2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugDataSpaces2 interface



## Methods

<p>The <b>IDebugDataSpaces2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugDataSpaces2::CheckLowMemory](nf-dbgeng-idebugdataspaces2-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [IDebugDataSpaces2::FillPhysical](nf-dbgeng-idebugdataspaces2-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces2::FillVirtual](nf-dbgeng-idebugdataspaces2-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces2::GetVirtualTranslationPhysicalOffsets](nf-dbgeng-idebugdataspaces2-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [IDebugDataSpaces2::QueryVirtual](nf-dbgeng-idebugdataspaces2-queryvirtual.md) | The QueryVirtual method provides information about the specified pages in the target's virtual address space. |
| [IDebugDataSpaces2::ReadBusData](nf-dbgeng-idebugdataspaces2-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [IDebugDataSpaces2::ReadControl](nf-dbgeng-idebugdataspaces2-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [IDebugDataSpaces2::ReadDebuggerData](nf-dbgeng-idebugdataspaces2-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [IDebugDataSpaces2::ReadHandleData](nf-dbgeng-idebugdataspaces2-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [IDebugDataSpaces2::ReadIo](nf-dbgeng-idebugdataspaces2-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [IDebugDataSpaces2::ReadMsr](nf-dbgeng-idebugdataspaces2-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [IDebugDataSpaces2::ReadPhysical](nf-dbgeng-idebugdataspaces2-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [IDebugDataSpaces2::ReadPointersVirtual](nf-dbgeng-idebugdataspaces2-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [IDebugDataSpaces2::ReadProcessorSystemData](nf-dbgeng-idebugdataspaces2-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [IDebugDataSpaces2::ReadVirtual](nf-dbgeng-idebugdataspaces2-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [IDebugDataSpaces2::ReadVirtualUncached](nf-dbgeng-idebugdataspaces2-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [IDebugDataSpaces2::SearchVirtual](nf-dbgeng-idebugdataspaces2-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [IDebugDataSpaces2::VirtualToPhysical](nf-dbgeng-idebugdataspaces2-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [IDebugDataSpaces2::WriteBusData](nf-dbgeng-idebugdataspaces2-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [IDebugDataSpaces2::WriteControl](nf-dbgeng-idebugdataspaces2-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [IDebugDataSpaces2::WriteIo](nf-dbgeng-idebugdataspaces2-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [IDebugDataSpaces2::WriteMsr](nf-dbgeng-idebugdataspaces2-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [IDebugDataSpaces2::WritePhysical](nf-dbgeng-idebugdataspaces2-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [IDebugDataSpaces2::WritePointersVirtual](nf-dbgeng-idebugdataspaces2-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [IDebugDataSpaces2::WriteVirtual](nf-dbgeng-idebugdataspaces2-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [IDebugDataSpaces2::WriteVirtualUncached](nf-dbgeng-idebugdataspaces2-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugdataspaces3.md">IDebugDataSpaces3</a>



<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>



<a href="..\dbgeng\nn-dbgeng-idebugdataspaces.md">IDebugDataSpaces</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces2 interface%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
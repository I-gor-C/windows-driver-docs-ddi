---
UID: NN:dbgeng.IDebugDataSpaces3
title: IDebugDataSpaces3
author: windows-driver-content
description: IDebugDataSpaces3 interface
old-location: debugger\idebugdataspaces3.htm
old-project: debugger
ms.assetid: a5da1ed0-c4e6-4ab8-b581-64bc7d0519f2
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugdataspaces3, IDebugDataSpaces3 interface [Windows Debugging], IDebugDataSpaces3 interface [Windows Debugging], described, IDebugDataSpaces3, dbgeng/IDebugDataSpaces3
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
-	IDebugDataSpaces3
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugDataSpaces3 interface



## Methods

<p>The <b>IDebugDataSpaces3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugDataSpaces3.CheckLowMemory](nf-dbgeng-idebugdataspaces3-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [dbgeng.IDebugDataSpaces3.EndEnumTagged](nf-dbgeng-idebugdataspaces3-endenumtagged.md) | The EndEnumTagged method releases the resources used by the specified enumeration. |
| [dbgeng.IDebugDataSpaces3.FillPhysical](nf-dbgeng-idebugdataspaces3-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [dbgeng.IDebugDataSpaces3.FillVirtual](nf-dbgeng-idebugdataspaces3-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [dbgeng.IDebugDataSpaces3.GetNextTagged](nf-dbgeng-idebugdataspaces3-getnexttagged.md) | The GetNextTagged method returns the GUID for the next block of tagged data in the enumeration. |
| [dbgeng.IDebugDataSpaces3.GetVirtualTranslationPhysicalOffsets](nf-dbgeng-idebugdataspaces3-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [dbgeng.IDebugDataSpaces3.ReadBusData](nf-dbgeng-idebugdataspaces3-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [dbgeng.IDebugDataSpaces3.ReadControl](nf-dbgeng-idebugdataspaces3-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [dbgeng.IDebugDataSpaces3.ReadDebuggerData](nf-dbgeng-idebugdataspaces3-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [dbgeng.IDebugDataSpaces3.ReadHandleData](nf-dbgeng-idebugdataspaces3-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [dbgeng.IDebugDataSpaces3.ReadImageNtHeaders](nf-dbgeng-idebugdataspaces3-readimagentheaders.md) | The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target. |
| [dbgeng.IDebugDataSpaces3.ReadIo](nf-dbgeng-idebugdataspaces3-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [dbgeng.IDebugDataSpaces3.ReadMsr](nf-dbgeng-idebugdataspaces3-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [dbgeng.IDebugDataSpaces3.ReadPhysical](nf-dbgeng-idebugdataspaces3-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [dbgeng.IDebugDataSpaces3.ReadPointersVirtual](nf-dbgeng-idebugdataspaces3-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces3.ReadProcessorSystemData](nf-dbgeng-idebugdataspaces3-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [dbgeng.IDebugDataSpaces3.ReadTagged](nf-dbgeng-idebugdataspaces3-readtagged.md) | The ReadTagged method reads the tagged data that might be associated with a debugger session. |
| [dbgeng.IDebugDataSpaces3.ReadVirtual](nf-dbgeng-idebugdataspaces3-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces3.ReadVirtualUncached](nf-dbgeng-idebugdataspaces3-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces3.SearchVirtual](nf-dbgeng-idebugdataspaces3-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [dbgeng.IDebugDataSpaces3.StartEnumTagged](nf-dbgeng-idebugdataspaces3-startenumtagged.md) | The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session. |
| [dbgeng.IDebugDataSpaces3.VirtualToPhysical](nf-dbgeng-idebugdataspaces3-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [dbgeng.IDebugDataSpaces3.WriteBusData](nf-dbgeng-idebugdataspaces3-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [dbgeng.IDebugDataSpaces3.WriteControl](nf-dbgeng-idebugdataspaces3-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [dbgeng.IDebugDataSpaces3.WriteIo](nf-dbgeng-idebugdataspaces3-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [dbgeng.IDebugDataSpaces3.WriteMsr](nf-dbgeng-idebugdataspaces3-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [dbgeng.IDebugDataSpaces3.WritePhysical](nf-dbgeng-idebugdataspaces3-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [dbgeng.IDebugDataSpaces3.WritePointersVirtual](nf-dbgeng-idebugdataspaces3-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [dbgeng.IDebugDataSpaces3.WriteVirtual](nf-dbgeng-idebugdataspaces3-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [dbgeng.IDebugDataSpaces3.WriteVirtualUncached](nf-dbgeng-idebugdataspaces3-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugdataspaces2.md">IDebugDataSpaces2</a>



<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>



<a href="..\dbgeng\nn-dbgeng-idebugdataspaces.md">IDebugDataSpaces</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces3 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
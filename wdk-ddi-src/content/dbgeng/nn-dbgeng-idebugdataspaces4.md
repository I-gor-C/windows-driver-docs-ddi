---
UID: NN:dbgeng.IDebugDataSpaces4
title: IDebugDataSpaces4
author: windows-driver-content
description: IDebugDataSpaces4 interface
old-location: debugger\idebugdataspaces4.htm
old-project: debugger
ms.assetid: e03202a5-2e4a-43f8-8183-fdd26df6ff8f
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugdataspaces4, IDebugDataSpaces4 interface [Windows Debugging], IDebugDataSpaces4 interface [Windows Debugging], described, IDebugDataSpaces4, dbgeng/IDebugDataSpaces4
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
-	IDebugDataSpaces4
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugDataSpaces4 interface



## Methods

<p>The <b>IDebugDataSpaces4</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugDataSpaces4.CheckLowMemory](nf-dbgeng-idebugdataspaces4-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [dbgeng.IDebugDataSpaces4.EndEnumTagged](nf-dbgeng-idebugdataspaces4-endenumtagged.md) | The EndEnumTagged method releases the resources used by the specified enumeration. |
| [dbgeng.IDebugDataSpaces4.FillPhysical](nf-dbgeng-idebugdataspaces4-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [dbgeng.IDebugDataSpaces4.FillVirtual](nf-dbgeng-idebugdataspaces4-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [dbgeng.IDebugDataSpaces4.GetNextDifferentlyValidOffsetVirtual](nf-dbgeng-idebugdataspaces4-getnextdifferentlyvalidoffsetvirtual.md) | The GetNextDifferentlyValidOffsetVirtual method returns the offset of the next address whose validity might be different from the validity of the specified address. |
| [dbgeng.IDebugDataSpaces4.GetNextTagged](nf-dbgeng-idebugdataspaces4-getnexttagged.md) | The GetNextTagged method returns the GUID for the next block of tagged data in the enumeration. |
| [dbgeng.IDebugDataSpaces4.GetOffsetInformation](nf-dbgeng-idebugdataspaces4-getoffsetinformation.md) | The GetOffsetInformation method provides general information about an address in a process's data space. |
| [dbgeng.IDebugDataSpaces4.GetValidRegionVirtual](nf-dbgeng-idebugdataspaces4-getvalidregionvirtual.md) | The GetValidRegionVirtual method locates the first valid region of memory in a specified memory range. |
| [dbgeng.IDebugDataSpaces4.GetVirtualTranslationPhysicalOffsets](nf-dbgeng-idebugdataspaces4-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [dbgeng.IDebugDataSpaces4.ReadBusData](nf-dbgeng-idebugdataspaces4-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [dbgeng.IDebugDataSpaces4.ReadControl](nf-dbgeng-idebugdataspaces4-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [dbgeng.IDebugDataSpaces4.ReadDebuggerData](nf-dbgeng-idebugdataspaces4-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [dbgeng.IDebugDataSpaces4.ReadHandleData](nf-dbgeng-idebugdataspaces4-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [dbgeng.IDebugDataSpaces4.ReadImageNtHeaders](nf-dbgeng-idebugdataspaces4-readimagentheaders.md) | The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target. |
| [dbgeng.IDebugDataSpaces4.ReadIo](nf-dbgeng-idebugdataspaces4-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [dbgeng.IDebugDataSpaces4.ReadMsr](nf-dbgeng-idebugdataspaces4-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [dbgeng.IDebugDataSpaces4.ReadMultiByteStringVirtual](nf-dbgeng-idebugdataspaces4-readmultibytestringvirtual.md) | The ReadMultiByteStringVirtual method reads a null-terminated, multibyte string from the target. |
| [dbgeng.IDebugDataSpaces4.ReadMultiByteStringVirtualWide](nf-dbgeng-idebugdataspaces4-readmultibytestringvirtualwide.md) | The ReadMultiByteStringVirtualWide method reads a null-terminated, multibyte string from the target and converts it to Unicode. |
| [dbgeng.IDebugDataSpaces4.ReadPhysical](nf-dbgeng-idebugdataspaces4-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [dbgeng.IDebugDataSpaces4.ReadPhysical2](nf-dbgeng-idebugdataspaces4-readphysical2.md) | The ReadPhysical2 method reads the target's memory from the specified physical address. |
| [dbgeng.IDebugDataSpaces4.ReadPointersVirtual](nf-dbgeng-idebugdataspaces4-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces4.ReadProcessorSystemData](nf-dbgeng-idebugdataspaces4-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [dbgeng.IDebugDataSpaces4.ReadTagged](nf-dbgeng-idebugdataspaces4-readtagged.md) | The ReadTagged method reads the tagged data that might be associated with a debugger session. |
| [dbgeng.IDebugDataSpaces4.ReadUnicodeStringVirtual](nf-dbgeng-idebugdataspaces4-readunicodestringvirtual.md) | The ReadUnicodeStringVirtual method reads a null-terminated, Unicode string from the target and converts it to a multibyte string. |
| [dbgeng.IDebugDataSpaces4.ReadUnicodeStringVirtualWide](nf-dbgeng-idebugdataspaces4-readunicodestringvirtualwide.md) | The ReadUnicodeStringVirtualWide method reads a null-terminated, Unicode string from the target. |
| [dbgeng.IDebugDataSpaces4.ReadVirtual](nf-dbgeng-idebugdataspaces4-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces4.ReadVirtualUncached](nf-dbgeng-idebugdataspaces4-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces4.SearchVirtual](nf-dbgeng-idebugdataspaces4-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [dbgeng.IDebugDataSpaces4.SearchVirtual2](nf-dbgeng-idebugdataspaces4-searchvirtual2.md) | The SearchVirtual2 method searches the process's virtual memory for a specified pattern of bytes. |
| [dbgeng.IDebugDataSpaces4.StartEnumTagged](nf-dbgeng-idebugdataspaces4-startenumtagged.md) | The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session. |
| [dbgeng.IDebugDataSpaces4.VirtualToPhysical](nf-dbgeng-idebugdataspaces4-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [dbgeng.IDebugDataSpaces4.WriteBusData](nf-dbgeng-idebugdataspaces4-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [dbgeng.IDebugDataSpaces4.WriteControl](nf-dbgeng-idebugdataspaces4-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [dbgeng.IDebugDataSpaces4.WriteIo](nf-dbgeng-idebugdataspaces4-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [dbgeng.IDebugDataSpaces4.WriteMsr](nf-dbgeng-idebugdataspaces4-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [dbgeng.IDebugDataSpaces4.WritePhysical](nf-dbgeng-idebugdataspaces4-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [dbgeng.IDebugDataSpaces4.WritePhysical2](nf-dbgeng-idebugdataspaces4-writephysical2.md) | The WritePhysical2 method writes data to the specified physical address in the target's memory. |
| [dbgeng.IDebugDataSpaces4.WritePointersVirtual](nf-dbgeng-idebugdataspaces4-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [dbgeng.IDebugDataSpaces4.WriteVirtual](nf-dbgeng-idebugdataspaces4-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [dbgeng.IDebugDataSpaces4.WriteVirtualUncached](nf-dbgeng-idebugdataspaces4-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugdataspaces3.md">IDebugDataSpaces3</a>

<a href="..\dbgeng\nn-dbgeng-idebugdataspaces.md">IDebugDataSpaces</a>

<a href="..\dbgeng\nn-dbgeng-idebugdataspaces2.md">IDebugDataSpaces2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces4 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
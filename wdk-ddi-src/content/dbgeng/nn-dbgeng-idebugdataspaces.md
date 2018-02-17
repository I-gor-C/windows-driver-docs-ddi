---
UID: NN:dbgeng.IDebugDataSpaces
title: IDebugDataSpaces
author: windows-driver-content
description: IDebugDataSpaces interface
old-location: debugger\idebugdataspaces.htm
old-project: debugger
ms.assetid: 9477821c-4f4f-4ea2-9968-d43f87c496b2
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugdataspaces, IDebugDataSpaces interface [Windows Debugging], IDebugDataSpaces interface [Windows Debugging], described, IDebugDataSpaces, dbgeng/IDebugDataSpaces, IDebugDataSpaces_83f3a88c-f7e6-4b5c-a2b2-4e8bccef4281.xml
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
-	IDebugDataSpaces
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugDataSpaces interface



## Methods

<p>The <b>IDebugDataSpaces</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugDataSpaces.CheckLowMemory](nf-dbgeng-idebugdataspaces-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [dbgeng.IDebugDataSpaces.ReadBusData](nf-dbgeng-idebugdataspaces-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [dbgeng.IDebugDataSpaces.ReadControl](nf-dbgeng-idebugdataspaces-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [dbgeng.IDebugDataSpaces.ReadDebuggerData](nf-dbgeng-idebugdataspaces-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [dbgeng.IDebugDataSpaces.ReadIo](nf-dbgeng-idebugdataspaces-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [dbgeng.IDebugDataSpaces.ReadMsr](nf-dbgeng-idebugdataspaces-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [dbgeng.IDebugDataSpaces.ReadPhysical](nf-dbgeng-idebugdataspaces-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [dbgeng.IDebugDataSpaces.ReadPointersVirtual](nf-dbgeng-idebugdataspaces-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces.ReadProcessorSystemData](nf-dbgeng-idebugdataspaces-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [dbgeng.IDebugDataSpaces.ReadVirtual](nf-dbgeng-idebugdataspaces-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces.ReadVirtualUncached](nf-dbgeng-idebugdataspaces-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [dbgeng.IDebugDataSpaces.SearchVirtual](nf-dbgeng-idebugdataspaces-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [dbgeng.IDebugDataSpaces.WriteBusData](nf-dbgeng-idebugdataspaces-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [dbgeng.IDebugDataSpaces.WriteControl](nf-dbgeng-idebugdataspaces-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [dbgeng.IDebugDataSpaces.WriteIo](nf-dbgeng-idebugdataspaces-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [dbgeng.IDebugDataSpaces.WriteMsr](nf-dbgeng-idebugdataspaces-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [dbgeng.IDebugDataSpaces.WritePhysical](nf-dbgeng-idebugdataspaces-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [dbgeng.IDebugDataSpaces.WritePointersVirtual](nf-dbgeng-idebugdataspaces-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [dbgeng.IDebugDataSpaces.WriteVirtual](nf-dbgeng-idebugdataspaces-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [dbgeng.IDebugDataSpaces.WriteVirtualUncached](nf-dbgeng-idebugdataspaces-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugdataspaces3.md">IDebugDataSpaces3</a>



<a href="..\dbgeng\nn-dbgeng-idebugdataspaces2.md">IDebugDataSpaces2</a>



<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
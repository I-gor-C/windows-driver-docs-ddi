---
UID: NF.wdm.MmFreeContiguousMemory
title: MmFreeContiguousMemory function
author: windows-driver-content
description: The MmFreeContiguousMemory routine releases a range of physically contiguous memory that was allocated by an MmAllocateContiguousMemoryXxx routine.
old-location: kernel\mmfreecontiguousmemory.htm
old-project: kernel
ms.assetid: 485c9b03-eb45-4c86-9292-ccd51ba7b080
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: MmFreeContiguousMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmFreeContiguousMemory
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlMmDispatch, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# MmFreeContiguousMemory function



## -description
The <b>MmFreeContiguousMemory</b> routine releases a range of physically contiguous memory that was allocated by an <b>MmAllocateContiguousMemory<i>Xxx</i></b> routine.



## -syntax

````
VOID MmFreeContiguousMemory(
  _In_ PVOID BaseAddress
);
````


## -parameters

### -param BaseAddress [in]

Pointer to the virtual address of the memory to be freed.


## -returns
None


## -remarks
The <b>MmFreeContiguousMemory</b> routine frees a block of physically contiguous memory that was allocated by a previous call to the <a href="kernel.mmallocatecontiguousmemory">MmAllocateContiguousMemory</a>, <a href="kernel.mmallocatecontiguousmemoryspecifycache">MmAllocateContiguousMemorySpecifyCache</a>, or <a href="kernel.mmallocatecontiguousmemoryspecifycachenode">MmAllocateContiguousMemorySpecifyCacheNode</a> routine. The <i>BaseAddress</i> parameter must be the base address that was obtained from the previous call to the <b>MmAllocateContiguousMemory<i>Xxx</i></b> routine.

A device driver that must use contiguous memory should allocate only what it needs during driver initialization because physical memory is likely to become fragmented as the system runs. Such a driver must deallocate the memory when the driver is done using the memory.

Callers of <b>MmFreeContiguousMemory</b> must be running at IRQL = APC_LEVEL. For Windows Server 2008 and later versions of the Windows operating system, you can also call <b>MmFreeContiguousMemory</b> with IRQL &lt;= DISPATCH_LEVEL. However, you can improve driver performance by calling at APC_LEVEL or below.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
See Remarks section.

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlmmdispatch">IrqlMmDispatch</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.mmallocatecontiguousmemory">MmAllocateContiguousMemory</a>
</dt>
<dt>
<a href="kernel.mmallocatecontiguousmemoryspecifycache">MmAllocateContiguousMemorySpecifyCache</a>
</dt>
<dt>
<a href="kernel.mmallocatecontiguousmemoryspecifycachenode">MmAllocateContiguousMemorySpecifyCacheNode</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmFreeContiguousMemory routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


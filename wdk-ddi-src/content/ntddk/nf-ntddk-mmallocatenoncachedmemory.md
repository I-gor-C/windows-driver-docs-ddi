---
UID: NF:ntddk.MmAllocateNonCachedMemory
title: MmAllocateNonCachedMemory function
author: windows-driver-content
description: The MmAllocateNonCachedMemory routine allocates a virtual address range of noncached and cache-aligned memory.
old-location: kernel\mmallocatenoncachedmemory.htm
old-project: kernel
ms.assetid: aabad72e-2636-47cd-9986-f50ab5101e68
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: MmAllocateNonCachedMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmAllocateNonCachedMemory
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlMmApcLte, HwStorPortProhibitedDDIs, SpNoWait, StorPortStartIo
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=APC_LEVEL
req.typenames: *PWHEA_RAW_DATA_FORMAT, WHEA_RAW_DATA_FORMAT
---

# MmAllocateNonCachedMemory function



## -description
The <b>MmAllocateNonCachedMemory</b> routine allocates a virtual address range of noncached and cache-aligned memory.



## -syntax

````
PVOID MmAllocateNonCachedMemory(
  _In_ SIZE_T NumberOfBytes
);
````


## -parameters

### -param NumberOfBytes [in]

Specifies the size in bytes of the range to be allocated. 


## -returns
If the requested memory cannot be allocated, the return value is <b>NULL</b>. Otherwise, it is the base virtual address of the allocated range. 


## -remarks
<b>MmAllocateNonCachedMemory</b> can be called from a <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine to allocate a noncached block of virtual memory for various device-specific buffers. The function always returns a full multiple of the virtual memory page size, of nonpaged system-address-space memory, regardless of the requested allocation size.

Noncached allocations are aligned on an integral multiple of the processor's data-cache-line size to prevent cache and coherency problems.

The physical memory pages that <b>MmAllocateNonCachedMemory</b> returns are typically not contiguous pages.


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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
&lt;=APC_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/075f5710-b2bf-4546-9648-661a3c8521f8">IrqlMmApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454255">SpNoWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454274">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nc-wdm-pallocate_common_buffer.md">AllocateCommonBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552087">KeGetDcacheFillSize</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmallocatecontiguousmemory.md">MmAllocateContiguousMemory</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmallocatecontiguousmemoryspecifycache.md">MmAllocateContiguousMemorySpecifyCache</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-mmfreenoncachedmemory.md">MmFreeNonCachedMemory</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocateNonCachedMemory routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


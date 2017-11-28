---
UID: NF.ntddk.MmAllocateNonCachedMemory
title: MmAllocateNonCachedMemory
author: windows-driver-content
description: The MmAllocateNonCachedMemory routine allocates a virtual address range of noncached and cache-aligned memory.
old-location: kernel\mmallocatenoncachedmemory.htm
old-project: kernel
ms.assetid: aabad72e-2636-47cd-9986-f50ab5101e68
ms.author: windowsdriverdev
ms.date: 11/20/2017
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
req.iface: 
---

# MmAllocateNonCachedMemory function



## -description
<p>The <b>MmAllocateNonCachedMemory</b> routine allocates a virtual address range of noncached and cache-aligned memory.</p>


## -syntax

````
PVOID MmAllocateNonCachedMemory(
  _In_ SIZE_T NumberOfBytes
);
````


## -parameters
<dl>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>Specifies the size in bytes of the range to be allocated. </p>
</dd>
</dl>

## -returns
<p>If the requested memory cannot be allocated, the return value is <b>NULL</b>. Otherwise, it is the base virtual address of the allocated range. </p>

## -remarks
<p><b>MmAllocateNonCachedMemory</b> can be called from a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine to allocate a noncached block of virtual memory for various device-specific buffers. The function always returns a full multiple of the virtual memory page size, of nonpaged system-address-space memory, regardless of the requested allocation size.</p>

<p>Noncached allocations are aligned on an integral multiple of the processor's data-cache-line size to prevent cache and coherency problems.</p>

<p>The physical memory pages that <b>MmAllocateNonCachedMemory</b> returns are typically not contiguous pages.</p>

<p><b>MmAllocateNonCachedMemory</b> can be called from a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine to allocate a noncached block of virtual memory for various device-specific buffers. The function always returns a full multiple of the virtual memory page size, of nonpaged system-address-space memory, regardless of the requested allocation size.</p>

<p>Noncached allocations are aligned on an integral multiple of the processor's data-cache-line size to prevent cache and coherency problems.</p>

<p>The physical memory pages that <b>MmAllocateNonCachedMemory</b> returns are typically not contiguous pages.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlmmapclte">IrqlMmApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454255">SpNoWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454274">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540575">AllocateCommonBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552087">KeGetDcacheFillSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554460">MmAllocateContiguousMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554464">MmAllocateContiguousMemorySpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554516">MmFreeNonCachedMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocateNonCachedMemory routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

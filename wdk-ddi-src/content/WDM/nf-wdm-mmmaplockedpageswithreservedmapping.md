---
UID: NF.wdm.MmMapLockedPagesWithReservedMapping
title: MmMapLockedPagesWithReservedMapping
author: windows-driver-content
description: The MmMapLockedPagesWithReservedMapping routine maps all or part of an address range that was previously reserved by the MmAllocateMappingAddress routine.
old-location: kernel\mmmaplockedpageswithreservedmapping.htm
ms.assetid: 3fc01bc5-05eb-482f-b625-67061d26915a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmMapLockedPagesWithReservedMapping
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
ms.keywords: MmMapLockedPagesWithReservedMapping
req.iface: 
req.product: Windows 10 or later.
---

# MmMapLockedPagesWithReservedMapping function



## -description
<p>The <b>MmMapLockedPagesWithReservedMapping</b> routine maps all or part of an address range that was previously reserved by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a> routine. </p>


## -syntax

````
PVOID MmMapLockedPagesWithReservedMapping(
  _In_ PVOID               MappingAddress,
  _In_ ULONG               PoolTag,
  _In_ PMDLX               MemoryDescriptorList,
  _In_ MEMORY_CACHING_TYPE CacheType
);
````


## -parameters
<dl>

### -param <i>MappingAddress</i> [in]

<dd>
<p>Pointer to the beginning of the reserved virtual memory range. This must be an address previously returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a>.</p>
</dd>

### -param <i>PoolTag</i> [in]

<dd>
<p>Specifies the pool tag for the reserved memory buffer. This must be identical to the value specified in the <i>PoolTag</i> parameter of the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a> that reserved the buffer. </p>
</dd>

### -param <i>MemoryDescriptorList</i> [in]

<dd>
<p>A pointer to the MDL that is to be mapped. This MDL must describe physical pages that are locked down. A locked-down MDL can be built by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554489">MmAllocatePagesForMdlEx</a> routine. </p>
</dd>

### -param <i>CacheType</i> [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a> value to use to create the mapping.</p>
</dd>
</dl>

## -returns
<p><b>MmMapLockedPagesWithReservedMapping</b> returns a pointer to the beginning of the mapped memory, or <b>NULL</b> if the system could not map the memory. This routine returns <b>NULL</b> only if there is an error in the function parameters (for example, the driver's mapping address is not large enough to span the supplied MDL). This function is intended to enable drivers to make forward progress even in low-resource scenarios.</p>

## -remarks
<p>The caller can use <b>MmMapLockedPagesWithReservedMapping</b> to map a subrange of the virtual memory range reserved by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a> as follows: </p>

<p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a> to allocate an MDL. The returned MDL is built using the specified starting address and size of the subrange of the virtual memory range to map. </p>

<p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a> to lock down the physical pages described by the MDL obtained in step 1.</p>

<p>Use <b>MmMapLockedPagesWithReservedMapping</b> to actually map the virtual memory to the physical memory that was locked down in step 2. Note that the virtual address returned by this function does include the byte offset that the MDL specifies. However, the <b>MappedSystemVa</b> field of the MDL that is set by this function does <u>not</u> include the byte offset. </p>

<p>Once the caller does not need to access the memory, it unmaps the memory with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556392">MmUnmapReservedMapping</a>. The caller can map and unmap the memory buffer as needed, and must unmap it prior to freeing the mapping range with <a href="https://msdn.microsoft.com/library/windows/hardware/ff554512">MmFreeMappingAddress</a>. </p>

<p>Note that the <i>MappingAddress</i> parameter specifies the beginning of the range of memory previously reserved by the caller, <u>not</u> the beginning of the memory subrange to be mapped. The caller specifies the starting address and length of the buffer when it allocates the MDL with <a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a>. The buffer must fit inside the reserved memory range, but it can be a strict subset.</p>

<p>The routine uses the <i>CacheType</i> parameter only if the pages that are described by the MDL do not already have a cache type associated with them. However, in nearly all cases, the pages already have an associated cache type, and this cache type is used by the new mapping. An exception to this rule is for pages that are allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554482">MmAllocatePagesForMdl</a>, which do not have a specific cache type associated with them. For such pages, the <i>CacheType</i> parameter determines the cache type of the mapping. </p>

<p>The caller can use <b>MmMapLockedPagesWithReservedMapping</b> to map a subrange of the virtual memory range reserved by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a> as follows: </p>

<p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a> to allocate an MDL. The returned MDL is built using the specified starting address and size of the subrange of the virtual memory range to map. </p>

<p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a> to lock down the physical pages described by the MDL obtained in step 1.</p>

<p>Use <b>MmMapLockedPagesWithReservedMapping</b> to actually map the virtual memory to the physical memory that was locked down in step 2. Note that the virtual address returned by this function does include the byte offset that the MDL specifies. However, the <b>MappedSystemVa</b> field of the MDL that is set by this function does <u>not</u> include the byte offset. </p>

<p>Once the caller does not need to access the memory, it unmaps the memory with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556392">MmUnmapReservedMapping</a>. The caller can map and unmap the memory buffer as needed, and must unmap it prior to freeing the mapping range with <a href="https://msdn.microsoft.com/library/windows/hardware/ff554512">MmFreeMappingAddress</a>. </p>

<p>Note that the <i>MappingAddress</i> parameter specifies the beginning of the range of memory previously reserved by the caller, <u>not</u> the beginning of the memory subrange to be mapped. The caller specifies the starting address and length of the buffer when it allocates the MDL with <a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a>. The buffer must fit inside the reserved memory range, but it can be a strict subset.</p>

<p>The routine uses the <i>CacheType</i> parameter only if the pages that are described by the MDL do not already have a cache type associated with them. However, in nearly all cases, the pages already have an associated cache type, and this cache type is used by the new mapping. An exception to this rule is for pages that are allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554482">MmAllocatePagesForMdl</a>, which do not have a specific cache type associated with them. For such pages, the <i>CacheType</i> parameter determines the cache type of the mapping. </p>

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
<p>Available in Windows XP and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554482">MmAllocatePagesForMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554489">MmAllocatePagesForMdlEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554512">MmFreeMappingAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556392">MmUnmapReservedMapping</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmMapLockedPagesWithReservedMapping routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

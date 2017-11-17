---
UID: NF.wdm.MmAllocateNodePagesForMdlEx
title: MmAllocateNodePagesForMdlEx
author: windows-driver-content
description: The MmAllocateNodePagesForMdlEx routine allocates nonpaged physical memory from an ideal node, and allocates an MDL structure to describe this memory.
old-location: kernel\mmallocatenodepagesformdlex.htm
ms.assetid: 491327A4-87B5-4206-9D47-007CE14E1327
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmAllocateNodePagesForMdlEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (See Remarks section.)
ms.keywords: MmAllocateNodePagesForMdlEx
req.iface: 
req.product: Windows 10 or later.
---

# MmAllocateNodePagesForMdlEx function



## -description
<p>The <b>MmAllocateNodePagesForMdlEx</b> routine allocates nonpaged physical memory from an ideal node, and allocates an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure to describe this memory.</p>


## -syntax

````
PMDL MmAllocateNodePagesForMdlEx(
  _In_ PHYSICAL_ADDRESS    LowAddress,
  _In_ PHYSICAL_ADDRESS    HighAddress,
  _In_ PHYSICAL_ADDRESS    SkipBytes,
  _In_ SIZE_T              TotalBytes,
  _In_ MEMORY_CACHING_TYPE CacheType,
  _In_ ULONG               IdealNode,
  _In_ ULONG               Flags
);
````


## -parameters
<dl>

### -param <i>LowAddress</i> [in]

<dd>
<p>The physical address of the start of the first address range from which the allocated pages can come. If <b>MmAllocateNodePagesForMdlEx</b> cannot allocate the requested number of bytes in the first address range, the routine iterates through additional address ranges to get more pages. At each iteration, <b>MmAllocateNodePagesForMdlEx</b> adds the value of <i>SkipBytes</i> to the previous start address to calculate the start of the next address range.</p>
</dd>

### -param <i>HighAddress</i> [in]

<dd>
<p>The physical address of the end of the first address range that the allocated pages can come from.</p>
</dd>

### -param <i>SkipBytes</i> [in]

<dd>
<p>The number of bytes to skip from the start of the previous address range that the allocated pages can come from. <i>SkipBytes</i> must be an integer multiple of the virtual memory page size, in bytes.</p>
</dd>

### -param <i>TotalBytes</i> [in]

<dd>
<p>The total number of bytes to allocate for the MDL.</p>
</dd>

### -param <i>CacheType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a> value, which indicates the type of caching that is allowed for the requested memory.</p>
</dd>

### -param <i>IdealNode</i> [in]

<dd>
<p>The ideal node number. If a multiprocessor system contains N nodes, valid node numbers are in the range 0 to N-1. Your driver can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553020">KeQueryHighestNodeNumber</a> routine to get the highest node number. A single-processor or non-NUMA multiprocessor system has only one node, node 0, from which to allocate memory. For a NUMA multiprocessor system, the allocation is made from the ideal node, if possible. If insufficient memory is available in the ideal node to satisfy the allocation request, and the caller does not set the MM_ALLOCATE_FROM_LOCAL_NODE_ONLY flag, <b>MmAllocateNodePagesForMdlEx</b> will try to allocate memory from other nodes.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Flags for this operation. Set this parameter to zero or to the bitwise-OR of one or more of the following flag bits:</p>
<ul>
<li>
<p>MM_DONT_ZERO_ALLOCATION</p>
</li>
<li>
<p>MM_ALLOCATE_FROM_LOCAL_NODE_ONLY</p>
</li>
<li>
<p>MM_ALLOCATE_FULLY_REQUIRED</p>
</li>
<li>
<p>MM_ALLOCATE_NO_WAIT</p>
</li>
<li>
<p>MM_ALLOCATE_PREFER_CONTIGUOUS</p>
</li>
<li>
<p>MM_ALLOCATE_REQUIRE_CONTIGUOUS_CHUNKS</p>
</li>
</ul>
<p>The MM_ALLOCATE_PREFER_CONTIGUOUS and MM_ALLOCATE_REQUIRE_CONTIGUOUS_CHUNKS flag bits are mutually exclusive. For more information about these flags, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556396">MM_ALLOCATE_XXX</a>.</p>
</dd>
</dl>

## -returns
<p><b>MmAllocateNodePagesForMdlEx</b> returns a pointer to an MDL structure if it is successful. Otherwise, if the routine fails to allocate any memory, the routine returns <b>NULL</b>.</p>

<p>A return value of <b>NULL</b> indicates that no physical memory pages are available in the specified address ranges, or that there is not enough memory pool available to allocate the MDL structure.</p>

<p>If the routine successfully allocates some, but not all, of the requested memory, the MDL describes as much physical memory as the routine was able to allocate.</p>

## -remarks
<p>In a non-uniform memory access (NUMA) multiprocessor system, the caller can specify an ideal node from which to allocate the memory. A node is a collection of processors that share fast access to a region of memory. In a non-NUMA multiprocessor or a single-processor system, <b>MmAllocateNodePagesForMdlEx</b> treats all memory as belonging to a single node and allocates memory from this node.</p>

<p>By default, the physical memory pages that <b>MmAllocateNodePagesForMdlEx</b> returns are not contiguous pages. Callers can override the default behavior of this routine by setting the MM_ALLOCATE_PREFER_CONTIGUOUS or MM_ALLOCATE_REQUIRE_CONTIGUOUS_CHUNKS flag bit in the <i>Flags</i> parameter.</p>

<p><b>MmAllocateNodePagesForMdlEx</b> does not map the allocated physical memory into virtual memory. If necessary, the caller can call a routine such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a> to map the physical memory pages described by the MDL.</p>

<p><b>MmAllocateNodePagesForMdlEx</b> is designed for kernel-mode drivers that do not need corresponding virtual addresses (that is, they need physical pages and do not need them to be physically contiguous), and for kernel-mode drivers that can achieve substantial performance gains if physical memory for a device is allocated in a specific physical address range (for example, an AGP graphics card).</p>

<p>Depending on how much physical memory is currently available in the requested ranges, <b>MmAllocateNodePagesForMdlEx</b> might return an MDL that describes less memory than was requested. The routine also might return <b>NULL</b> if no memory was allocated. The caller should check the amount of memory that is actually allocated, as described by the MDL.</p>

<p>The caller must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554521">MmFreePagesFromMdl</a> to release the memory pages that are described by an MDL that was created by <b>MmAllocateNodePagesForMdlEx</b>. After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> to release the memory allocated for the MDL structure.</p>

<p>By default, <b>MmAllocateNodePagesForMdlEx</b> fills the pages that it allocates with zeros. The caller can specify the MM_DONT_ZERO_ALLOCATION flag to override this default and to possibly improve performance.</p>

<p>The maximum amount of memory that <b>MmAllocateNodePagesForMdlEx</b> can allocate in a single call is (4 gigabytes - PAGE_SIZE). The routine can satisfy an allocation request for this amount only if enough pages are available.</p>

<p><b>MmAllocateNodePagesForMdlEx</b> runs at IRQL &lt;= APC_LEVEL. If necessary, your driver can call <b>MmAllocateNodePagesForMdlEx</b> at DISPATCH_LEVEL. However, you can improve driver performance by calling at APC_LEVEL or below.</p>

<p>In a non-uniform memory access (NUMA) multiprocessor system, the caller can specify an ideal node from which to allocate the memory. A node is a collection of processors that share fast access to a region of memory. In a non-NUMA multiprocessor or a single-processor system, <b>MmAllocateNodePagesForMdlEx</b> treats all memory as belonging to a single node and allocates memory from this node.</p>

<p>By default, the physical memory pages that <b>MmAllocateNodePagesForMdlEx</b> returns are not contiguous pages. Callers can override the default behavior of this routine by setting the MM_ALLOCATE_PREFER_CONTIGUOUS or MM_ALLOCATE_REQUIRE_CONTIGUOUS_CHUNKS flag bit in the <i>Flags</i> parameter.</p>

<p><b>MmAllocateNodePagesForMdlEx</b> does not map the allocated physical memory into virtual memory. If necessary, the caller can call a routine such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a> to map the physical memory pages described by the MDL.</p>

<p><b>MmAllocateNodePagesForMdlEx</b> is designed for kernel-mode drivers that do not need corresponding virtual addresses (that is, they need physical pages and do not need them to be physically contiguous), and for kernel-mode drivers that can achieve substantial performance gains if physical memory for a device is allocated in a specific physical address range (for example, an AGP graphics card).</p>

<p>Depending on how much physical memory is currently available in the requested ranges, <b>MmAllocateNodePagesForMdlEx</b> might return an MDL that describes less memory than was requested. The routine also might return <b>NULL</b> if no memory was allocated. The caller should check the amount of memory that is actually allocated, as described by the MDL.</p>

<p>The caller must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554521">MmFreePagesFromMdl</a> to release the memory pages that are described by an MDL that was created by <b>MmAllocateNodePagesForMdlEx</b>. After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> to release the memory allocated for the MDL structure.</p>

<p>By default, <b>MmAllocateNodePagesForMdlEx</b> fills the pages that it allocates with zeros. The caller can specify the MM_DONT_ZERO_ALLOCATION flag to override this default and to possibly improve performance.</p>

<p>The maximum amount of memory that <b>MmAllocateNodePagesForMdlEx</b> can allocate in a single call is (4 gigabytes - PAGE_SIZE). The routine can satisfy an allocation request for this amount only if enough pages are available.</p>

<p><b>MmAllocateNodePagesForMdlEx</b> runs at IRQL &lt;= APC_LEVEL. If necessary, your driver can call <b>MmAllocateNodePagesForMdlEx</b> at DISPATCH_LEVEL. However, you can improve driver performance by calling at APC_LEVEL or below.</p>

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
<p>Available starting with Windows 8.</p>
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
<p>&lt;= DISPATCH_LEVEL (See Remarks section.)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553020">KeQueryHighestNodeNumber</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556396">MM_ALLOCATE_XXX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554521">MmFreePagesFromMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocateNodePagesForMdlEx routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

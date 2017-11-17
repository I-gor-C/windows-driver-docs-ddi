---
UID: NF.ntddk.MmAllocateContiguousMemorySpecifyCacheNode
title: MmAllocateContiguousMemorySpecifyCacheNode
author: windows-driver-content
description: The MmAllocateContiguousMemorySpecifyCacheNode routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space.
old-location: kernel\mmallocatecontiguousmemoryspecifycachenode.htm
ms.assetid: ce54870e-80af-4588-a0ca-1ad115739256
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmAllocateContiguousMemorySpecifyCacheNode
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: MmAllocateContiguousMemorySpecifyCacheNode
req.iface: 
---

# MmAllocateContiguousMemorySpecifyCacheNode function



## -description
<p>The <b>MmAllocateContiguousMemorySpecifyCacheNode</b> routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space.</p>


## -syntax

````
PVOID MmAllocateContiguousMemorySpecifyCacheNode(
  _In_     SIZE_T              NumberOfBytes,
  _In_     PHYSICAL_ADDRESS    LowestAcceptableAddress,
  _In_     PHYSICAL_ADDRESS    HighestAcceptableAddress,
  _In_opt_ PHYSICAL_ADDRESS    BoundaryAddressMultiple,
  _In_     MEMORY_CACHING_TYPE CacheType,
  _In_     NODE_REQUIREMENT    PreferredNode
);
````


## -parameters
<dl>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>The size, in bytes, of the block of contiguous memory to allocate. For more information, see Remarks.</p>
</dd>

### -param <i>LowestAcceptableAddress</i> [in]

<dd>
<p>The lowest valid physical address the caller can use. For example, if a device can address only locations above the first 8 megabytes of the processor's physical memory address range, the driver for this device  should set <i>LowestAcceptableAddress</i> to 0x0000000000800000.</p>
</dd>

### -param <i>HighestAcceptableAddress</i> [in]

<dd>
<p>The highest valid physical address the caller can use. For example, if a device can address only locations in the first 16 megabytes of the processor's physical memory address range, the driver for this device should set <i>HighestAcceptableAddress</i> to 0x0000000000FFFFFF.</p>
</dd>

### -param <i>BoundaryAddressMultiple</i> [in, optional]

<dd>
<p>The physical address multiple that the allocated buffer must not cross. A physical address multiple must always be a power of two. This parameter is optional and can be specified as zero to indicate that the device has no special memory boundary restrictions. For more information, see Remarks.</p>
</dd>

### -param <i>CacheType</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a> value, which indicates the type of caching requested for the contiguous physical memory.</p>
</dd>

### -param <i>PreferredNode</i> [in]

<dd>
<p>The preferred node number. If a multiprocessor system contains N nodes, the nodes are numbered 0 to N-1. If MM_ANY_NODE_OK is specified or the machine only has one node, then the allocation is satisfied from any node. Otherwise, the allocation is made from the preferred node or if a satisfactory range cannot be found from the preferred node, then <b>NULL</b> is returned.</p>
</dd>
</dl>

## -returns
<p><b>MmAllocateContiguousMemorySpecifyCacheNode</b> returns the base virtual address for the allocated memory. If the request cannot be satisfied, the routine returns <b>NULL</b>.</p>

## -remarks
<p>A kernel-mode device driver calls this routine  to allocate a contiguous block of physical memory. In a non-uniform memory access (NUMA) multiprocessor system, the caller can specify a preferred node from which to allocate the memory. A node is a collection of processors that share fast access to a region of memory. In a non-NUMA multiprocessor or a single-processor system, <b>MmAllocateContiguousMemorySpecifyCacheNode</b> treats all memory as belonging to a single node and allocates memory from this node.</p>

<p><b>MmAllocateContiguousMemorySpecifyCacheNode</b> allocates a block of nonpaged memory that is contiguous in physical address space. The routine maps this block to a contiguous block of virtual memory in the system address space and returns the virtual address of the base of this block. The routine aligns the starting address of a contiguous memory allocation to a memory page boundary.</p>

<p>Drivers must not access memory beyond the requested allocation size. For example, developers should not assume that their drivers can safely use memory between the end of their requested allocation and the next page boundary.</p>

<p>Because contiguous physical memory is usually in short supply, it should be used sparingly and only when necessary. A driver that must use contiguous memory should allocate this memory during driver initialization because physical memory is likely to become fragmented over time as the operating system allocates and frees memory. Typically, a driver calls <b>MmAllocateContiguousMemorySpecifyCacheNode</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine to allocate an internal buffer for long-term use, and frees the buffer just before the driver is unloaded.</p>

<p>Memory allocated by <b>MmAllocateContiguousMemorySpecifyCacheNode</b> must be freed when the memory is no longer needed. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554503">MmFreeContiguousMemory</a> routine to free memory that is allocated by <b>MmAllocateContiguousMemorySpecifyCacheNode</b>.</p>

<p>If you specify a nonzero value for the <i>BoundaryAddressMultiple</i> parameter, the physical address range of the allocated memory block will not cross an address boundary that is an integer multiple of this value. A driver should set this parameter to zero unless a nonzero value is required to work around a hardware limitation. For example, if a device cannot transfer data across 16-megabyte physical boundaries, the driver should specify a value of 0x1000000 for this parameter to ensure that the addresses that the device sees do not wrap around at a 16-megabyte boundary.</p>

<p>A kernel-mode device driver calls this routine  to allocate a contiguous block of physical memory. In a non-uniform memory access (NUMA) multiprocessor system, the caller can specify a preferred node from which to allocate the memory. A node is a collection of processors that share fast access to a region of memory. In a non-NUMA multiprocessor or a single-processor system, <b>MmAllocateContiguousMemorySpecifyCacheNode</b> treats all memory as belonging to a single node and allocates memory from this node.</p>

<p><b>MmAllocateContiguousMemorySpecifyCacheNode</b> allocates a block of nonpaged memory that is contiguous in physical address space. The routine maps this block to a contiguous block of virtual memory in the system address space and returns the virtual address of the base of this block. The routine aligns the starting address of a contiguous memory allocation to a memory page boundary.</p>

<p>Drivers must not access memory beyond the requested allocation size. For example, developers should not assume that their drivers can safely use memory between the end of their requested allocation and the next page boundary.</p>

<p>Because contiguous physical memory is usually in short supply, it should be used sparingly and only when necessary. A driver that must use contiguous memory should allocate this memory during driver initialization because physical memory is likely to become fragmented over time as the operating system allocates and frees memory. Typically, a driver calls <b>MmAllocateContiguousMemorySpecifyCacheNode</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine to allocate an internal buffer for long-term use, and frees the buffer just before the driver is unloaded.</p>

<p>Memory allocated by <b>MmAllocateContiguousMemorySpecifyCacheNode</b> must be freed when the memory is no longer needed. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554503">MmFreeContiguousMemory</a> routine to free memory that is allocated by <b>MmAllocateContiguousMemorySpecifyCacheNode</b>.</p>

<p>If you specify a nonzero value for the <i>BoundaryAddressMultiple</i> parameter, the physical address range of the allocated memory block will not cross an address boundary that is an integer multiple of this value. A driver should set this parameter to zero unless a nonzero value is required to work around a hardware limitation. For example, if a device cannot transfer data across 16-megabyte physical boundaries, the driver should specify a value of 0x1000000 for this parameter to ensure that the addresses that the device sees do not wrap around at a 16-megabyte boundary.</p>

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
<p>Available starting with Windows Vista.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554503">MmFreeContiguousMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocateContiguousMemorySpecifyCacheNode routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

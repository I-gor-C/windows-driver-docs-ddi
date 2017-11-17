---
UID: NF.wdm.ExAllocatePoolWithTag~r1
title: ExAllocatePoolWithTag
author: windows-driver-content
description: The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block.
old-location: kernel\exallocatepoolwithtag.htm
ms.assetid: a9951e7b-60a2-4bf2-913c-b7291d7c3173
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExAllocatePoolWithTag
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CheckDeviceObjectFlags, IrqlExAllocatePool, IrqlExFree1, PowerDownAllocate, PowerUpFail, HwStorPortProhibitedDDIs, SpNoWait, StorPortStartIo
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
ms.keywords: ExAllocatePoolWithTag
req.iface: 
req.product: Windows 10 or later.
---

# ExAllocatePoolWithTag function



## -description
<p>The <b>ExAllocatePoolWithTag</b> routine allocates pool memory of the specified type and returns a pointer to the allocated block.</p>


## -syntax

````
PVOID ExAllocatePoolWithTag(
  _In_ POOL_TYPE PoolType,
  _In_ SIZE_T    NumberOfBytes,
  _In_ ULONG     Tag
);
````


## -parameters
<dl>

### -param <i>PoolType</i> [in]

<dd>
<p>The type of pool memory to allocate. For a description of the available pool memory types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>.</p>
<p>You can modify the <i>PoolType</i> value by bitwise-ORing this value with the POOL_RAISE_IF_ALLOCATION_FAILURE flag. This flag causes an exception to be raised if the request cannot be satisfied. Use of the POOL_RAISE_IF_ALLOCATION_FAILURE flag is not recommended because it is costly.</p>
<p>Similarly, you can modify the <i>PoolType</i> value by bitwise-ORing this value with the POOL_COLD_ALLOCATION flag as a hint to the kernel to allocate the memory from pages that are likely to be paged out quickly. To reduce the amount of resident pool memory as much as possible, you should not reference these allocations frequently. The POOL_COLD_ALLOCATION flag is only advisory and is supported starting with Windows XP.</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>The number of bytes to allocate.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>The pool tag to use for the allocated memory. Specify the pool tag as a character literal of up to four characters delimited by single quotation marks (for example, 'Tag1'). The string is usually specified in reverse order (for example, '1gaT'). Each ASCII character in the tag must be a value in the range 0x20 (space) to 0x126 (tilde). Each allocation code path should use a unique pool tag to help debuggers and verifiers identify the code path.</p>
</dd>
</dl>

## -returns
<p><b>ExAllocatePoolWithTag</b> returns <b>NULL</b> if there is insufficient memory in the free pool to satisfy the request. Otherwise, the routine returns a pointer to the allocated memory.</p>

## -remarks
<p>This routine is used for the general pool allocation of memory.</p>

<p>If <i>NumberOfBytes</i> is PAGE_SIZE or greater, a page-aligned buffer is allocated. Memory allocations of PAGE_SIZE or less are allocated within a page and do not cross page boundaries. Memory allocations of less than PAGE_SIZE are not necessarily page-aligned but are aligned to 8-byte boundaries in 32-bit systems and to 16-byte boundaries in 64-bit systems.</p>

<p>A successful allocation requesting <i>NumberOfBytes</i> &lt; PAGE_SIZE of nonpaged pool gives the caller exactly the number of requested bytes of memory. If an allocation request for <i>NumberOfBytes</i> &gt; PAGE_SIZE succeeds and <i>NumberOfBytes</i> is not an exact multiple of PAGE_SIZE, the last page in the allocation contains bytes that are not part of the caller's allocation. If possible, the pool allocator uses these bytes. To avoid corrupting data that belongs to other kernel-mode components, drivers must access only storage addresses that they have explicitly allocated.</p>

<p>The system associates the pool tag with the allocated memory. Programming tools, such as WinDbg, can display the pool tag associated with each allocated buffer. Gflags, a tool included in <a href="https://msdn.microsoft.com/938ef180-84de-442f-9b6c-1138c2fc8d5a">Debugging Tools for Windows</a>, turns on a system feature that requests allocation from <a href="NULL">special pool</a> for a particular pool tag. <a href="NULL">Poolmon</a>, which is included in the WDK, tracks memory by pool tag.</p>

<p>The value of <i>Tag</i> is stored, and sometimes displayed, in reverse (little-endian) order. For example, if a caller passes 'Fred' as a <i>Tag</i>, it appears as "derF" in a pool dump and in pool usage tracking in the debugger, and as 0x64657246 in the registry and in tool displays.</p>

<p>The allocated buffer can be freed with either <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544593">ExFreePoolWithTag</a>.</p>

<p>The system automatically sets certain standard event objects when the amount of pool (paged or nonpaged) is high or low. Drivers can wait for these events to tune their pool usage. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563847">Standard Event Objects</a>.</p>

<p>Callers of <b>ExAllocatePoolWithTag</b> must be executing at IRQL &lt;= DISPATCH_LEVEL. A caller executing at DISPATCH_LEVEL must specify a <b>NonPaged</b><i>Xxx</i> value for <i>PoolType</i>. A caller executing at IRQL &lt;= APC_LEVEL can specify any <b>POOL_TYPE</b> value, but the IRQL and environment must also be considered for determining the page type.</p>

<p>In a non-uniform memory access (NUMA) multiprocessor architecture, <b>ExAllocatePoolWithTag</b> tries to allocate memory that is local to the processor that is calling <b>ExAllocatePoolWithTag</b>. If no local memory is available, <b>ExAllocatePoolWithTag</b> allocates the closest available memory.</p>

<p>This routine is used for the general pool allocation of memory.</p>

<p>If <i>NumberOfBytes</i> is PAGE_SIZE or greater, a page-aligned buffer is allocated. Memory allocations of PAGE_SIZE or less are allocated within a page and do not cross page boundaries. Memory allocations of less than PAGE_SIZE are not necessarily page-aligned but are aligned to 8-byte boundaries in 32-bit systems and to 16-byte boundaries in 64-bit systems.</p>

<p>A successful allocation requesting <i>NumberOfBytes</i> &lt; PAGE_SIZE of nonpaged pool gives the caller exactly the number of requested bytes of memory. If an allocation request for <i>NumberOfBytes</i> &gt; PAGE_SIZE succeeds and <i>NumberOfBytes</i> is not an exact multiple of PAGE_SIZE, the last page in the allocation contains bytes that are not part of the caller's allocation. If possible, the pool allocator uses these bytes. To avoid corrupting data that belongs to other kernel-mode components, drivers must access only storage addresses that they have explicitly allocated.</p>

<p>The system associates the pool tag with the allocated memory. Programming tools, such as WinDbg, can display the pool tag associated with each allocated buffer. Gflags, a tool included in <a href="https://msdn.microsoft.com/938ef180-84de-442f-9b6c-1138c2fc8d5a">Debugging Tools for Windows</a>, turns on a system feature that requests allocation from <a href="NULL">special pool</a> for a particular pool tag. <a href="NULL">Poolmon</a>, which is included in the WDK, tracks memory by pool tag.</p>

<p>The value of <i>Tag</i> is stored, and sometimes displayed, in reverse (little-endian) order. For example, if a caller passes 'Fred' as a <i>Tag</i>, it appears as "derF" in a pool dump and in pool usage tracking in the debugger, and as 0x64657246 in the registry and in tool displays.</p>

<p>The allocated buffer can be freed with either <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544593">ExFreePoolWithTag</a>.</p>

<p>The system automatically sets certain standard event objects when the amount of pool (paged or nonpaged) is high or low. Drivers can wait for these events to tune their pool usage. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563847">Standard Event Objects</a>.</p>

<p>Callers of <b>ExAllocatePoolWithTag</b> must be executing at IRQL &lt;= DISPATCH_LEVEL. A caller executing at DISPATCH_LEVEL must specify a <b>NonPaged</b><i>Xxx</i> value for <i>PoolType</i>. A caller executing at IRQL &lt;= APC_LEVEL can specify any <b>POOL_TYPE</b> value, but the IRQL and environment must also be considered for determining the page type.</p>

<p>In a non-uniform memory access (NUMA) multiprocessor architecture, <b>ExAllocatePoolWithTag</b> tries to allocate memory that is local to the processor that is calling <b>ExAllocatePoolWithTag</b>. If no local memory is available, <b>ExAllocatePoolWithTag</b> allocates the closest available memory.</p>

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
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975142">CheckDeviceObjectFlags</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547747">IrqlExAllocatePool</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975183">IrqlExFree1</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975201">PowerDownAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975205">PowerUpFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454255">SpNoWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454274">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544513">ExAllocatePoolWithQuotaTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544523">ExAllocatePoolWithTagPriority</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544593">ExFreePoolWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExAllocatePoolWithTag routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

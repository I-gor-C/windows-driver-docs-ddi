---
UID: NF.wdm.ExAllocatePoolWithTagPriority
title: ExAllocatePoolWithTagPriority
author: windows-driver-content
description: The ExAllocatePoolWithTagPriority routine allocates pool memory of the specified type.
old-location: kernel\exallocatepoolwithtagpriority.htm
ms.assetid: 33087a37-e6fc-4b21-aa9e-e4617eeccd29
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
req.alt-api: ExAllocatePoolWithTagPriority
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExAllocatePool, IrqlExFree2, HwStorPortProhibitedDDIs, SpNoWait, StorPortStartIo
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
ms.keywords: ExAllocatePoolWithTagPriority
req.iface: 
req.product: Windows 10 or later.
---

# ExAllocatePoolWithTagPriority function



## -description
<p>The <b>ExAllocatePoolWithTagPriority</b> routine allocates pool memory of the specified type.</p>


## -syntax

````
PVOID ExAllocatePoolWithTagPriority(
  _In_ POOL_TYPE        PoolType,
  _In_ SIZE_T           NumberOfBytes,
  _In_ ULONG            Tag,
  _In_ EX_POOL_PRIORITY Priority
);
````


## -parameters
<dl>

### -param <i>PoolType</i> [in]

<dd>
<p>The type of pool memory to allocate. For a description of the available pool memory types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>.</p>
<p>You can modify the <i>PoolType</i> value by bitwise-ORing this value with the POOL_RAISE_IF_ALLOCATION_FAILURE flag. This flag causes an exception to be raised if the request cannot be satisfied.</p>
<p>Similarly, you can modify the <i>PoolType</i> value by bitwise-ORing this value with the POOL_COLD_ALLOCATION flag as a hint to the kernel to allocate the memory from pages that are likely to be paged out  quickly. To reduce the amount of resident pool memory as much as possible, you should not reference these allocations frequently. The POOL_COLD_ALLOCATION flag is only advisory and is available starting with Windows XP.</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>The number of bytes to allocate.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>The pool tag to use for the allocated memory. For more information, see the <i>Tag</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>.</p>
</dd>

### -param <i>Priority</i> [in]

<dd>
<p>The priority of this request. Set this parameter to one of the following <b>EX_POOL_PRIORITY</b> enumeration values.</p>
<table>
<tr>
<th>Priority value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p><b>LowPoolPriority</b></p>
</td>
<td>
<p>Specifies that the system may fail the request when it runs low on resources. Driver allocations that can recover from an allocation failure use this priority.</p>
</td>
</tr>
<tr>
<td>
<p><b>NormalPoolPriority</b></p>
</td>
<td>
<p>Specifies that the system may fail the request when it runs very low on resources. Most drivers should use this value.</p>
</td>
</tr>
<tr>
<td>
<p><b>HighPoolPriority</b></p>
</td>
<td>
<p>Specifies that the system must not fail the request, unless it is completely out of resources. Drivers only use this value when it is critically important for the request to succeed.</p>
</td>
</tr>
</table>
<p> </p>
<p>The <b>EX_POOL_PRIORITY</b> enumeration defines <b><i>Xxx</i>SpecialPoolOverrun</b> and <b><i>Xxx</i>SpecialPoolUnderrun</b> variants to specify how memory should be allocated when <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> (or special pool) is enabled. If the driver specifies <b><i>Xxx</i>SpecialPoolUnderrun</b>, when the <a href="https://msdn.microsoft.com/ab464d5b-7bad-494e-80cd-e32ca9e9fa8d">memory manager</a> allocates memory from <a href="NULL">special pool</a>, it allocates it at the start of a physical page. If the driver specifies <b><i>Xxx</i>SpecialPoolOverrun</b>, the memory manager allocates it at the end of a physical page.</p>
</dd>
</dl>

## -returns
<p><b>ExAllocatePoolWithTagPriority</b> returns <b>NULL</b> if there is insufficient memory in the free pool to satisfy the request unless POOL_RAISE_IF_ALLOCATION_FAILURE is specified. Otherwise, the routine returns a pointer to the allocated memory. </p>

## -remarks
<p>Callers of <b>ExAllocatePoolWithTagPriority</b> must be executing at IRQL &lt;= DISPATCH_LEVEL. A caller executing at DISPATCH_LEVEL must specify a <b>NonPaged</b><i>Xxx</i> value for <i>PoolType</i>. A caller executing at IRQL &lt;= APC_LEVEL can specify any <b>POOL_TYPE</b> value, but the IRQL and environment must also be considered for determining the page type.</p>

<p>If <i>NumberOfBytes</i> is PAGE_SIZE or greater, a page-aligned buffer is allocated. Memory allocations of PAGE_SIZE or less are allocated within a page and do not cross page boundaries. Memory allocations of less than PAGE_SIZE are not necessarily page-aligned but are aligned to 8-byte boundaries in 32-bit systems and to 16-byte boundaries in 64-bit systems.</p>

<p>The system automatically sets certain standard event objects when the amount of pool (paged or nonpaged) is high or low. Drivers can wait for these events to tune their pool usage. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563847">Standard Event Objects</a>.</p>

<p>In a non-uniform memory access (NUMA) multiprocessor architecture, <b>ExAllocatePoolWithTagPriority</b> tries to allocate memory that is local to the processor that is calling <b>ExAllocatePoolWithTagPriority</b>. If no local memory is available, <b>ExAllocatePoolWithTagPriority</b> allocates the closest available memory.</p>

<p>Callers of <b>ExAllocatePoolWithTagPriority</b> must be executing at IRQL &lt;= DISPATCH_LEVEL. A caller executing at DISPATCH_LEVEL must specify a <b>NonPaged</b><i>Xxx</i> value for <i>PoolType</i>. A caller executing at IRQL &lt;= APC_LEVEL can specify any <b>POOL_TYPE</b> value, but the IRQL and environment must also be considered for determining the page type.</p>

<p>If <i>NumberOfBytes</i> is PAGE_SIZE or greater, a page-aligned buffer is allocated. Memory allocations of PAGE_SIZE or less are allocated within a page and do not cross page boundaries. Memory allocations of less than PAGE_SIZE are not necessarily page-aligned but are aligned to 8-byte boundaries in 32-bit systems and to 16-byte boundaries in 64-bit systems.</p>

<p>The system automatically sets certain standard event objects when the amount of pool (paged or nonpaged) is high or low. Drivers can wait for these events to tune their pool usage. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563847">Standard Event Objects</a>.</p>

<p>In a non-uniform memory access (NUMA) multiprocessor architecture, <b>ExAllocatePoolWithTagPriority</b> tries to allocate memory that is local to the processor that is calling <b>ExAllocatePoolWithTagPriority</b>. If no local memory is available, <b>ExAllocatePoolWithTagPriority</b> allocates the closest available memory.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547747">IrqlExAllocatePool</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975184">IrqlExFree2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454255">SpNoWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454274">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExAllocatePoolWithTagPriority routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

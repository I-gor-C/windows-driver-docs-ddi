---
UID: NF.wdm.ExAllocatePoolWithQuotaTag~r1
title: ExAllocatePoolWithQuotaTag
author: windows-driver-content
description: The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process.
old-location: kernel\exallocatepoolwithquotatag.htm
old-project: kernel
ms.assetid: 1d2e4c8c-c76c-4936-80bf-005d8a393aa9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExAllocatePoolWithQuotaTag
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExAllocatePoolWithQuotaTag
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs, SpNoWait, StorPortStartIo
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# ExAllocatePoolWithQuotaTag function



## -description
<p>The <b>ExAllocatePoolWithQuotaTag</b> routine allocates pool memory, charging the quota against the current process.</p>


## -syntax

````
PVOID ExAllocatePoolWithQuotaTag(
  _In_ POOL_TYPE PoolType,
  _In_ SIZE_T    NumberOfBytes,
  _In_ ULONG     Tag
);
````


## -parameters
<dl>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the type of pool memory to allocate. For a description of the available pool memory types, see <a href="..\wdm\ne-wdm--pool-type.md">POOL_TYPE</a>.</p>
<p>You can modify the <i>PoolType</i> value by bitwise-ORing this value with the POOL_QUOTA_FAIL_INSTEAD_OF_RAISE flag. This flag causes the routine to return a <b>NULL</b> value if the request cannot be satisfied.</p>
<p>Similarly, you can modify the <i>PoolType</i> value by bitwise-ORing this value with the POOL_COLD_ALLOCATION flag as a hint to the kernel to allocate the memory from pages that are likely to be paged out quickly. To reduce the amount of resident pool memory as much as possible, you should not reference these allocations frequently. The POOL_COLD_ALLOCATION flag is only advisory and is supported in Windows XP and later versions of the Windows operating system.</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>Specifies the number of bytes to allocate.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Specifies the pool tag for the allocated memory. For more information, see the <i>Tag</i> parameter of <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>.</p>
</dd>
</dl>

## -returns
<p><b>ExAllocatePoolWithQuotaTag</b> returns a pointer to the allocated pool.</p>

<p>If the request cannot be satisfied, <b>ExAllocatePoolWithQuotaTag</b> raises an exception unless POOL_QUOTA_FAIL_INSTEAD_OF_RAISE is specified. Using POOL_QUOTA_FAIL_INSTEAD_OF_RAISE is preferred for performance reasons.</p>

## -remarks
<p>This routine is called by highest-level drivers that allocate memory to satisfy a request in the context of the process that originally made the I/O request. Lower-level drivers call <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a> instead.</p>

<p>If <i>NumberOfBytes</i> is PAGE_SIZE or greater, a page-aligned buffer is allocated. Memory allocations of PAGE_SIZE or less are allocated within a page and do not cross page boundaries. Memory allocations of less than PAGE_SIZE are not necessarily page-aligned but are aligned to 8-byte boundaries in 32-bit systems and to 16-byte boundaries in 64-bit systems.</p>

<p>The system associates the pool tag with the allocated memory. Programming tools, such as WinDbg, can display the pool tag associated with each allocated buffer. The value of <i>Tag</i> is normally displayed in reversed order. For example, if a caller passes 'Fred' as a <i>Tag</i>, it would appear as 'derF' if the pool is dumped or when tracking pool usage in the debugger.</p>

<p>The allocated buffer can be freed with either <a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a> or <a href="..\wdm\nf-wdm-exfreepoolwithtag.md">ExFreePoolWithTag</a>.</p>

<p>The system automatically sets certain standard event objects when the amount of pool (paged or nonpaged) is high or low. Drivers can wait for these events to tune their pool usage. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563847">Standard Event Objects</a>.</p>

<p>In a non-uniform memory access (NUMA) multiprocessor architecture, <b>ExAllocatePoolWithQuotaTag</b> tries to allocate memory that is local to the processor that is calling <b>ExAllocatePoolWithQuotaTag</b>. If no local memory is available, <b>ExAllocatePoolWithQuotaTag</b> allocates the closest available memory.</p>

<p>Callers of <b>ExAllocatePoolWithQuotaTag</b> must be executing at IRQL &lt;= DISPATCH_LEVEL. A caller executing at DISPATCH_LEVEL must specify a <b>NonPaged</b><i>Xxx</i> value for <i>PoolType</i>. A caller executing at IRQL &lt;= APC_LEVEL can specify any <b>POOL_TYPE</b> value, but the IRQL and environment must also be considered for determining the pool type.</p>

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
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_spnowait">SpNoWait</a>, <a href="devtest.storport_storportstartio">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exfreepoolwithtag.md">ExFreePoolWithTag</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--pool-type.md">POOL_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExAllocatePoolWithQuotaTag routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

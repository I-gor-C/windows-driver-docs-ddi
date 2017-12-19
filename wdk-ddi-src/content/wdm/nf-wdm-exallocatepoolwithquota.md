---
UID: NF.wdm.ExAllocatePoolWithQuota
title: ExAllocatePoolWithQuota function
author: windows-driver-content
description: The ExAllocatePoolWithQuota routine is obsolete, and is exported only for existing driver binaries. Use ExAllocatePoolWithQuotaTag instead.ExAllocatePoolWithQuota allocates pool memory, charging quota against the current process.
old-location: kernel\exallocatepoolwithquota.htm
old-project: kernel
ms.assetid: cfdfae5e-4669-4e88-82d2-35fb2bca3012
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ExAllocatePoolWithQuota
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Obsolete. This routine is exported only for existing driver binaries. Use ExAllocatePoolWithQuotaTag instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExAllocatePoolWithQuota
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
req.product: Windows 10 or later.
---

# ExAllocatePoolWithQuota function



## -description
The <b>ExAllocatePoolWithQuota</b> routine is <u>obsolete</u>, and is exported only for existing driver binaries. Use <a href="kernel.exallocatepoolwithquotatag">ExAllocatePoolWithQuotaTag</a> instead.

<b>ExAllocatePoolWithQuota</b> allocates pool memory, charging quota against the current process.



## -syntax

````
PVOID ExAllocatePoolWithQuota(
  _In_ POOL_TYPE PoolType,
  _In_ SIZE_T    NumberOfBytes
);
````


## -parameters

### -param PoolType [in]

Specifies the type of pool memory to allocate. For a description of the available pool memory types, see <a href="kernel.pool_type">POOL_TYPE</a>.

You can modify <i>PoolType</i> by using a bitwise OR with the POOL_COLD_ALLOCATION flag as a hint to the kernel to allocate the memory from pages that are likely to be paged out quickly. To reduce the amount of resident pool memory as much as possible, you should not reference these allocations frequently. The POOL_COLD_ALLOCATION flag is only advisory and is available for Windows XP and later versions of the Windows operating system.


### -param NumberOfBytes [in]

Specifies the number of bytes to allocate.


## -returns
<b>ExAllocatePoolWithQuota</b> returns a pointer to the allocated pool.

If the request cannot be satisfied, <b>ExAllocatePoolWithQuota</b> raises an exception.


## -remarks
This routine is called by highest-level drivers that allocate memory to satisfy a request in the context of the process that originally made the I/O request. Lower-level drivers call <a href="kernel.exallocatepoolwithtag">ExAllocatePoolWithTag</a> instead.

If <i>NumberOfBytes</i> is PAGE_SIZE or greater, a page-aligned buffer is allocated. Quota is <u>not</u> charged to the process for allocations of PAGE_SIZE or greater.

Memory allocations of less than PAGE_SIZE are allocated within a page and do not cross page boundaries. Memory allocations of PAGE_SIZE or less are not necessarily page-aligned but are aligned to 8-byte boundaries in 32-bit systems and to 16-byte boundaries in 64-bit systems.

The system automatically sets certain standard event objects when the amount of pool (paged or nonpaged) is high or low. Drivers can wait for these events to tune their pool usage. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563847">Standard Event Objects</a>.

Callers of <b>ExAllocatePoolWithQuota</b> must be executing at IRQL &lt;= DISPATCH_LEVEL. A caller executing at DISPATCH_LEVEL must specify a <b>NonPaged</b><i>Xxx</i> value for <i>PoolType</i>. A caller executing at IRQL &lt;= APC_LEVEL can specify any <b>POOL_TYPE</b> value, but the IRQL and environment must also be considered for determining the pool type.


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
Obsolete. This routine is exported only for existing driver binaries. Use <a href="kernel.exallocatepoolwithquotatag">ExAllocatePoolWithQuotaTag</a> instead.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
&lt;= DISPATCH_LEVEL (see Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_spnowait">SpNoWait</a>, <a href="devtest.storport_storportstartio">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exallocatepoolwithtag">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="kernel.exallocatepoolwithquotatag">ExAllocatePoolWithQuotaTag</a>
</dt>
<dt>
<a href="kernel.exfreepool">ExFreePool</a>
</dt>
<dt>
<a href="kernel.pool_type">POOL_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExAllocatePoolWithQuota routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


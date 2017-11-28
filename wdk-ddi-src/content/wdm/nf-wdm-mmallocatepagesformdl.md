---
UID: NF.wdm.MmAllocatePagesForMdl
title: MmAllocatePagesForMdl
author: windows-driver-content
description: The MmAllocatePagesForMdl routine allocates zero-filled, nonpaged, physical memory pages to an MDL.
old-location: kernel\mmallocatepagesformdl.htm
old-project: kernel
ms.assetid: 06b52af0-c2d3-444e-8714-4fce4181dddc
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MmAllocatePagesForMdl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows; however, MmAllocatePagesForMdlEx should be used instead of MmAllocatePagesForMdl in Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmAllocatePagesForMdl
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
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# MmAllocatePagesForMdl function



## -description
<p>The <b>MmAllocatePagesForMdl</b> routine allocates zero-filled, nonpaged, physical memory pages to an MDL.</p>


## -syntax

````
PMDL MmAllocatePagesForMdl(
  _In_ PHYSICAL_ADDRESS LowAddress,
  _In_ PHYSICAL_ADDRESS HighAddress,
  _In_ PHYSICAL_ADDRESS SkipBytes,
  _In_ SIZE_T           TotalBytes
);
````


## -parameters
<dl>

### -param <i>LowAddress</i> [in]

<dd>
<p>Specifies the physical address of the start of the first address range from which the allocated pages can come. If <b>MmAllocatePagesForMdl</b> cannot allocate the requested number of bytes in the first address range, it iterates through additional address ranges to get more pages. At each iteration, <b>MmAllocatePagesForMdl</b> adds the value of <i>SkipBytes</i> to the previous start address to obtain the start of the next address range.</p>
</dd>

### -param <i>HighAddress</i> [in]

<dd>
<p>Specifies the physical address of the end of the first address range from which the allocated pages can come. </p>
</dd>

### -param <i>SkipBytes</i> [in]

<dd>
<p>Specifies the number of bytes to skip from the start of the previous address range from which the allocated pages can come. <i>SkipBytes</i> must be an integer multiple of the virtual memory page size, in bytes. </p>
</dd>

### -param <i>TotalBytes</i> [in]

<dd>
<p>Specifies the total number of bytes to allocate for the MDL. </p>
</dd>
</dl>

## -returns
<p><b>MmAllocatePagesForMdl</b> returns one of the following:</p><dl>
<dt><b>MDL pointer</b></dt>
</dl><p>The MDL pointer describes a set of physical pages in the specified address range. If the requested number of bytes is not available, the MDL describes as much physical memory as is available. </p><dl>
<dt><b><b>NULL</b></b></dt>
</dl><p>There are no physical memory pages in the specified address ranges, or there is not enough memory pool for the MDL itself. </p>

<p> </p>

## -remarks
<p>Drivers that are running in Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554489">MmAllocatePagesForMdlEx</a> routine instead of <b>MmAllocatePagesForMdl</b>. <b>MmAllocatePagesForMdlEx</b> provides better performance than <b>MmAllocatePagesForMdl</b> by avoiding unnecessary flushes of the <a href="wdkgloss.t#wdkgloss.tlb#wdkgloss.tlb"><i>TLB</i></a> and cache memory.</p>

<p>The physical memory pages that are returned by <b>MmAllocatePagesForMdl</b> are typically not contiguous pages. <b>MmAllocatePagesForMdl</b> always fills the allocated pages in the returned MDL with zeros.</p>

<p><b>MmAllocatePagesForMdl</b> is designed to be used by kernel-mode drivers that do not need corresponding virtual addresses (that is, they need physical pages and do not need the pages to be physically contiguous) or by kernel-mode drivers that can achieve substantial performance gains if physical memory for a device is allocated in a specific physical address range. A driver for an AGP graphics card is an example of such a driver.</p>

<p>Depending on how much physical memory is currently available in the requested ranges, <b>MmAllocatePagesForMdl</b> might return an MDL that describes less memory than was requested. The routine returns <b>NULL</b> if no memory was allocated. The caller should check the amount of memory that is actually allocated to the MDL. </p>

<p>The caller must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554521">MmFreePagesFromMdl</a> to release the memory pages that are described by an MDL that was created by <b>MmAllocatePagesForMdl</b>. After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> to release the memory that is allocated for the MDL structure itself.</p>

<p>In Windows 2000 and later versions of Windows, the maximum amount of memory that <b>MmAllocatePagesForMdl</b> can allocate in a single call is (4 gigabytes - PAGE_SIZE). The routine can satisfy an allocation request for this amount only if enough pages are available.</p>

<p><b>MmAllocatePagesForMdl</b> runs at IRQL &lt;= APC_LEVEL. Windows Server 2008 and later versions of the Windows operating system enable <b>MmAllocatePagesForMdl</b> callers to call at DISPATCH_LEVEL. However, you can improve driver performance by calling at APC_LEVEL or below. </p>

<p>Drivers that are running in Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554489">MmAllocatePagesForMdlEx</a> routine instead of <b>MmAllocatePagesForMdl</b>. <b>MmAllocatePagesForMdlEx</b> provides better performance than <b>MmAllocatePagesForMdl</b> by avoiding unnecessary flushes of the <a href="wdkgloss.t#wdkgloss.tlb#wdkgloss.tlb"><i>TLB</i></a> and cache memory.</p>

<p>The physical memory pages that are returned by <b>MmAllocatePagesForMdl</b> are typically not contiguous pages. <b>MmAllocatePagesForMdl</b> always fills the allocated pages in the returned MDL with zeros.</p>

<p><b>MmAllocatePagesForMdl</b> is designed to be used by kernel-mode drivers that do not need corresponding virtual addresses (that is, they need physical pages and do not need the pages to be physically contiguous) or by kernel-mode drivers that can achieve substantial performance gains if physical memory for a device is allocated in a specific physical address range. A driver for an AGP graphics card is an example of such a driver.</p>

<p>Depending on how much physical memory is currently available in the requested ranges, <b>MmAllocatePagesForMdl</b> might return an MDL that describes less memory than was requested. The routine returns <b>NULL</b> if no memory was allocated. The caller should check the amount of memory that is actually allocated to the MDL. </p>

<p>The caller must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554521">MmFreePagesFromMdl</a> to release the memory pages that are described by an MDL that was created by <b>MmAllocatePagesForMdl</b>. After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> to release the memory that is allocated for the MDL structure itself.</p>

<p>In Windows 2000 and later versions of Windows, the maximum amount of memory that <b>MmAllocatePagesForMdl</b> can allocate in a single call is (4 gigabytes - PAGE_SIZE). The routine can satisfy an allocation request for this amount only if enough pages are available.</p>

<p><b>MmAllocatePagesForMdl</b> runs at IRQL &lt;= APC_LEVEL. Windows Server 2008 and later versions of the Windows operating system enable <b>MmAllocatePagesForMdl</b> callers to call at DISPATCH_LEVEL. However, you can improve driver performance by calling at APC_LEVEL or below. </p>

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
<p>Available in Windows 2000 and later versions of Windows; however, <b>MmAllocatePagesForMdlEx</b> should be used instead of <b>MmAllocatePagesForMdl</b> in Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows.</p>
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
<p>See Remarks section.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554489">MmAllocatePagesForMdlEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554521">MmFreePagesFromMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554622">MmMapLockedPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocatePagesForMdl routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

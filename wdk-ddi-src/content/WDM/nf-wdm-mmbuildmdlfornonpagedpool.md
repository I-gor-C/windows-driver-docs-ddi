---
UID: NF.wdm.MmBuildMdlForNonPagedPool
title: MmBuildMdlForNonPagedPool
author: windows-driver-content
description: The MmBuildMdlForNonPagedPool routine receives an MDL that specifies a nonpaged virtual memory buffer, and updates it to describe the underlying physical pages.
old-location: kernel\mmbuildmdlfornonpagedpool.htm
ms.assetid: f83a9a57-be44-4aa0-bb2e-740f48d82e06
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
req.alt-api: MmBuildMdlForNonPagedPool
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: MmBuildMdlForNonPagedPool
req.iface: 
req.product: Windows 10 or later.
---

# MmBuildMdlForNonPagedPool function



## -description
<p>The <b>MmBuildMdlForNonPagedPool</b> routine receives an MDL that specifies a nonpaged virtual memory buffer, and updates it to describe the underlying physical pages. </p>


## -syntax

````
VOID MmBuildMdlForNonPagedPool(
  _Inout_ PMDLX MemoryDescriptorList
);
````


## -parameters
<dl>

### -param <i>MemoryDescriptorList</i> [in, out]

<dd>
<p>A pointer to an MDL that specifies a virtual memory buffer in nonpaged memory. The caller used the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a> routine to create the MDL for this buffer. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>At entry, the specified MDL must describe a buffer in nonpaged system memory, such as memory that is allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a> routine with <i>PoolType</i> = <b>NonPagedPool</b> or by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554464">MmAllocateContiguousMemorySpecifyCache</a> routine. <b>MmBuildMdlForNonPagedPool</b> updates the MDL to describe the underlying physical pages.</p>

<p><b>MmBuildMdlForNonPagedPool</b> may not be used with MDLs describing buffers allocated on a kernel stack. To build an MDL describing a kernel stack buffer, drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>. This rule applies even if the driver guarantees that the kernel stack cannot be paged out.</p>

<p>Because the pages described by the MDL are already nonpageable and are already mapped to the system address space, drivers must not try to lock them by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a> routine, or to create additional system-address-space mappings by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a> routine. Similarly, drivers must not try to unlock the pages by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556381">MmUnlockPages</a> routine, or to release the existing system-address-space mapping by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556391">MmUnmapLockedPages</a> routine. If a driver performs any of these illegal operations on an MDL that is built by <b>MmBuildMdlForNonPagedPool,</b> the resulting behavior is undefined.</p>

<p>Passing an MDL built by <b>MmBuildMdlForNonPagedPool</b> to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554559">MmGetSystemAddressForMdlSafe</a> routine is allowed. The <b>MmGetSystemAddressForMdlSafe</b> call, in this case, simply returns the starting virtual address of the buffer that is described by the MDL.</p>

<p>A driver can use the <b>MmMapLockedPagesSpecifyCache</b> routine to map an MDL that is built by <b>MmBuildMdlForNonPagedPool</b> into user virtual address space. However, the driver must perform this operation in a way that avoids certain security issues. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a>. </p>

<p>At entry, the specified MDL must describe a buffer in nonpaged system memory, such as memory that is allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a> routine with <i>PoolType</i> = <b>NonPagedPool</b> or by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554464">MmAllocateContiguousMemorySpecifyCache</a> routine. <b>MmBuildMdlForNonPagedPool</b> updates the MDL to describe the underlying physical pages.</p>

<p><b>MmBuildMdlForNonPagedPool</b> may not be used with MDLs describing buffers allocated on a kernel stack. To build an MDL describing a kernel stack buffer, drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>. This rule applies even if the driver guarantees that the kernel stack cannot be paged out.</p>

<p>Because the pages described by the MDL are already nonpageable and are already mapped to the system address space, drivers must not try to lock them by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a> routine, or to create additional system-address-space mappings by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a> routine. Similarly, drivers must not try to unlock the pages by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556381">MmUnlockPages</a> routine, or to release the existing system-address-space mapping by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556391">MmUnmapLockedPages</a> routine. If a driver performs any of these illegal operations on an MDL that is built by <b>MmBuildMdlForNonPagedPool,</b> the resulting behavior is undefined.</p>

<p>Passing an MDL built by <b>MmBuildMdlForNonPagedPool</b> to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554559">MmGetSystemAddressForMdlSafe</a> routine is allowed. The <b>MmGetSystemAddressForMdlSafe</b> call, in this case, simply returns the starting virtual address of the buffer that is described by the MDL.</p>

<p>A driver can use the <b>MmMapLockedPagesSpecifyCache</b> routine to map an MDL that is built by <b>MmBuildMdlForNonPagedPool</b> into user virtual address space. However, the driver must perform this operation in a way that avoids certain security issues. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a>. </p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554464">MmAllocateContiguousMemorySpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554559">MmGetSystemAddressForMdlSafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556381">MmUnlockPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556391">MmUnmapLockedPages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmBuildMdlForNonPagedPool routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

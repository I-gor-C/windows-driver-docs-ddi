---
UID: NF.ntddk.MmLockPagableSectionByHandle
title: MmLockPagableSectionByHandle
author: windows-driver-content
description: The MmLockPagableSectionByHandle routine locks a pageable code or data section into system memory by incrementing the reference count on the handle to the section.
old-location: kernel\mmlockpagablesectionbyhandle.htm
ms.assetid: d2e50d98-1c25-4ed6-98eb-0fb7e71fda55
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmLockPagableSectionByHandle
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlMmApcLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
ms.keywords: MmLockPagableSectionByHandle
req.iface: 
---

# MmLockPagableSectionByHandle function



## -description
<p>The <b>MmLockPagableSectionByHandle</b> routine locks a pageable code or data section into system memory by incrementing the reference count on the handle to the section.</p>


## -syntax

````
VOID MmLockPagableSectionByHandle(
  _In_ PVOID ImageSectionHandle
);
````


## -parameters
<dl>

### -param <i>ImageSectionHandle</i> [in]

<dd>
<p>The handle to a pageable code or data section. The caller obtained this handle from a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554601">MmLockPagableCodeSection</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554607">MmLockPagableDataSection</a> routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver initially calls <b>MmLockPagableCodeSection</b> or <b>MmLockPagableDataSection</b> to obtain a handle to a pageable code or data section. Thereafter, the driver can call <b>MmLockPagableSectionByHandle</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556377">MmUnlockPagableImageSection</a> to increment and decrement the reference count on the handle.</p>

<p>The <b>MmLockPagableCodeSection</b> or <b>MmLockPagableDataSection</b> call locks the pageable section into system memory, returns a handle to the section, and initializes the reference count on the handle to one. <b>MmLockPagableSectionByHandle</b> increments the reference count by one, and <b>MmUnlockPagableImageSection</b> decrements the reference count by one.</p>

<p>If the reference count on the handle is nonzero, the pageable section is locked. If the reference count is zero, the section is unlocked.</p>

<p>The handle to the pageable section remains valid as long as the driver stays loaded in memory. The driver can use the same handle to repeatedly lock and unlock the section. That is, the driver can reuse a handle whose reference count is zero. <b>MmLockPagableSectionByHandle</b> checks to see if the referenced section is resident in the caller's address space and, if it is, simply increments the reference count on the section. If the section is not resident, <b>MmLockPagableSectionByHandle</b> pages in the section, locks it in system space, and sets the reference count to one.</p>

<p>To avoid leaking system memory, the reference count on the handle must be zero when the driver is unloaded from memory. Otherwise, the pageable section will stay locked into system memory after the driver unloads.</p>

<p>If the driver is preparing to unload, and the reference count on the handle is nonzero, the driver should call <b>MmUnlockPagableImageSection</b> to decrement the count to zero before the unload occurs.</p>

<p>A driver cannot call <b>MmLockPagableSectionByHandle</b> to lock down user buffers passed in IRPs. Use <b>MmProbeAndLockPages</b> instead.</p>

<p>For more information about paging code and data, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554346">Making Drivers Pageable</a>.</p>

<p>A driver initially calls <b>MmLockPagableCodeSection</b> or <b>MmLockPagableDataSection</b> to obtain a handle to a pageable code or data section. Thereafter, the driver can call <b>MmLockPagableSectionByHandle</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556377">MmUnlockPagableImageSection</a> to increment and decrement the reference count on the handle.</p>

<p>The <b>MmLockPagableCodeSection</b> or <b>MmLockPagableDataSection</b> call locks the pageable section into system memory, returns a handle to the section, and initializes the reference count on the handle to one. <b>MmLockPagableSectionByHandle</b> increments the reference count by one, and <b>MmUnlockPagableImageSection</b> decrements the reference count by one.</p>

<p>If the reference count on the handle is nonzero, the pageable section is locked. If the reference count is zero, the section is unlocked.</p>

<p>The handle to the pageable section remains valid as long as the driver stays loaded in memory. The driver can use the same handle to repeatedly lock and unlock the section. That is, the driver can reuse a handle whose reference count is zero. <b>MmLockPagableSectionByHandle</b> checks to see if the referenced section is resident in the caller's address space and, if it is, simply increments the reference count on the section. If the section is not resident, <b>MmLockPagableSectionByHandle</b> pages in the section, locks it in system space, and sets the reference count to one.</p>

<p>To avoid leaking system memory, the reference count on the handle must be zero when the driver is unloaded from memory. Otherwise, the pageable section will stay locked into system memory after the driver unloads.</p>

<p>If the driver is preparing to unload, and the reference count on the handle is nonzero, the driver should call <b>MmUnlockPagableImageSection</b> to decrement the count to zero before the unload occurs.</p>

<p>A driver cannot call <b>MmLockPagableSectionByHandle</b> to lock down user buffers passed in IRPs. Use <b>MmProbeAndLockPages</b> instead.</p>

<p>For more information about paging code and data, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554346">Making Drivers Pageable</a>.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/075f5710-b2bf-4546-9648-661a3c8521f8">IrqlMmApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554607">MmLockPagableDataSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554601">MmLockPagableCodeSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554650">MmPageEntireDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554680">MmResetDriverPaging</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556377">MmUnlockPagableImageSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmLockPagableSectionByHandle routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

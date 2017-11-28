---
UID: NF.wdm.MmUnlockPagableImageSection
title: MmUnlockPagableImageSection
author: windows-driver-content
description: The MmUnlockPagableImageSection routine releases a section of driver code or driver data, previously locked into system space with MmLockPagableCodeSection, MmLockPagableDataSection or MmLockPagableSectionByHandle, so the section can be paged out again.
old-location: kernel\mmunlockpagableimagesection.htm
old-project: kernel
ms.assetid: 3a6e3029-d378-4e42-8556-e3640cfdb392
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MmUnlockPagableImageSection
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
req.alt-api: MmUnlockPagableImageSection
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
req.irql: <=APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# MmUnlockPagableImageSection function



## -description
<p>The <b>MmUnlockPagableImageSection</b> routine releases a section of driver code or driver data, previously locked into system space with <b>MmLockPagableCodeSection</b>, <b>MmLockPagableDataSection</b> or <b>MmLockPagableSectionByHandle</b>, so the section can be paged out again. </p>


## -syntax

````
VOID MmUnlockPagableImageSection(
  _In_ PVOID ImageSectionHandle
);
````


## -parameters
<dl>

### -param <i>ImageSectionHandle</i> [in]

<dd>
<p>Specifies the handle returned by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff554601">MmLockPagableCodeSection</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554607">MmLockPagableDataSection</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The handle for a driver's pageable section must not be released if the driver has any outstanding IRPs in its device queue(s) or internal queue(s). A call to <b>MmUnlockPagableImageSection</b> restores the pageability of that entire section when there are no more references to the handle for that section. </p>

<p>The memory manager maintains the reference count on the handle to a section. A pageable section is only available to be paged out when the reference count is zero. Every lock request increments the count; every unlock request decrements the count. A driver must unlock a section as many times as it locks a section to make the section available to be paged out.</p>

<p>A handle is always valid, no matter what the count. If the count on a handle is zero and a call is made to <b>MmLockPagableSectionByHandle</b>, the count is set to one, and if the section has been paged out, it will be paged in.</p>

<p>In most cases, <b>MmUnlockPagableImageSection</b> is called before a driver's <i>Unload</i> routine. That is, a driver with a pageable section is likely to have its <i>DispatchClose</i> and/or <i>DispatchShutdown</i> routine call <b>MmUnlockPagableImageSection</b> before its <i>Unload</i> routine is called. However, care should be taken in unloadable drivers to release any pageable section before the driver itself is unloaded from the system.</p>

<p>For more information about paging code and data, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554346">Making Drivers Pageable</a>. </p>

<p>The handle for a driver's pageable section must not be released if the driver has any outstanding IRPs in its device queue(s) or internal queue(s). A call to <b>MmUnlockPagableImageSection</b> restores the pageability of that entire section when there are no more references to the handle for that section. </p>

<p>The memory manager maintains the reference count on the handle to a section. A pageable section is only available to be paged out when the reference count is zero. Every lock request increments the count; every unlock request decrements the count. A driver must unlock a section as many times as it locks a section to make the section available to be paged out.</p>

<p>A handle is always valid, no matter what the count. If the count on a handle is zero and a call is made to <b>MmLockPagableSectionByHandle</b>, the count is set to one, and if the section has been paged out, it will be paged in.</p>

<p>In most cases, <b>MmUnlockPagableImageSection</b> is called before a driver's <i>Unload</i> routine. That is, a driver with a pageable section is likely to have its <i>DispatchClose</i> and/or <i>DispatchShutdown</i> routine call <b>MmUnlockPagableImageSection</b> before its <i>Unload</i> routine is called. However, care should be taken in unloadable drivers to release any pageable section before the driver itself is unloaded from the system.</p>

<p>For more information about paging code and data, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554346">Making Drivers Pageable</a>. </p>

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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlmmapclte">IrqlMmApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554650">MmPageEntireDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554680">MmResetDriverPaging</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554601">MmLockPagableCodeSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554607">MmLockPagableDataSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554610">MmLockPagableSectionByHandle</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmUnlockPagableImageSection routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

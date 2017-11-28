---
UID: NF.wdm.MmPageEntireDriver
title: MmPageEntireDriver
author: windows-driver-content
description: The MmPageEntireDriver routine causes all of a driver's code and data to be made pageable, overriding the attributes of the various sections that make up the driver's image.
old-location: kernel\mmpageentiredriver.htm
old-project: kernel
ms.assetid: 467a8e64-c4ed-4bd0-81f8-b792367d33bf
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MmPageEntireDriver
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
req.alt-api: MmPageEntireDriver
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
req.iface: 
req.product: Windows 10 or later.
---

# MmPageEntireDriver function



## -description
<p>The <b>MmPageEntireDriver</b> routine causes all of a driver's code and data to be made pageable, overriding the attributes of the various sections that make up the driver's image.</p>


## -syntax

````
PVOID MmPageEntireDriver(
  _In_ PVOID AddressWithinSection
);
````


## -parameters
<dl>

### -param <i>AddressWithinSection</i> [in]

<dd>
<p>Pointer to a virtual address within the driver (for example, the address of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine).</p>
</dd>
</dl>

## -returns
<p><b>MmPageEntireDriver</b> returns a pointer to the beginning of the driver image in memory.</p>

## -remarks
<p>Use this routine to force a driver to be completely pageable. Drivers that call <b>MmPageEntireDriver</b> must not have an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547958">InterruptService</a> routine (ISR) registered for any interrupts. If the interrupt occurs while the driver is paged out, the system issues a bug check.</p>

<p>The effect of a call to <b>MmPageEntireDriver</b> can be undone by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554680">MmResetDriverPaging</a>.</p>

<p>If the driver is already completely pageable, calling <b>MmPageEntireDriver</b> has no effect. For more information about paging an entire driver, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554346">Making Drivers Pageable</a>.</p>

<p>Use this routine to force a driver to be completely pageable. Drivers that call <b>MmPageEntireDriver</b> must not have an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547958">InterruptService</a> routine (ISR) registered for any interrupts. If the interrupt occurs while the driver is paged out, the system issues a bug check.</p>

<p>The effect of a call to <b>MmPageEntireDriver</b> can be undone by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554680">MmResetDriverPaging</a>.</p>

<p>If the driver is already completely pageable, calling <b>MmPageEntireDriver</b> has no effect. For more information about paging an entire driver, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554346">Making Drivers Pageable</a>.</p>

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
<p>&lt;= APC_LEVEL</p>
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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556377">MmUnlockPagableImageSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmPageEntireDriver routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

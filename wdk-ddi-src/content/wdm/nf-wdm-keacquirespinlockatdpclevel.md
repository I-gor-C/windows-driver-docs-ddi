---
UID: NF.wdm.KeAcquireSpinLockAtDpcLevel
title: KeAcquireSpinLockAtDpcLevel
author: windows-driver-content
description: The KeAcquireSpinLockAtDpcLevel routine acquires a spin lock when the caller is already running at IRQL &gt;= DISPATCH_LEVEL.
old-location: kernel\keacquirespinlockatdpclevel.htm
old-project: kernel
ms.assetid: 010b5e42-26c7-433f-b67b-1afdc0ec564c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeAcquireSpinLockAtDpcLevel
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
req.alt-api: KeAcquireSpinLockAtDpcLevel,KefAcquireSpinLockAtDpcLevel
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs, IrqlDispatch, SpinLockSafe
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

# KeAcquireSpinLockAtDpcLevel function



## -description
<p>The <b>KeAcquireSpinLockAtDpcLevel</b> routine acquires a spin lock when the caller is already running at IRQL &gt;= DISPATCH_LEVEL. </p>


## -syntax

````
VOID KeAcquireSpinLockAtDpcLevel(
  _Inout_ PKSPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param <i>SpinLock</i> [in, out]

<dd>
<p>Pointer to an initialized spin lock for which the caller must provide the storage.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers call <b>KeAcquireSpinLockAtDpcLevel</b> instead of <a href="..\wdm\nf-wdm-keacquirespinlock.md">KeAcquireSpinLock</a> for better driver performance if and only if they are already running at an IRQL of DISPATCH_LEVEL or above.</p>

<p>If a driver is running at IRQL &lt;= APC_LEVEL, it should call <b>KeAcquireSpinLock</b> to have IRQL raised by that routine. <b>KeAcquireSpinLockAtDpcLevel</b> assumes the caller is already running at IRQL &gt;= DISPATCH_LEVEL, so no raise is necessary.</p>

<p>The caller should release the spin lock with <a href="..\wdm\nf-wdm-kereleasespinlockfromdpclevel.md">KeReleaseSpinLockFromDpcLevel</a> as quickly as possible.</p>

<p>For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>.</p>

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
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_irqldispatch">IrqlDispatch</a>, <a href="devtest.storport_spinlocksafe">SpinLockSafe</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keacquireinstackqueuedspinlockatdpclevel">KeAcquireInStackQueuedSpinLockAtDpcLevel</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keacquirespinlock.md">KeAcquireSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializespinlock.md">KeInitializeSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kereleasespinlock.md">KeReleaseSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kereleasespinlockfromdpclevel.md">KeReleaseSpinLockFromDpcLevel</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ketrytoacquirespinlockatdpclevel.md">KeTryToAcquireSpinLockAtDpcLevel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeAcquireSpinLockAtDpcLevel routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

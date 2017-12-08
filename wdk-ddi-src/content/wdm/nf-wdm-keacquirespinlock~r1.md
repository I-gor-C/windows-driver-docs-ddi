---
UID: NF.wdm.KeAcquireSpinLock~r1
title: KeAcquireSpinLock
author: windows-driver-content
description: The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL.
old-location: kernel\keacquirespinlock.htm
old-project: kernel
ms.assetid: 10999175-4793-4045-8a74-a9a491724ec9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeAcquireSpinLock
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
req.alt-api: KeAcquireSpinLock
req.alt-loc: Hal.lib,Hal.dll
req.ddi-compliance: IrqlKeDispatchLte, MarkingQueuedIrps, SpinLock, SpinLockDpc, SpinlockRelease, SpinLockSafe, ReqSendWhileSpinlock, Spinlock(kmdf), SpinlockDpc(kmdf), SpinlockRelease(kmdf), HwStorPortProhibitedDDIs, SpinLock(storport), SpinLockDpc(storport), SpinLockRelease(storport), SpinLockSafe(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KeAcquireSpinLock function



## -description
<p>The <b>KeAcquireSpinLock</b> routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL.</p>


## -syntax

````
VOID KeAcquireSpinLock(
  _In_  PKSPIN_LOCK SpinLock,
  _Out_ PKIRQL      OldIrql
);
````


## -parameters
<dl>

### -param SpinLock [in]

<dd>
<p>Pointer to an initialized spin lock for which the caller provides the storage.</p>
</dd>

### -param OldIrql [out]

<dd>
<p>Pointer to a variable that is set to the current IRQL when this call occurs.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>KeAcquireSpinLock</b> first resets the IRQL to DISPATCH_LEVEL and then acquires the lock. The previous IRQL is written to <i>OldIrql</i> after the lock is acquired.</p>

<p>The <i>OldIrql</i> value must be specified when the spin lock is released with <a href="..\wdm\nf-wdm-kereleasespinlock.md">KeReleaseSpinLock</a>.</p>

<p>Most drivers use a local variable to store the old IRQL value. A driver can also use a shared memory location, such as a global variable, but the driver must not use the same location for two different locks. Otherwise, a race condition can occur.</p>

<p>Spin locks can cause serious problems if not used judiciously. In particular, no deadlock protection is performed and dispatching is disabled while the spin lock is held. Therefore:</p>

<p>The code within a critical region guarded by an spin lock must neither be pageable nor make any references to pageable data.</p>

<p>The code within a critical region guarded by a spin lock can neither call any external function that might access pageable data or raise an exception, nor can it generate any exceptions.</p>

<p>The caller should release the spin lock with <b>KeReleaseSpinLock</b> as quickly as possible.</p>

<p>Attempting to acquire a spin lock recursively is guaranteed to cause a deadlock. For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>.</p>

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
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlkedispatchlte">IrqlKeDispatchLte</a>, <a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.wdm_spinlock">SpinLock</a>, <a href="devtest.wdm_spinlockdpc">SpinLockDpc</a>, <a href="devtest.wdm_spinlockrelease">SpinlockRelease</a>, <a href="devtest.wdm_spinlocksafe">SpinLockSafe</a>, <a href="devtest.kmdf_reqsendwhilespinlock">ReqSendWhileSpinlock</a>, <a href="devtest.kmdf_spinlock">Spinlock(kmdf)</a>, <a href="devtest.kmdf_spinlockdpc">SpinlockDpc(kmdf)</a>, <a href="devtest.kmdf_spinlockrelease">SpinlockRelease(kmdf)</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_spinlock">SpinLock(storport)</a>, <a href="devtest.storport_spinlockdpc">SpinLockDpc(storport)</a>, <a href="devtest.storport_spinlockrelease">SpinLockRelease(storport)</a>, <a href="devtest.storport_spinlocksafe">SpinLockSafe(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keacquireinstackqueuedspinlock">KeAcquireInStackQueuedSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keacquirespinlockatdpclevel.md">KeAcquireSpinLockAtDpcLevel</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializespinlock.md">KeInitializeSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kereleasespinlock.md">KeReleaseSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeAcquireSpinLock routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

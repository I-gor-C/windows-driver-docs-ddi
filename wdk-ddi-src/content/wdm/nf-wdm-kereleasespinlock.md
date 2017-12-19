---
UID: NF.wdm.KeReleaseSpinLock
title: KeReleaseSpinLock macro
author: windows-driver-content
description: The KeReleaseSpinLock routine releases a spin lock and restores the original IRQL at which the caller was running.
old-location: kernel\kereleasespinlock.htm
old-project: kernel
ms.assetid: 300cdd3b-0c12-45e3-ae45-c26084f3ec12
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeReleaseSpinLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeReleaseSpinLock
req.alt-loc: Hal.lib,Hal.dll
req.ddi-compliance: IrqlKeReleaseSpinLock, MarkingQueuedIrps, SpinLock, SpinLockDpc, SpinlockRelease, SpinLockSafe, ReqSendWhileSpinlock, Spinlock(kmdf), SpinlockDpc(kmdf), SpinlockRelease(kmdf), HwStorPortProhibitedDDIs, IrqlKeReleaseSpinLock(storport), SpinLock(storport), SpinLockDpc(storport), SpinLockRelease(storport), SpinLockSafe(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: 
req.irql: DISPATCH_LEVEL (see Remarks section)
req.product: Windows 10 or later.
---

# KeReleaseSpinLock macro



## -description
The <b>KeReleaseSpinLock</b> routine releases a spin lock and restores the original IRQL at which the caller was running.



## -syntax

````
VOID KeReleaseSpinLock(
  _Inout_ PKSPIN_LOCK SpinLock,
  _In_    KIRQL       NewIrql
);
````


## -parameters

### -param SpinLock [in, out]

Pointer to a spin lock for which the caller provides the storage.


### -param NewIrql [in]

Specifies the IRQL value saved from the preceding call to <a href="kernel.keacquirespinlock">KeAcquireSpinLock</a>.


## -remarks
This call is a reciprocal to <a href="kernel.keacquirespinlock">KeAcquireSpinLock</a>. The input <i>NewIrql</i> value must be the <i>OldIrql</i> returned by <b>KeAcquireSpinLock</b>.

For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>.

Callers of this routine are running at IRQL = DISPATCH_LEVEL. On return from <b>KeReleaseSpinLock</b>, IRQL is restored to the <i>NewIrql</i> value.


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
Available starting with Windows 2000.

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
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
DISPATCH_LEVEL (see Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlkereleasespinlock">IrqlKeReleaseSpinLock</a>, <a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.wdm_spinlock">SpinLock</a>, <a href="devtest.wdm_spinlockdpc">SpinLockDpc</a>, <a href="devtest.wdm_spinlockrelease">SpinlockRelease</a>, <a href="devtest.wdm_spinlocksafe">SpinLockSafe</a>, <a href="devtest.kmdf_reqsendwhilespinlock">ReqSendWhileSpinlock</a>, <a href="devtest.kmdf_spinlock">Spinlock(kmdf)</a>, <a href="devtest.kmdf_spinlockdpc">SpinlockDpc(kmdf)</a>, <a href="devtest.kmdf_spinlockrelease">SpinlockRelease(kmdf)</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_irqlkereleasespinlock">IrqlKeReleaseSpinLock(storport)</a>, <a href="devtest.storport_spinlock">SpinLock(storport)</a>, <a href="devtest.storport_spinlockdpc">SpinLockDpc(storport)</a>, <a href="devtest.storport_spinlockrelease">SpinLockRelease(storport)</a>, <a href="devtest.storport_spinlocksafe">SpinLockSafe(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keacquirespinlock">KeAcquireSpinLock</a>
</dt>
<dt>
<a href="kernel.keinitializespinlock">KeInitializeSpinLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeReleaseSpinLock routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


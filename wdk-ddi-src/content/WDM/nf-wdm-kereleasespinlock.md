---
UID: NF.wdm.KeReleaseSpinLock
title: KeReleaseSpinLock
author: windows-driver-content
description: The KeReleaseSpinLock routine releases a spin lock and restores the original IRQL at which the caller was running.
old-location: kernel\kereleasespinlock.htm
ms.assetid: 300cdd3b-0c12-45e3-ae45-c26084f3ec12
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
ms.keywords: KeReleaseSpinLock
req.iface: 
req.product: Windows 10 or later.
---

# KeReleaseSpinLock function



## -description
<p>The <b>KeReleaseSpinLock</b> routine releases a spin lock and restores the original IRQL at which the caller was running.</p>


## -syntax

````
VOID KeReleaseSpinLock(
  _Inout_ PKSPIN_LOCK SpinLock,
  _In_    KIRQL       NewIrql
);
````


## -parameters
<dl>

### -param <i>SpinLock</i> [in, out]

<dd>
<p>Pointer to a spin lock for which the caller provides the storage.</p>
</dd>

### -param <i>NewIrql</i> [in]

<dd>
<p>Specifies the IRQL value saved from the preceding call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This call is a reciprocal to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>. The input <i>NewIrql</i> value must be the <i>OldIrql</i> returned by <b>KeAcquireSpinLock</b>.</p>

<p>For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>.</p>

<p>Callers of this routine are running at IRQL = DISPATCH_LEVEL. On return from <b>KeReleaseSpinLock</b>, IRQL is restored to the <i>NewIrql</i> value.</p>

<p>This call is a reciprocal to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>. The input <i>NewIrql</i> value must be the <i>OldIrql</i> returned by <b>KeAcquireSpinLock</b>.</p>

<p>For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>.</p>

<p>Callers of this routine are running at IRQL = DISPATCH_LEVEL. On return from <b>KeReleaseSpinLock</b>, IRQL is restored to the <i>NewIrql</i> value.</p>

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
<p>DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547830">IrqlKeReleaseSpinLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549016">MarkingQueuedIrps</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn926953">SpinLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff819089">SpinLockDpc</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454251">SpinlockRelease</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454252">SpinLockSafe</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551602">ReqSendWhileSpinlock</a>, <a href="https://msdn.microsoft.com/911E4350-851F-4AC4-B982-B2B4B974C243">Spinlock(kmdf)</a>, <a href="https://msdn.microsoft.com/77DA365C-7717-45B6-B8AD-9686B880AB50">SpinlockDpc(kmdf)</a>, <a href="https://msdn.microsoft.com/23BEB857-309D-4C11-A361-D72F87C84154">SpinlockRelease(kmdf)</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/A1AEE8C9-F5F1-4BBE-8291-1E61D73AFC6A">IrqlKeReleaseSpinLock(storport)</a>, <a href="https://msdn.microsoft.com/7D06327F-CE74-4337-8B5C-79189FE15F2F">SpinLock(storport)</a>, <a href="https://msdn.microsoft.com/955B5A37-5E14-4380-A30D-3D019C4D5B59">SpinLockDpc(storport)</a>, <a href="https://msdn.microsoft.com/CD4287CB-EF0C-476C-BF10-B46B96AB7D11">SpinLockRelease(storport)</a>, <a href="https://msdn.microsoft.com/12D36178-C00D-44A7-9DA0-E0663DF1FFDC">SpinLockSafe(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552160">KeInitializeSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeReleaseSpinLock routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

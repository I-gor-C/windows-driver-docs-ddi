---
UID: NF.wdm.KeReleaseSpinLockFromDpcLevel
title: KeReleaseSpinLockFromDpcLevel
author: windows-driver-content
description: The KeReleaseSpinLockFromDpcLevel routine releases an executive spin lock without changing the IRQL.
old-location: kernel\kereleasespinlockfromdpclevel.htm
old-project: kernel
ms.assetid: 5f7a92ee-ebaf-442f-a197-2fb58dd65a25
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeReleaseSpinLockFromDpcLevel
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
req.alt-api: KeReleaseSpinLockFromDpcLevel,KefReleaseSpinLockFromDpcLevel
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
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KeReleaseSpinLockFromDpcLevel function



## -description
<p>The <b>KeReleaseSpinLockFromDpcLevel</b> routine releases an executive spin lock without changing the IRQL.</p>


## -syntax

````
VOID KeReleaseSpinLockFromDpcLevel(
  _Inout_ PKSPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param <i>SpinLock</i> [in, out]

<dd>
<p>Pointer to an executive spin lock for which the caller provides the storage. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers call <b>KeReleaseSpinLockFromDpcLevel</b> to release a spin lock acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551921">KeAcquireSpinLockAtDpcLevel</a>.</p>

<p>It is an error to call <b>KeReleaseSpinLockFromDpcLevel</b> if the specified spin lock was acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a> because the caller's original IRQL is not restored, which can cause deadlocks or fatal page faults.</p>

<p>For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>. </p>

<p>Drivers call <b>KeReleaseSpinLockFromDpcLevel</b> to release a spin lock acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551921">KeAcquireSpinLockAtDpcLevel</a>.</p>

<p>It is an error to call <b>KeReleaseSpinLockFromDpcLevel</b> if the specified spin lock was acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a> because the caller's original IRQL is not restored, which can cause deadlocks or fatal page faults.</p>

<p>For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>. </p>

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547743">IrqlDispatch</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454252">SpinLockSafe</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551921">KeAcquireSpinLockAtDpcLevel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553145">KeReleaseSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeReleaseSpinLockFromDpcLevel routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

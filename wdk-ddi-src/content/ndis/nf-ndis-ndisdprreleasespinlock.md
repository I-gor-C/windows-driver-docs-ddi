---
UID: NF.ndis.NdisDprReleaseSpinLock
title: NdisDprReleaseSpinLock
author: windows-driver-content
description: The NdisDprReleaseSpinLock function releases a spin lock acquired in the immediately preceding call to the NdisDprAcquireSpinLock function.
old-location: netvista\ndisdprreleasespinlock.htm
old-project: netvista
ms.assetid: d6a7af70-6a1e-471b-919f-80a704d25446
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisDprReleaseSpinLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisDprReleaseSpinLock (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisDprReleaseSpinLock (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisDprReleaseSpinLock
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Synch_Function, SpinLock, SpinLockBalanced, SpinLockDpr, SpinLockDprRelease, SpinlockRelease
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
---

# NdisDprReleaseSpinLock function



## -description
<p>The 
  <b>NdisDprReleaseSpinLock</b> function releases a spin lock acquired in the immediately preceding call to
  the 
  <a href="..\ndis\nf-ndis-ndisdpracquirespinlock.md">
  NdisDprAcquireSpinLock</a> function.</p>


## -syntax

````
VOID NdisDprReleaseSpinLock(
  _In_ PNDIS_SPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param <i>SpinLock</i> [in]

<dd>
<p>Pointer to the acquired spin lock to be released.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Release of the spin lock allows another driver function to use the resources the lock protects after
    that function acquires the spin lock.</p>

<p>A spin lock acquired with 
    <b>NdisDprAcquireSpinLock</b> must be released with 
    <b>NdisDprReleaseSpinLock</b>. A spin lock acquired with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff560699">NdisAcquireSpinLock</a> must be released
    with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564524">NdisReleaseSpinLock</a>.</p>

<p>For more information about acquiring and releasing NDIS spin locks, see 
    <a href="netvista.synchronization_and_notification_in_network_drivers">Synchronization
    and Notification in Network Drivers</a>.</p>

<p>Release of the spin lock allows another driver function to use the resources the lock protects after
    that function acquires the spin lock.</p>

<p>A spin lock acquired with 
    <b>NdisDprAcquireSpinLock</b> must be released with 
    <b>NdisDprReleaseSpinLock</b>. A spin lock acquired with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff560699">NdisAcquireSpinLock</a> must be released
    with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564524">NdisReleaseSpinLock</a>.</p>

<p>For more information about acquiring and releasing NDIS spin locks, see 
    <a href="netvista.synchronization_and_notification_in_network_drivers">Synchronization
    and Notification in Network Drivers</a>.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/27178665-3b9c-48bb-827c-f2aa160616b3">NdisDprReleaseSpinLock (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisDprReleaseSpinLock (NDIS
   5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548015">Irql_Synch_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn926953">SpinLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551865">SpinLockBalanced</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552770">SpinLockDpr</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975126">SpinLockDprRelease</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454251">SpinlockRelease</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561749">NdisDprAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisDprReleaseSpinLock function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

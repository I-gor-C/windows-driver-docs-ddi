---
UID: NF.ndis.NdisDprAcquireReadWriteLock
title: NdisDprAcquireReadWriteLock function
author: windows-driver-content
description: The NdisDprAcquireReadWriteLock function acquires a lock that the caller uses for either write or read access to the resources that are shared among driver threads.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisAcquireRWLockRead or NdisAcquireRWLockWrite (setting NDIS_RWL_AT_DISPATCH_LEVEL in the Flags parameter) instead of NdisDprAcquireReadWriteLock.
old-location: netvista\ndisdpracquirereadwritelock.htm
old-project: netvista
ms.assetid: 09B574FA-BCBA-4370-8F9F-BF30CE0BE52D
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisDprAcquireReadWriteLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Deprecated for NDIS 6.20 and later drivers, which should use NdisAcquireRWLockRead or NdisAcquireRWLockWrite instead of NdisDprAcquireReadWriteLock. Supported in NDIS 6.0 and 6.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisDprAcquireReadWriteLock
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: = DISPATCH_LEVEL
---

# NdisDprAcquireReadWriteLock function



## -description
The 
  <a href="netvista.ndisacquirereadwritelock">NdisDprAcquireReadWriteLock</a> function acquires a lock that the caller uses for either write or read
  access to the resources that are shared among driver threads.


## -syntax

````
VOID NdisDprAcquireReadWriteLock(
  _Inout_ PNDIS_RW_LOCK Lock,
  _In_    BOOLEAN       fWrite,
  _Out_   PLOCK_STATE   LockState
);
````


## -parameters

### -param Lock [in, out]

A pointer to an opaque variable that represents a lock. The caller can use this lock to access
     shared resources.

### -param fWrite [in]

A Boolean value. If the value is TRUE, this function is provided with write access to shared
     resources; if the value is FALSE, this function is provided with read access.

### -param LockState [out]

A pointer to an opaque variable that tracks the state of the lock. This variable exists in the
     interval between the time the caller acquires and releases the lock. The caller must use a different
     variable of type <a href="netvista.lock_state">LOCK_STATE</a> for each attempt that it makes to acquire the lock from the same non-ISR
     driver thread.

## -returns
None

## -remarks
The driver must initialize a variable of type <a href="netvista.ndis_rw_lock">NDIS_RW_LOCK</a> using the 
    <a href="netvista.ndisinitializereadwritelock">
    NdisInitializeReadWriteLock</a> function before the driver calls any other 
    Ndis<i>Xxx</i>ReadWriteLock function. The driver must provide resident storage for the locks it uses.

After acquiring a lock by using 
    <a href="netvista.ndisacquirereadwritelock">NdisDprAcquireReadWriteLock</a>, the caller must release that lock by calling the 
    <a href="netvista.ndisreleasereadwritelock">NdisDprReleaseReadWriteLock</a> function. To decrement the reference count of the lock, a driver must call
    
    <b>NdisDprReleaseReadWriteLock</b> once for each call to 
    <b>NdisDprAcquireReadWriteLock</b>.

It is safe to use both <a href="netvista.ndisacquirereadwritelock">NdisDprAcquireReadWriteLock</a> and <b>NdisDprAcquireReadWriteLock</b> on the same lock.  However, calls must be balanced so that if the lock is acquired with <b>NdisDprAcquireReadWriteLock</b>, it must be released with <a href="netvista.ndisreleasereadwritelock">NdisDprReleaseReadWriteLock</a>.  Likewise, if the lock is acquired with <b>NdisAcquireReadWriteLock</b>, it must be released with <b>NdisReleaseReadWriteLock</b>.

With some architectures, <a href="netvista.ndisacquirereadwritelock">NdisDprAcquireReadWriteLock</a>     performs faster than <b>NdisAcquireReadWriteLock</b>.  Drivers can use <b>NdisDprAcquireReadWriteLock</b>  rather than  <b>NdisAcquireReadWriteLock</b> when it is certain that the current IRQL is already <b>DISPATCH_LEVEL</b>.  However, it is not required.  The overhead of calling the <a href="kernel.kegetcurrentirql">KeGetCurrentIrql</a> function is greater than the performance advantage of calling <b>NdisDprAcquireReadWriteLock</b> rather than <b>NdisAcquireReadWriteLock</b>.

To modify resources that are shared among driver threads, a driver thread must acquire a write lock.
    To simply monitor those resources, a driver thread must acquire a read-only lock. Read access does not
    require interlocked operations or contention for spin locks. Using read-only access helps to maintain
    good operating system and driver performance.

A driver thread should never hold a write lock for more than 25 microseconds. Holding a write lock for
    a prolonged period degrades both operating system and driver performance.

The driver cannot use a lock to protect resources from read or write access that its other functions
    share with the 
    <a href="..\ndis\nc-ndis-miniport_isr.md">MiniportInterrupt</a> and/or 
    <a href="..\ndis\nc-ndis-miniport_disable_interrupt.md">
    MiniportDisableInterruptEx</a> functions. Instead, the driver must call 
    <a href="netvista.ndismsynchronizewithinterruptex">NdisMSynchronizeWithInterruptEx</a> so that its 
    <a href="..\ndis\nc-ndis-miniport_synchronize_interrupt.md">
    MiniportSynchronizeInterrupt</a> function accesses such shared resources at the same DIRQL at which its
    
    <i>MiniportInterrupt</i> and/or 
    <i>
    MiniportDisableInterruptEx</i> functions do.

For more information about acquiring and releasing NDIS spin locks, see 
    <a href="netvista.synchronization_and_notification_in_network_drivers">Synchronization
    and Notification in Network Drivers</a>.

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
Deprecated for NDIS 6.20 and later drivers, which should use <a href="netvista.ndisacquirerwlockread">NdisAcquireRWLockRead</a> or <a href="netvista.ndisacquirerwlockwrite">NdisAcquireRWLockWrite</a> instead of <a href="netvista.ndisacquirereadwritelock">NdisDprAcquireReadWriteLock</a>. Supported in NDIS 6.0 and 6.1.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.lock_state">LOCK_STATE</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_disable_interrupt.md">MiniportDisableInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_isr.md">MiniportInterrupt</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_synchronize_interrupt.md">
   MiniportSynchronizeInterrupt</a>
</dt>
<dt>
<a href="netvista.ndisacquirerwlockread">NdisAcquireRWLockRead</a>
</dt>
<dt>
<a href="netvista.ndisacquirerwlockwrite">NdisAcquireRWLockWrite</a>
</dt>
<dt>
<a href="netvista.ndisinitializereadwritelock">NdisInitializeReadWriteLock</a>
</dt>
<dt>
<a href="netvista.ndismsynchronizewithinterruptex">
   NdisMSynchronizeWithInterruptEx</a>
</dt>
<dt>
<a href="netvista.ndisreleasereadwritelock">NdisDprReleaseReadWriteLock</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisDprAcquireReadWriteLock function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

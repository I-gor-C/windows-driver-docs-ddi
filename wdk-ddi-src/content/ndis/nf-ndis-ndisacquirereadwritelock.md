---
UID: NF.ndis.NdisAcquireReadWriteLock
title: NdisAcquireReadWriteLock function
author: windows-driver-content
description: The NdisAcquireReadWriteLock function acquires a lock that the caller uses for either write or read access to the resources that are shared among driver threads.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisAcquireRWLockRead or NdisAcquireRWLockWrite instead of NdisAcquireReadWriteLock.
old-location: netvista\ndisacquirereadwritelock.htm
old-project: netvista
ms.assetid: 563b4bff-36ee-4597-ae6e-7d3811592549
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisAcquireReadWriteLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Deprecated for NDIS 6.20 and later drivers, which should use NdisAcquireRWLockRead or NdisAcquireRWLockWrite instead. Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisAcquireReadWriteLock (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisAcquireReadWriteLock (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisAcquireReadWriteLock
req.alt-loc: ndis.sys
req.ddi-compliance: Irql_Synch_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: Ndis.sys
req.irql: <= DISPATCH_LEVEL
---

# NdisAcquireReadWriteLock function



## -description
The 
  <b>NdisAcquireReadWriteLock</b> function acquires a lock that the caller uses for either write or read
  access to the resources that are shared among driver threads.


## -syntax

````
VOID NdisAcquireReadWriteLock(
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

A Boolean value. If the value is <b>TRUE</b>, this function is provided with write access to shared
     resources; if the value is <b>FALSE</b>, this function is provided with read access.

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
    <b>NdisAcquireReadWriteLock</b>, the caller must release that lock by calling the 
    <a href="netvista.ndisreleasereadwritelock">
    NdisReleaseReadWriteLock</a> function. To decrement the reference count of the lock, a driver must call
    
    <b>NdisReleaseReadWriteLock</b> once for each call to 
    <b>NdisAcquireReadWriteLock</b>.

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
    <a href="netvista.ndismsynchronizewithinterruptex">
    NdisMSynchronizeWithInterruptEx</a> so that its 
    <a href="..\ndis\nc-ndis-miniport_synchronize_interrupt.md">
    MiniportSynchronizeInterrupt</a> function accesses such shared resources at the same DIRQL at which its
    
    <i>MiniportInterrupt</i> and/or 
    <i>
    MiniportDisableInterruptEx</i> functions do.

<b>NdisAcquireReadWriteLock</b> always raises the IRQL. For a write operation, 
    <b>NdisAcquireReadWriteLock</b> raises the IRQL by acquiring a spin lock. For a read operation, 
    <b>NdisAcquireReadWriteLock</b> explicitly raises the IRQL to IRQL = <b>DISPATCH_LEVEL</b>.

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
Deprecated for NDIS 6.20 and later drivers, which should use <a href="netvista.ndisacquirerwlockread">NdisAcquireRWLockRead</a> or <a href="netvista.ndisacquirerwlockwrite">NdisAcquireRWLockWrite</a> instead. Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/fe648a14-431b-4671-9b20-93cfa7ffd55d">NdisAcquireReadWriteLock (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisAcquireReadWriteLock (NDIS
   5.1)</b>) in Windows XP.
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
DLL
</th>
<td width="70%">
<dl>
<dt>Ndis.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.ndis_irql_synch_function">Irql_Synch_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
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
<a href="netvista.ndisreleasereadwritelock">NdisReleaseReadWriteLock</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAcquireReadWriteLock function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

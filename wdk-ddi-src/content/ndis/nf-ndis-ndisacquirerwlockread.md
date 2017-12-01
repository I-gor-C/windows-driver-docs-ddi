---
UID: NF.ndis.NdisAcquireRWLockRead
title: NdisAcquireRWLockRead
author: windows-driver-content
description: The NdisAcquireRWLockRead function obtains a read lock that the caller uses for read access to resources that are shared among driver threads.
old-location: netvista\ndisacquirerwlockread.htm
old-project: netvista
ms.assetid: a9c16537-e344-43d4-bae7-fb11487caa0e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisAcquireRWLockRead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisAcquireRWLockRead
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisAcquireRWLockRead function



## -description
<p>The 
  <b>NdisAcquireRWLockRead</b> function obtains a read lock that the caller uses for read access to resources
  that are shared among driver threads.</p>


## -syntax

````
VOID NdisAcquireRWLockRead(
  _In_  PNDIS_RW_LOCK_EX Lock,
  _Out_ PLOCK_STATE_EX   LockState,
  _In_  UCHAR            Flags
);
````


## -parameters
<dl>

### -param <i>Lock</i> [in]

<dd>
<p>A pointer to an opaque 
     <a href="..\ndis\ns-ndis--ndis-rw-lock-ex.md">NDIS_RW_LOCK_EX</a> variable that represents a
     lock. The caller can use this lock to gain write or read access to resources that are shared between
     non-ISR driver threads.</p>
</dd>

### -param <i>LockState</i> [out]

<dd>
<p>A pointer to an opaque 
     <a href="..\ndis\ns-ndis--lock-state-ex.md">LOCK_STATE_EX</a> variable that tracks the state
     of the lock. This variable exists in the interval between the times that the caller obtains and releases
     the lock. The caller must use a different variable of type <b>LOCK_STATE_EX</b> for each attempt that it makes
     to obtain the lock from the same non-ISR driver thread.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A <b>ULONG</b> value that contains lock flags. Set this parameter to <b>NDIS_RWL_AT_DISPATCH_LEVEL</b> if the
     caller's current IRQL is <b>DISPATCH_LEVEL</b>. Otherwise, set this parameter to zero. For more information
     about dispatch IRQL tracking, see 
     <a href="NULL">Dispatch IRQL Tracking</a>.</p>
<div class="alert"><b>Note</b>  If the caller knows the current IRQL is <b>DISPATCH_LEVEL</b>, set this parameter to <b>NDIS_RWL_AT_DISPATCH_LEVEL</b>.  This flag makes the lock even more efficient by causing it to omit a check for the current IRQL.  If the current IRQL is unknown, do not test the current IRQL with <a href="..\wdm\nf-wdm-kegetcurrentirql.md">KeGetCurrentIrql</a> solely to determine whether to set this flag, as it is more efficient to allow the <b>NdisAcquireRWLockRead</b> function to test the IRQL itself.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>NDIS drivers call the 
    <b>NdisAcquireRWLockRead</b> function to obtain read-only access to resources that are shared between
    driver threads.</p>

<p>The driver must allocate a variable of type 
    <a href="..\ndis\ns-ndis--ndis-rw-lock-ex.md">NDIS_RW_LOCK_EX</a> with the 
    <a href="..\ndis\nf-ndis-ndisallocaterwlock.md">NdisAllocateRWLock</a> function before the
    driver calls the 
    <b>NdisAcquireRWLockRead</b> function.</p>

<p>After the driver calls 
    <a href="..\ndis\nf-ndis-ndisallocaterwlock.md">NdisAllocateRWLock</a>, it can call 
    <a href="..\ndis\nf-ndis-ndisacquirerwlockwrite.md">NdisAcquireRWLockWrite</a> or 
    <b>NdisAcquireRWLockRead</b> to obtain either write or read access to the resource. Only one non-ISR
    driver thread at a time can obtain write access to the resource. When one non-ISR thread has write
    access, all read and write accesses by other non-ISR threads must wait until the write-access holder
    releases the lock. However, if a non-ISR thread has read access, other non-ISR threads can concurrently
    obtain read access.</p>

<p>The <a href="..\ndis\ns-ndis--ndis-rw-lock-ex.md">NDIS_RW_LOCK_EX</a> lock does not support promotion from read to write.  Once a processor has acquired an <b>NDIS_RW_LOCK_EX</b> for read access (by calling <b>NdisAcquireRWLockRead</b>), the same processor must not attempt to acquire write access (by calling <a href="..\ndis\nf-ndis-ndisacquirerwlockwrite.md">NdisAcquireRWLockWrite</a>) until the previous read access is released.</p>

<p>An <a href="..\ndis\ns-ndis--ndis-rw-lock-ex.md">NDIS_RW_LOCK_EX</a> read lock  can be acquired recursively on the same processor.  For each call to <b>NdisAcquireRWLockRead</b>, there must be a corresponding call to <a href="..\ndis\nf-ndis-ndisreleaserwlock.md">NdisReleaseRWLock</a>.  The lock is only released after the last call to <b>NdisReleaseRWLock</b>.</p>

<p>The driver cannot use a lock to protect resources from read or write access that its other functions
    share with the 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> or 
    <a href="..\ndis\nc-ndis-miniport-disable-interrupt.md">
    MiniportDisableInterruptEx</a> function, or both. Instead, the driver must call 
    <a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
    NdisMSynchronizeWithInterruptEx</a> so that its 
    <a href="..\ndis\nc-ndis-miniport-synchronize-interrupt.md">
    MiniportSynchronizeInterrupt</a> function accesses such shared resources at the same DIRQL that its 
    <i>MiniportInterrupt</i> or 
    <i>
    MiniportDisableInterruptEx</i> functions, or both do.</p>

<p><b>NdisAcquireRWLockRead</b> always raises the IRQL to IRQL = <b>DISPATCH_LEVEL</b>.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--lock-state-ex.md">LOCK_STATE_EX</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-disable-interrupt.md">MiniportDisableInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-synchronize-interrupt.md">
   MiniportSynchronizeInterrupt</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-rw-lock-ex.md">NDIS_RW_LOCK_EX</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisacquirerwlockwrite.md">NdisAcquireRWLockWrite</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocaterwlock.md">NdisAllocateRWLock</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
   NdisMSynchronizeWithInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisreleaserwlock.md">NdisReleaseRWLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAcquireRWLockRead function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

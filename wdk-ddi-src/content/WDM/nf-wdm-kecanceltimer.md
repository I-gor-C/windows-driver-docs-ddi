---
UID: NF.wdm.KeCancelTimer
title: KeCancelTimer
author: windows-driver-content
description: The KeCancelTimer routine dequeues a timer object before the timer interval, if any was set, expires.
old-location: kernel\kecanceltimer.htm
ms.assetid: aefbf6d6-c107-4bf2-993d-d7ba8ea7ffcd
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
req.alt-api: KeCancelTimer
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeDispatchLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
ms.keywords: KeCancelTimer
req.iface: 
req.product: Windows 10 or later.
---

# KeCancelTimer function



## -description
<p>The <b>KeCancelTimer</b> routine dequeues a timer object before the timer interval, if any was set, expires.</p>


## -syntax

````
BOOLEAN KeCancelTimer(
  _Inout_ PKTIMER Timer
);
````


## -parameters
<dl>

### -param <i>Timer</i> [in, out]

<dd>
<p>Pointer to an initialized timer object, for which the caller provides the storage.</p>
</dd>
</dl>

## -returns
<p>If the specified timer object is in the system timer queue, <b>KeCancelTimer</b> returns <b>TRUE</b>.</p>

## -remarks
<p>If the timer object is currently in the system timer queue, it is removed from the queue. If a DPC object is associated with the timer, it too is canceled. Otherwise, no operation is performed.</p>

<p>The routine returns <b>TRUE</b> if the timer is still in the timer queue. A nonperiodic timer is removed from the system queue as soon as it expires. Thus, for nonperiodic timers, <b>KeCancelTimer</b> returns <b>FALSE</b> if the timer DPC has been queued. Periodic timers are always in the timer queue, so <b>KeCancelTimer</b> always returns <b>TRUE</b> for periodic timers. </p>

<p>Note that a DPC that is already running runs to completion. The driver must ensure that the DPC has completed before freeing any resources used by the DPC. For a nonperiodic timer, you can use synchronization primitives, such as event objects, to synchronize between the driver and the DPC. The driver can check the return code of <b>KeCancelTimer</b> to determine if the DPC is running. If so, the DPC can signal the event before exiting, and the driver can wait for that event to be reset to the not-signaled state.</p>

<p>Since for periodic timers <b>KeCancelTimer</b> always returns <b>TRUE</b>, drivers must use a different technique to wait until the DPC has completed. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552050">KeFlushQueuedDpcs</a> routine to block until the DPC executes.</p>

<p>Drivers do not need to synchronize for data stored in global variables or driver object extensions. The system automatically calls <b>KeFlushQueuedDpcs</b> before deallocating either of these regions.</p>

<p>For more information about timer objects, see <a href="https://msdn.microsoft.com/b58487de-6e9e-45f4-acb8-9233c8718ee2">Timer Objects and DPCs</a>.</p>

<p>If the timer object is currently in the system timer queue, it is removed from the queue. If a DPC object is associated with the timer, it too is canceled. Otherwise, no operation is performed.</p>

<p>The routine returns <b>TRUE</b> if the timer is still in the timer queue. A nonperiodic timer is removed from the system queue as soon as it expires. Thus, for nonperiodic timers, <b>KeCancelTimer</b> returns <b>FALSE</b> if the timer DPC has been queued. Periodic timers are always in the timer queue, so <b>KeCancelTimer</b> always returns <b>TRUE</b> for periodic timers. </p>

<p>Note that a DPC that is already running runs to completion. The driver must ensure that the DPC has completed before freeing any resources used by the DPC. For a nonperiodic timer, you can use synchronization primitives, such as event objects, to synchronize between the driver and the DPC. The driver can check the return code of <b>KeCancelTimer</b> to determine if the DPC is running. If so, the DPC can signal the event before exiting, and the driver can wait for that event to be reset to the not-signaled state.</p>

<p>Since for periodic timers <b>KeCancelTimer</b> always returns <b>TRUE</b>, drivers must use a different technique to wait until the DPC has completed. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552050">KeFlushQueuedDpcs</a> routine to block until the DPC executes.</p>

<p>Drivers do not need to synchronize for data stored in global variables or driver object extensions. The system automatically calls <b>KeFlushQueuedDpcs</b> before deallocating either of these regions.</p>

<p>For more information about timer objects, see <a href="https://msdn.microsoft.com/b58487de-6e9e-45f4-acb8-9233c8718ee2">Timer Objects and DPCs</a>.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547812">IrqlKeDispatchLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552168">KeInitializeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553099">KeReadStateTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeCancelTimer routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ntifs.KeRemoveQueue
title: KeRemoveQueue
author: windows-driver-content
description: The KeRemoveQueue routine gives the calling thread a pointer to a dequeued entry from the given queue object or allows the caller to wait, up to an optional timeout interval, on the queue object.
old-location: ifsk\keremovequeue.htm
ms.assetid: 475e352a-b6ea-4e37-ad46-e94284caa105
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRemoveQueue
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
ms.keywords: KeRemoveQueue
req.iface: 
---

# KeRemoveQueue function



## -description
<p>The <b>KeRemoveQueue</b> routine gives the calling thread a pointer to a dequeued entry from the given queue object or allows the caller to wait, up to an optional timeout interval, on the queue object. </p>


## -syntax

````
PLIST_ENTRY KeRemoveQueue(
  _Inout_  PRKQUEUE        Queue,
  _In_     KPROCESSOR_MODE WaitMode,
  _In_opt_ PLARGE_INTEGER  Timeout
);
````


## -parameters
<dl>

### -param <i>Queue</i> [in, out]

<dd>
<p>Pointer to an initialized queue object for which the caller provides resident storage in nonpaged pool.</p>
</dd>

### -param <i>WaitMode</i> [in]

<dd>
<p>The processor mode in which the caller is waiting, which can be either <b>KernelMode</b> or <b>UserMode</b>. If anything on its stack might be accessed at IRQL &gt;= DISPATCH_LEVEL, the caller must specify <b>KernelMode</b>. </p>
</dd>

### -param <i>Timeout</i> [in, optional]

<dd>
<p>Pointer to a variable that specifies the absolute or relative time, in units of 100 nanoseconds, at which the wait is to expire. If the value of <i>Timeout</i> is negative, the expiration time is relative to the current system time; otherwise, it is absolute. Absolute expiration times track any changes in system time; relative expiration times are not affected by system time changes. This pointer can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>KeRemoveQueue</b> returns one of the following:</p>

## -remarks
<p>Callers of <b>KeRemoveQueue</b> should test whether its return value is STATUS_TIMEOUT or STATUS_USER_APC before accessing any entry members. Testing the return value of <b>KeRemoveQueue</b> against <b>NULL</b> is a programming error. </p>

<p>Specifying a zero value for <i>*Timeout</i> indicates the caller's unwillingness to wait for an entry if the queue is currently empty. Specifying a <b>NULL</b><i>Timeout</i> pointer indicates the caller's willingness to wait indefinitely for an entry. </p>

<p>If the <i>WaitMode</i> parameter is <b>UserMode</b>, the kernel stack can be swapped out during the wait. Consequently, a caller must never attempt to pass parameters on the stack when calling <b>KeRemoveQueue</b> with <i>WaitMode</i> set to <b>UserMode</b>.</p>

<p>Specifying <i>WaitMode</i> as <b>KernelMode</b> in a call to <b>KeRemoveQueue</b> prevents the calling thread's kernel stack from being swapped out, as well as preventing the delivery of user-mode asynchronous procedure calls (APC). It does not prevent the delivery of kernel-mode APCs, such as those used by the I/O Manager to complete IRPs, when a thread calls <b>KeRemoveQueue</b> from IRQL PASSIVE_LEVEL. Delivery of such a kernel-mode APC does not prevent the calling thread from waiting on the queue object nor from being dispatched for execution with an entry after the kernel APC has run. </p>

<p>For more information about using driver-managed internal queues, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544165">Driver-Managed Queues</a>. </p>

<p>Callers of <b>KeRemoveQueue</b> should test whether its return value is STATUS_TIMEOUT or STATUS_USER_APC before accessing any entry members. Testing the return value of <b>KeRemoveQueue</b> against <b>NULL</b> is a programming error. </p>

<p>Specifying a zero value for <i>*Timeout</i> indicates the caller's unwillingness to wait for an entry if the queue is currently empty. Specifying a <b>NULL</b><i>Timeout</i> pointer indicates the caller's willingness to wait indefinitely for an entry. </p>

<p>If the <i>WaitMode</i> parameter is <b>UserMode</b>, the kernel stack can be swapped out during the wait. Consequently, a caller must never attempt to pass parameters on the stack when calling <b>KeRemoveQueue</b> with <i>WaitMode</i> set to <b>UserMode</b>.</p>

<p>Specifying <i>WaitMode</i> as <b>KernelMode</b> in a call to <b>KeRemoveQueue</b> prevents the calling thread's kernel stack from being swapped out, as well as preventing the delivery of user-mode asynchronous procedure calls (APC). It does not prevent the delivery of kernel-mode APCs, such as those used by the I/O Manager to complete IRPs, when a thread calls <b>KeRemoveQueue</b> from IRQL PASSIVE_LEVEL. Delivery of such a kernel-mode APC does not prevent the calling thread from waiting on the queue object nor from being dispatched for execution with an entry after the kernel APC has run. </p>

<p>For more information about using driver-managed internal queues, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544165">Driver-Managed Queues</a>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549559">KeInsertHeadQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549570">KeInsertQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20KeRemoveQueue routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wdm.KeReleaseMutex
title: KeReleaseMutex
author: windows-driver-content
description: The KeReleaseMutex routine releases a mutex object, and specifies whether the caller is to call one of the KeWaitXxx routines as soon as KeReleaseMutex returns control.
old-location: kernel\kereleasemutex.htm
old-project: kernel
ms.assetid: d220f913-6111-435d-b617-257edf2a9c68
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeReleaseMutex
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
req.alt-api: KeReleaseMutex
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
req.iface: 
req.product: Windows 10 or later.
---

# KeReleaseMutex function



## -description
<p>The <b>KeReleaseMutex</b> routine releases a mutex object, and specifies whether the caller is to call one of the <b>KeWait<i>Xxx</i></b> routines as soon as <b>KeReleaseMutex</b> returns control. </p>


## -syntax

````
LONG KeReleaseMutex(
  _Inout_ PRKMUTEX Mutex,
  _In_    BOOLEAN  Wait
);
````


## -parameters
<dl>

### -param <i>Mutex</i> [in, out]

<dd>
<p>A pointer to an initialized mutex object for which the caller provides the storage.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Specifies whether the call to <b>KeReleaseMutex</b> is to be immediately followed by a call to one of the <b>KeWait<i>Xxx</i></b> routines. If <b>TRUE</b>, the <b>KeReleaseMutex</b> call must be followed by a call to <a href="..\wdm\nf-wdm-kewaitformultipleobjects.md">KeWaitForMultipleObjects</a>, <a href="kernel.kewaitformutexobject">KeWaitForMutexObject</a>, or <a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>. For more information, see the following Remarks section. </p>
</dd>
</dl>

## -returns
<p>If the return value is zero, the mutex object was released and attained a state of <i>signaled</i>.</p>

## -remarks
<p>For better performance, use fast mutexes or guarded mutexes. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540595">Alternatives to Mutex Objects</a>.</p>

<p>If the mutex object attains a signaled state, an attempt is made to satisfy a wait for the mutex object.</p>

<p>A mutex object can be released only by the thread that currently holds the mutex. If an attempt is made to release a mutex that the thread does not hold or if a mutex was acquired at IRQL = DISPATCH_LEVEL and the thread is not running at DISPATCH_LEVEL (and vice versa), the routine raises a STATUS_ABANDONED or STATUS_MUTEX_NOT_OWNED exception.</p>

<p>When a mutex object attains a signaled state, it is removed from the list of the mutexes that are held by that thread. If this list contains no more entries, the original priority for the thread is restored.</p>

<p>The <b>KeReleaseMutex</b> routine might temporarily raise the IRQL. If the <i>Wait</i> parameter is <b>FALSE</b>, the routine, before it returns, restores the IRQL to the original value that it had at the start of the call.</p>

<p>If <i>Wait</i> = <b>TRUE</b>, the routine returns without lowering the IRQL. In this case, the <b>KeReleaseMutex</b> call must be immediately followed by a <b>KeWait<i>Xxx</i></b> call. By setting <i>Wait</i> = <b>TRUE</b>, the caller can prevent an unnecessary context switch from occurring between the <b>KeReleaseMutex</b> call and the <b>KeWait<i>Xxx</i></b> call. The <b>KeWait<i>Xxx</i></b> routine, before it returns, restores the IRQL to its original value at the start of the <b>KeReleaseMutex</b> call. Although the IRQL disables context switches between the two calls, these calls cannot reliably be used as the start and end of an atomic operation. For example, between these two calls, a thread that is running at the same time on another processor might change the state of the event object or of the target of the wait.</p>

<p>If the caller is executing at IRQL = DISPATCH_LEVEL or in an arbitrary thread context, the <i>Timeout</i> parameter to <b>KeWait<i>Xxx</i></b> must be zero.</p>

<p>If a mutex is acquired recursively, the holding thread must call <b>KeReleaseMutex</b> as many times as it acquired the mutex to set it to the signaled state.</p>

<p>For more information about mutex objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556417">Mutex Objects</a>.</p>

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
<a href="devtest.wdm_irqlkedispatchlte">IrqlKeDispatchLte</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exreleasefastmutex">ExReleaseFastMutex</a>
</dt>
<dt>
<a href="kernel.exreleasefastmutexunsafe">ExReleaseFastMutexUnsafe</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializemutex.md">KeInitializeMutex</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kereadstatemutex.md">KeReadStateMutex</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitformultipleobjects.md">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="kernel.kewaitformutexobject">KeWaitForMutexObject</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeReleaseMutex routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

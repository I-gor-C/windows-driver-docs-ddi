---
UID: NF.wdm.KeSetTimer
title: KeSetTimer
author: windows-driver-content
description: The KeSetTimer routine sets the absolute or relative interval at which a timer object is to be set to a signaled state and, optionally, supplies a CustomTimerDpc routine to be executed when that interval expires.
old-location: kernel\kesettimer.htm
old-project: kernel
ms.assetid: 81a205cd-a641-4f85-a217-7febf203b62d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeSetTimer
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
req.alt-api: KeSetTimer
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

# KeSetTimer function



## -description
<p>The <b>KeSetTimer</b> routine sets the absolute or relative interval at which a timer object is to be set to a signaled state and, optionally, supplies a <a href="kernel.customtimerdpc">CustomTimerDpc</a> routine to be executed when that interval expires. </p>


## -syntax

````
BOOLEAN KeSetTimer(
  _Inout_  PKTIMER       Timer,
  _In_     LARGE_INTEGER DueTime,
  _In_opt_ PKDPC         Dpc
);
````


## -parameters
<dl>

### -param Timer [in, out]

<dd>
<p>Pointer to a timer object that was initialized with <a href="..\wdm\nf-wdm-keinitializetimer.md">KeInitializeTimer</a> or <a href="..\wdm\nf-wdm-keinitializetimerex.md">KeInitializeTimerEx</a>.</p>
</dd>

### -param DueTime [in]

<dd>
<p>Specifies the absolute or relative time at which the timer is to expire. If the value of the <i>DueTime</i> parameter is negative, the expiration time is relative to the current system time. Otherwise, the expiration time is absolute. The expiration time is expressed in system time units (100-nanosecond intervals). Absolute expiration times track any changes in the system time; relative expiration times are not affected by system time changes.</p>
</dd>

### -param Dpc [in, optional]

<dd>
<p>Pointer to a DPC object that was initialized by <a href="..\wdm\nf-wdm-keinitializedpc.md">KeInitializeDpc</a>. This parameter is optional. </p>
</dd>
</dl>

## -returns
<p>If the timer object was already in the system timer queue, <b>KeSetTimer</b> returns <b>TRUE</b>.</p>

## -remarks
<p>The <b>KeSetTimer</b> routine does the following:</p>

<p>Computes the expiration time.</p>

<p>Sets the timer to a not-signaled state.</p>

<p>Inserts the timer object in the system timer queue.</p>

<p>If the timer object was already in the timer queue, it is implicitly canceled before being set to the new expiration time. A call to <b>KeSetTimer</b> before the previously specified <i>DueTime</i> has expired cancels both the timer and the call to the <i>Dpc</i>, if any, associated with the previous call.</p>

<p>If the <i>Dpc</i> parameter is specified, a DPC object is associated with the timer object. When the timer expires, the timer object is removed from the system timer queue and its state is set to signaled. If a DPC object was associated with the timer when it was set, the DPC object is inserted in the system DPC queue to be executed as soon as conditions permit after the timer interval expires.</p>

<p>Expiration times are measured relative to the system clock, and the accuracy with which the operating system can detect when a timer expires is limited by the granularity of the system clock. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj602805">Timer Accuracy</a>.</p>

<p>Only one instantiation of a given DPC object can be queued at any given moment. To avoid potential race conditions, the DPC passed to <b>KeSetTimer</b> should <u>not</u> be passed to <a href="..\wdm\nf-wdm-keinsertqueuedpc.md">KeInsertQueueDpc</a>.</p>

<p>Drivers must cancel any active timers in their <a href="kernel.unload">Unload</a> routines. Use <a href="..\wdm\nf-wdm-kecanceltimer.md">KeCancelTimer</a> to cancel any timers.</p>

<p>Callers of <b>KeSetTimer</b> can specify one expiration time for a timer. To set a recurring timer use <a href="..\wdm\nf-wdm-kesettimerex.md">KeSetTimerEx</a>.</p>

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
<a href="devtest.wdm_irqlkedispatchlte">IrqlKeDispatchLte</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-kecanceltimer.md">KeCancelTimer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializedpc.md">KeInitializeDpc</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializetimer.md">KeInitializeTimer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializetimerex.md">KeInitializeTimerEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kereadstatetimer.md">KeReadStateTimer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kesettimerex.md">KeSetTimerEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitformultipleobjects.md">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSetTimer routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

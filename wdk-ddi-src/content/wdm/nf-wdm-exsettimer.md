---
UID: NF.wdm.ExSetTimer
title: ExSetTimer
author: windows-driver-content
description: The ExSetTimer routine starts a timer operation and sets the timer to expire at the specified due time.
old-location: kernel\exsettimer.htm
old-project: kernel
ms.assetid: 0320AB36-CA88-40E7-859E-B940401474DD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExSetTimer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExSetTimer
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExSetTimer function



## -description
<p>The <b>ExSetTimer</b> routine starts a timer operation and sets the timer to expire at the specified due time.</p>


## -syntax

````
BOOLEAN ExSetTimer(
  _In_     PEX_TIMER           Timer,
  _In_     LONGLONG            DueTime,
  _In_     LONGLONG            Period,
  _In_opt_ PEXT_SET_PARAMETERS Parameters
);
````


## -parameters
<dl>

### -param <i>Timer</i> [in]

<dd>
<p>A pointer to an <a href="kernel.ex_timer">EX_TIMER</a> structure. This structure is a timer object that was previously allocated by the <a href="..\wdm\nf-wdm-exallocatetimer.md">ExAllocateTimer</a> routine.</p>
</dd>

### -param <i>DueTime</i> [in]

<dd>
<p>The absolute or relative time at which the timer is to expire. If the value of the <i>DueTime</i> parameter is negative, the expiration time is relative to the current system time. Otherwise, the expiration time is absolute. The expiration time is expressed in system time units (100-nanosecond intervals). Absolute expiration times track any changes in the system time; relative expiration times are not affected by system time changes. An absolute time is expressed as the amount of time passed, in system time units, since the start of the year 1601.</p>
<p>The <i>DueTime</i> parameter for a <a href="https://msdn.microsoft.com/B8F2B28C-A02B-4015-B392-3D30BC0229B8">high-resolution timer</a> must be a relative time (negative value), or the routine bug checks.</p>
</dd>

### -param <i>Period</i> [in]

<dd>
<p>An optional period for the timer in system time units (100-nanosecond intervals). Must be less than or equal to MAXLONG. For a timer that is one-shot instead of periodic, set <i>Period</i> to zero.</p>
</dd>

### -param <i>Parameters</i> [in, optional]

<dd>
<p>A pointer to an <a href="kernel.ext_set_parameters">EXT_SET_PARAMETERS</a> structure. The calling driver previously called the <a href="..\wdm\nf-wdm-exinitializesettimerparameters.md">ExInitializeSetTimerParameters</a> routine to initialize this structure.</p>
</dd>
</dl>

## -returns
<p>This routine returns <b>TRUE</b> if it cancels a timer that was pending at the time that the routine was called. Otherwise, the routine returns <b>FALSE</b>. For more information, see Remarks.</p>

## -remarks
<p>Your driver can call this routine to set a timer to expire at a future time. The driver can then wait for the timer to expire. Or, the driver can implement a callback routine that is called when the timer expires.</p>

<p>After a driver calls <b>ExSetTimer</b>, the driver can call a routine such as <a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a> or or <a href="..\wdm\nf-wdm-kewaitformultipleobjects.md">KeWaitForMultipleObjects</a> to wait for the timer to expire. When the timer expires, the operating system signals the timer object.</p>

<p>As an option, the driver can implement an <a href="kernel.extimercallback">ExTimerCallback</a> callback routine, and supply a pointer to this routine as an input parameter to the <a href="..\wdm\nf-wdm-exallocatetimer.md">ExAllocateTimer</a> routine. When the timer expires, the operating system calls the <i>ExTimerCallback</i> routine.</p>

<p>An <b>ExSetTimer</b> call implicitly cancels any previously started set-timer operation on the timer object specified by <i>Timer</i>. If your driver previously called <b>ExSetTimer</b> to set a timer that uses <i>Timer</i>, and this timer has not yet expired when <b>ExSetTimer</b> is called a second time, the second call cancels the timer from the first call and then starts the new timer. In this case, the second call returns <b>TRUE</b>. However, if the timer started by the first call expires before the second call can cancel this timer, the second call starts the new timer and returns <b>FALSE</b>.</p>

<p>If the <i>Period</i> parameter is nonzero, the timer is periodic. For a periodic timer, the <i>DueTime</i> parameter specifies the time of the initial timer expiration, and <i>Period</i> specifies the interval between subsequent expirations.</p>

<p>The hardware timer used for the system clock signals interrupt requests at uniform intervals, but the handling of these interrupts might be delayed by interrupt processing for other devices. Thus, for a periodic timer, the delay from a periodic expiration time to the time at which the timer object is signaled or the <i>ExTimerCallback</i> routine runs might vary from one period to the next. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj602805">Timer Accuracy</a>.</p>

<p>A periodic timer can expire no more than once per system clock tick. Setting the period of a timer to a value smaller than the interval between system clock ticks does not cause the timer to expire more than once per system clock tick, but might cause the intervals between successive expirations to vary if the system clock rate changes. For example, the operating system might temporarily increase the system clock rate to meet the timing requirements of a high-resolution timer. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265247">High-Resolution Timers</a>.</p>

<p>For a periodic timer that is not a high-resolution timer, a driver can achieve relatively uniform periodic expirations by setting <i>Period</i> to an integer multiple of the default interval between system clock ticks.</p>

<p>To avoid excessive power consumption, a driver should not set the period of a long-running high-resolution timer to a value less than the default interval between system clock ticks. Otherwise, the system clock timer will continuously generate interrupts at the maximum allowed system clock rate.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265198">ExXxxTimer Routines and EX_TIMER Objects</a>.</p>

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
<p>Available starting with Windows 8.1.</p>
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
<dt>Ntoskrnl.lib</dt>
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
<a href="..\wdm\nf-wdm-exallocatetimer.md">ExAllocateTimer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinitializesettimerparameters.md">ExInitializeSetTimerParameters</a>
</dt>
<dt>
<a href="kernel.ex_timer">EX_TIMER</a>
</dt>
<dt>
<a href="kernel.extimercallback">ExTimerCallback</a>
</dt>
<dt>
<a href="kernel.ext_set_parameters">EXT_SET_PARAMETERS</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExSetTimer routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

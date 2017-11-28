---
UID: NF.wdftimer.WdfTimerStart
title: WdfTimerStart
author: windows-driver-content
description: The WdfTimerStart method starts a timer's clock.
old-location: wdf\wdftimerstart.htm
old-project: wdf
ms.assetid: 32c40be2-dee0-4ac7-9f78-a64b9f985f51
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfTimerStart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdftimer.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfTimerStart
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfTimerStart function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfTimerStart</b> method starts a timer's clock.</p>


## -syntax

````
BOOLEAN WdfTimerStart(
  _In_ WDFTIMER Timer,
  _In_ LONGLONG DueTime
);
````


## -parameters
<dl>

### -param <i>Timer</i> [in]

<dd>
<p>A handle to a framework timer object that was obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a>.</p>
</dd>

### -param <i>DueTime</i> [in]

<dd>
<p>A time period, in system time units (100-nanosecond intervals). The framework calls the driver's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function when the specified time period elapses. The time period value can be negative or positive as follows:
<ul>
<li>
<p>If the value is negative, the time period is relative to the current system time.</p>
</li>
<li>If the value is positive, the time period specifies an absolute time (which is actually relative to January 1, 1601).</li>
</ul>
</p>
<div class="alert"><b>Warning</b>  If you set the <b>UseHighResolutionTimer</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552519">WDF_TIMER_CONFIG</a> to <b>WdfTrue</b>, you must call <b>WdfTimerStart</b> with the <i>DueTime</i> parameter set to a negative value.  Otherwise, the call causes the system to crash.</div>
<div> </div>
<p>Relative times are not affected by any changes to the system time that might occur within the specified time period. Absolute times do reflect system time changes.</p>
<p>The framework provides <a href="wdf.wdf_timer_object_reference">time conversion functions</a> that convert time values into system time units.



</p>
</dd>
</dl>

## -returns
<p><b>WdfTimerStart</b> returns <b>TRUE</b> if the timer object was in the system's timer queue. Otherwise, this method returns <b>FALSE</b>. For more information, see the following Remarks section. </p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>After a driver calls <b>WdfTimerStart</b>, the framework calls the driver's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function when the time that is specified for the <i>DueTime</i> parameter elapses. After this first call, the framework calls the callback function each time that the time period that is specified by the <b>Period</b> member of the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552519">WDF_TIMER_CONFIG</a> structure elapses. </p>

<p>The expiration of the timer ultimately depends on the granularity of the system clock. The value specified for <i>DueTime</i> guarantees that the framework calls the driver's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function on or after the given <i>DueTime</i>. However, <b>WdfTimerStart</b> cannot override the granularity of the system clock, whatever the value specified for <i>DueTime</i>. </p>

<p>When a driver calls <b>WdfTimerStart</b>, its timer object is added to the system's queue of timer objects. If the timer is not a periodic timer, the system removes the timer object from the queue after the timer's "due time" has elapsed. If the timer is a periodic timer, the timer object remains in the queue until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550056">WdfTimerStop</a>.</p>

<p>A driver might call <b>WdfTimerStart</b> from its <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function in order to restart a non-periodic timer after it expires.</p>

<p><b>WdfTimerStart</b> returns <b>TRUE</b> if the driver has previously called <b>WdfTimerStart</b> and the timer object is still in the system's queue because the time period has not elapsed (or because it is a periodic timer). Before <b>WdfTimerStart</b> returns <b>TRUE</b>, the operating system resets the time period to the value that the driver specified in the new call to <b>WdfTimerStart</b>. The framework calls the <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function only after the new time period elapses.</p>

<p>To stop the timer's clock, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550056">WdfTimerStop</a>.</p>

<p>For more information about framework timer objects, see <a href="wdf.using_timers">Using Timers</a>.</p>

<p>The following code example starts a timer. The framework will call the timer's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function after 10 milliseconds. </p>

<p>After a driver calls <b>WdfTimerStart</b>, the framework calls the driver's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function when the time that is specified for the <i>DueTime</i> parameter elapses. After this first call, the framework calls the callback function each time that the time period that is specified by the <b>Period</b> member of the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552519">WDF_TIMER_CONFIG</a> structure elapses. </p>

<p>The expiration of the timer ultimately depends on the granularity of the system clock. The value specified for <i>DueTime</i> guarantees that the framework calls the driver's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function on or after the given <i>DueTime</i>. However, <b>WdfTimerStart</b> cannot override the granularity of the system clock, whatever the value specified for <i>DueTime</i>. </p>

<p>When a driver calls <b>WdfTimerStart</b>, its timer object is added to the system's queue of timer objects. If the timer is not a periodic timer, the system removes the timer object from the queue after the timer's "due time" has elapsed. If the timer is a periodic timer, the timer object remains in the queue until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550056">WdfTimerStop</a>.</p>

<p>A driver might call <b>WdfTimerStart</b> from its <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function in order to restart a non-periodic timer after it expires.</p>

<p><b>WdfTimerStart</b> returns <b>TRUE</b> if the driver has previously called <b>WdfTimerStart</b> and the timer object is still in the system's queue because the time period has not elapsed (or because it is a periodic timer). Before <b>WdfTimerStart</b> returns <b>TRUE</b>, the operating system resets the time period to the value that the driver specified in the new call to <b>WdfTimerStart</b>. The framework calls the <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function only after the new time period elapses.</p>

<p>To stop the timer's clock, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550056">WdfTimerStop</a>.</p>

<p>For more information about framework timer objects, see <a href="wdf.using_timers">Using Timers</a>.</p>

<p>The following code example starts a timer. The framework will call the timer's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function after 10 milliseconds. </p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdftimer.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evttimerfunc">EvtTimerFunc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552519">WDF_TIMER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550056">WdfTimerStop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfTimerStart method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

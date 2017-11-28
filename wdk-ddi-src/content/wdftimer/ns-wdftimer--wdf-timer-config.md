---
UID: NS.wdftimer._WDF_TIMER_CONFIG
title: WDF_TIMER_CONFIG
author: windows-driver-content
description: The WDF_TIMER_CONFIG structure contains configuration information for a framework timer object.
old-location: wdf\wdf_timer_config.htm
old-project: wdf
ms.assetid: 5ef6491d-90bb-472c-821a-b296bef17463
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_TIMER_CONFIG, WDF_TIMER_CONFIG, *PWDF_TIMER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdftimer.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_TIMER_CONFIG
req.alt-loc: wdftimer.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# WDF_TIMER_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_TIMER_CONFIG</b> structure contains configuration information for a framework timer object.</p>


## -syntax

````
typedef struct _WDF_TIMER_CONFIG {
  ULONG         Size;
  PFN_WDF_TIMER EvtTimerFunc;
  ULONG         Period;
  BOOLEAN       AutomaticSerialization;
  ULONG         TolerableDelay;
  WDF_TRI_STATE UseHighResolutionTimer;
} WDF_TIMER_CONFIG, *PWDF_TIMER_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtTimerFunc</b>

<dd>
<p>A pointer to a driver-supplied <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>Period</b>

<dd>
<p>A time period, in milliseconds. The framework calls the driver's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function repeatedly, whenever the specified number of milliseconds elapses. If this value is zero, the framework does not call the driver's <i>EvtTimerFunc</i> callback function repeatedly. Instead, it calls the callback function once, after the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550054">WdfTimerStart</a> method's <i>DueTime</i> has elapsed. (The time period must be zero if <a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a> sets the execution level to <a href="..\wdfobject\ne-wdfobject--wdf-execution-level.md">WdfExecutionLevelPassive</a>.) The time period cannot be a negative value.</p>
</dd>

### -field <b>AutomaticSerialization</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the framework will synchronize execution of the timer object's <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function with callback functions from other objects that are underneath the timer's parent device object. For more information, see the following Remarks section. If <b>FALSE</b>, the framework does not synchronize execution of the <i>EvtTimerFunc</i> callback function.</p>
</dd>

### -field <b>TolerableDelay</b>

<dd>
<p>Specifies a tolerance, in milliseconds, for the timer period that <i>Period</i> specifies and for the initial time interval that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550054">WdfTimerStart</a> method's <i>DueTime</i> specifies. For a periodic timer, the time interval between two successive timer expirations will be in the range from (<i>Period</i> - <i>TolerableDelay</i>) to (<i>Period</i> + <i>TolerableDelay</i>). The initial expiration time will be in the range from <i>DueTime</i> to (<i>DueTime</i> + <i>TolerableDelay</i>). The <i>TolerableDelay</i> value cannot be negative.</p>
<p> The <b>TolerableDelay</b> member is available in version 1.9 and later versions of KMDF.</p>
<p> Starting in Windows 8.1, in a driver using at minimum KMDF 1.13 or UMDF 2.0, you can set this member to <b>TolerableDelayUnlimited</b> to specify that the system should not be woken up as a result of this timer's expiration.</p>
<p>If  <b>UseHighResolutionTimer</b> is <b>WdfTrue</b>, you must set <b>TolerableDelay</b> to zero. Otherwise, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a> returns a failure code.</p>
<p>For more information about this member, see the following Remarks section.</p>
</dd>

### -field <b>UseHighResolutionTimer</b>

<dd>
<p><b>KMDF only</b></p>
<p>This member is available starting with Windows 8.1 and KMDF version 1.13.</p>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value. If this value is <b>WdfTrue</b>, the framework uses a high resolution timer that has an accuracy of one millisecond.  If the value is <b>WdfFalse</b> or <b>WdfDefault</b>, the framework uses a standard timer that has an accuracy matching the system clock tick interval, which is by default 15.6 milliseconds.</p>
<div class="alert"><b>Warning</b>  If you set <b>UseHighResolutionTimer</b> to <b>WdfTrue</b>, you must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550054">WdfTimerStart</a> with the <i>DueTime</i> parameter set to a negative value.  Otherwise, the call causes the system to crash.</div>
<div> </div>
<p>If  <b>UseHighResolutionTimer</b> is <b>WdfTrue</b>, you must set <b>TolerableDelay</b> to zero. Otherwise, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a> returns a failure code.</p>
<p>
             For more information about this member, see the following Remarks section.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_TIMER_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a> method. To initialize a <b>WDF_TIMER_CONFIG</b> structure, your driver must call either <a href="https://msdn.microsoft.com/library/windows/hardware/ff552522">WDF_TIMER_CONFIG_INIT</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552526">WDF_TIMER_CONFIG_INIT_PERIODIC</a>.</p>

<p>Setting the <b>AutomaticSerialization</b> member of <b>WDF_TIMER_CONFIG</b> to <b>TRUE</b> has no effect if the parent object's <a href="..\wdfobject\ne-wdfobject--wdf-synchronization-scope.md">synchronization scope</a> is set to <b>WdfSynchronizationScopeNone</b>.</p>

<p>If the parent device object's execution level is <b>WdfExecutionLevelPassive</b>, you can set the <b>AutomaticSerialization</b> member to <b>TRUE</b> only if the timer object represents a <a href="wdf.using_timers">passive-level timer</a>.</p>

<p>If a driver uses the <b>TolerableDelay</b> member, the operating system can group together expiration times that are close together and process them all at once. If the operating system can handle the expirations of multiple timers at once, it can potentially keep the computer in a low-power state for longer periods of time to increase battery life.</p>

<p>If the  <b>TolerableDelay</b> member is <b>TolerableDelayUnlimited</b>, the system will not return to its fully on (S0) state to service the timer if it is in a low-power (S<i>x</i>) state when the timer expires. A driver can specify <b>TolerableDelayUnlimited</b> to increase battery life when the timer is related to a non-critical periodic operation.</p>

<p>Setting <b>UseHighResolutionTimer</b> to <b>WdfTrue</b> may result in decreased battery life.</p>

<p>For more information about <b>AutomaticSerialization</b> and synchronizing driver callback functions, see <a href="wdf.synchronization_techniques_for_wdf_drivers">Synchronization Techniques for Framework-Based Drivers</a>.</p>

<p>For more information about framework timer objects, see <a href="wdf.using_timers">Using Timers</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evttimerfunc">EvtTimerFunc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552522">WDF_TIMER_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552526">WDF_TIMER_CONFIG_INIT_PERIODIC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550050">WdfTimerCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550054">WdfTimerStart</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_TIMER_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

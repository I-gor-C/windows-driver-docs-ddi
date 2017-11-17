---
UID: NF.ndis.NdisSetTimerObject
title: NdisSetTimerObject
author: windows-driver-content
description: The NdisSetTimerObject function sets a timer object to fire after a specified interval or periodically.
old-location: netvista\ndissettimerobject.htm
ms.assetid: 75f8fa1b-5b79-4bc2-8b7b-aa1101c9c331
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisSetTimerObject
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Timer_Function, PeriodicTimer
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisSetTimerObject
req.iface: 
---

# NdisSetTimerObject function



## -description
<p>The 
  <b>NdisSetTimerObject</b> function sets a timer object to fire after a specified interval or
  periodically.</p>


## -syntax

````
BOOLEAN NdisSetTimerObject(
  _In_     NDIS_HANDLE   TimerObject,
  _In_     LARGE_INTEGER DueTime,
  _In_opt_ LONG          MillisecondsPeriod,
  _In_opt_ PVOID         FunctionContext
);
````


## -parameters
<dl>

### -param <i>TimerObject</i> [in]

<dd>
<p>A handle to a timer object that NDIS provides when a driver calls the 
     <a href="https://msdn.microsoft.com/feb5e4cf-7e23-434e-9dc5-bb445a6f5606">
     NdisAllocateTimerObject</a> function.</p>
</dd>

### -param <i>DueTime</i> [in]

<dd>
<p>The absolute or relative time at which the timer is to expire. If the value of the 
     <i>DueTime</i> parameter is negative, the expiration time is relative to the current system time.
     Otherwise, the expiration time is absolute. The expiration time is expressed in system time units
     (100-nanosecond intervals). Absolute expiration times track any changes in the system time; relative
     expiration times are not affected by system time changes.</p>
</dd>

### -param <i>MillisecondsPeriod</i> [in, optional]

<dd>
<p>The periodic time interval, in milliseconds, that elapses between each time the timer fires and
     the next call to the 
     <i>NetTimerCallback</i> function, unless the timer is canceled. The value of this parameter must be less
     than or equal to MAXLONG.</p>
</dd>

### -param <i>FunctionContext</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied context area that NDIS passes to the associated 
     <i>NetTimerCallback</i> function when a timer fires. If this parameter is <b>NULL</b>, NDIS uses the default
     value that is specified in the 
     <a href="https://msdn.microsoft.com/9a62e94c-f635-4ab7-b439-b98c60ba2854">
     NDIS_TIMER_CHARACTERISTICS</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>NdisSetTimerObject</b> returns <b>TRUE</b> if the timer object was already in the system timer queue;
     otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>After a driver calls 
    <b>NdisSetTimerObject</b>, the timer object is queued until the interval that is specified in the 
    <i>DueTime</i> parameter expires. After the interval expires, the timer object is dequeued and the
    caller-supplied 
    <a href="https://msdn.microsoft.com/76e59376-58a4-4e35-bac4-ec5938c88cd7">NetTimerCallback</a> function is run once
    at IRQL = DISPATCH_LEVEL as soon as a processor becomes available.</p>

<p>If a nonzero value is specified in the 
    <i>MillisecondsPeriod</i> parameter, the timer object is queued again until the interval that is specified
    in 
    <i>MillisecondsPeriod</i> expires. After this interval expires, the timer object is requeued and the
    caller-supplied 
    <i>NetTimerCallback</i> function is run once at IRQL = DISPATCH_LEVEL as soon as a processor becomes
    available.</p>

<p>For more information about timer behavior, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>.</p>

<p>To cancel a timer, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a> function.</p>

<p>After a driver calls 
    <b>NdisSetTimerObject</b>, the timer object is queued until the interval that is specified in the 
    <i>DueTime</i> parameter expires. After the interval expires, the timer object is dequeued and the
    caller-supplied 
    <a href="https://msdn.microsoft.com/76e59376-58a4-4e35-bac4-ec5938c88cd7">NetTimerCallback</a> function is run once
    at IRQL = DISPATCH_LEVEL as soon as a processor becomes available.</p>

<p>If a nonzero value is specified in the 
    <i>MillisecondsPeriod</i> parameter, the timer object is queued again until the interval that is specified
    in 
    <i>MillisecondsPeriod</i> expires. After this interval expires, the timer object is requeued and the
    caller-supplied 
    <i>NetTimerCallback</i> function is run once at IRQL = DISPATCH_LEVEL as soon as a processor becomes
    available.</p>

<p>For more information about timer behavior, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>.</p>

<p>To cancel a timer, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a> function.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548019">Irql_Timer_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550378">PeriodicTimer</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567886">NDIS_TIMER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f6f50bba-cda5-41ed-9e0b-1aea5113a22b">
   NdisSetCoalescableTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/76e59376-58a4-4e35-bac4-ec5938c88cd7">NetTimerCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSetTimerObject function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

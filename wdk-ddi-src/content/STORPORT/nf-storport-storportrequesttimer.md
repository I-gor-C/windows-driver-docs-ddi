---
UID: NF.storport.StorPortRequestTimer
title: StorPortRequestTimer
author: windows-driver-content
description: Schedules a callback event for a Storport timer context object.
old-location: storage\storportrequesttimer.htm
ms.assetid: EE5A6D39-EC76-4D97-B2EC-4A43225C2FB5
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortRequestTimer
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any
ms.keywords: StorPortRequestTimer
req.iface: 
req.product: Windows 10 or later.
---

# StorPortRequestTimer function



## -description
<p>Schedules a callback event for a Storport timer context object.</p>


## -syntax

````
ULONG StorPortRequestTimer(
  _In_     PVOID        HwDeviceExtension,
  _In_     PVOID        TimerHandle,
  _In_     PHW_TIMER_EX TimerCallback,
  _In_opt_ PVOID        CallbackContext,
  _In_     LONGLONG     TimerValue,
  _In_     LONGLONG     TolerableDelay
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>TimerHandle</i> [in]

<dd>
<p>A pointer to an opaque buffer for the timer context returned by <a href="https://msdn.microsoft.com/library/windows/hardware/hh451483">StorPortInitializeTimer</a>.</p>
</dd>

### -param <i>TimerCallback</i> [in]

<dd>
<p>A pointer to a timer callback routine supplied by the miniport. The following is the prototype defined for <b>PHW_TIMER_EX</b>:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
VOID
(*PHW_TIMER_EX) (
  _In_ PVOID  DeviceExtension,
  _In_opt_ PVOID Context
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -param <i>CallbackContext</i> [in, optional]

<dd>
<p>A pointer to a miniport provided context for the timer callback.</p>
</dd>

### -param <i>TimerValue</i> [in]

<dd>
<p>The timeout value for the timer, in microseconds. Setting <i>TimerValue</i> to 0 will cancel the timer.</p>
</dd>

### -param <i>TolerableDelay</i> [in]

<dd>
<p>The allowable delay for the timer in microseconds. Values less than 32 microseconds are ignored and <i>TolerableDelay</i> defaults to 0.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortRequestTimer</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Not enough resources available to defer scheduling of the timer.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p><i>HwDeviceExtension</i>, <i>TimerHandle</i>, or <i>TimerCallback</i> is NULL.</p>

<p>The timer context object, <i>TimerHandle</i>, is invalid.</p><dl>
<dt><b>STOR_STATUS_BUSY</b></dt>
</dl><p>A previous timer request is active. <i>TimerValue</i> &gt; 0 and <i>TimerCallback</i> has not been called.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The timer request was successfully scheduled.</p>

<p> </p>

## -remarks
<p>The <b>StorPortRequestTimer</b> routine is callable at any IRQL. However, if the routine is called when IRQL &gt; DISPATCH_LEVEL, the timer's scheduling is deferred until IRQL &lt;= DISPATCH_LEVEL.</p>

<p>The <b>StorPortRequestTimer</b> routine is callable at any IRQL. However, if the routine is called when IRQL &gt; DISPATCH_LEVEL, the timer's scheduling is deferred until IRQL &lt;= DISPATCH_LEVEL.</p>

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
<p>Available in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557426">HwStorTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451476">StorPortFreeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451483">StorPortInitializeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortRequestTimer routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

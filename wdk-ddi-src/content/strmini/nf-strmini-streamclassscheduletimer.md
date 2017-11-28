---
UID: NF.strmini.StreamClassScheduleTimer
title: StreamClassScheduleTimer
author: windows-driver-content
description: The minidriver calls the StreamClassScheduleTimer routine to schedule a timer, and to specify a routine that is called when the timer expires.
old-location: stream\streamclassscheduletimer.htm
old-project: stream
ms.assetid: 83271c19-911b-481a-bc25-c0b3816cf800
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: StreamClassScheduleTimer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassScheduleTimer
req.alt-loc: Stream.lib,Stream.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Stream.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassScheduleTimer function



## -description
<p>The minidriver calls the <b>StreamClassScheduleTimer</b> routine to schedule a timer, and to specify a routine that is called when the timer expires.</p>


## -syntax

````
VOID StreamClassScheduleTimer(
  _In_opt_ PHW_STREAM_OBJECT StreamObject,
  _In_     PVOID             HwDeviceExtension,
  _In_     ULONG             NumberOfMicroseconds,
  _In_     PHW_TIMER_ROUTINE TimerRoutine,
  _In_     PVOID             Context
);
````


## -parameters
<dl>

### -param <i>StreamObject</i> [in, optional]

<dd>
<p>Specifies the stream that sets the timer, or <b>NULL</b> if the timer is set for the whole driver. The minidriver may only schedule one timer per stream, and one for the driver as a whole. This parameter is optional.</p>
</dd>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the minidriver's device extension. The minidriver specifies the size of this buffer in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>. The class driver then passes pointers to the buffer in the <b>HwDeviceExtension</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559706">HW_TIME_CONTEXT</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -param <i>NumberOfMicroseconds</i> [in]

<dd>
<p>Specifies the amount of time, in microseconds, before the timer expires.</p>
</dd>

### -param <i>TimerRoutine</i> [in]

<dd>
<p>Specifies the routine called when the timer expires. The routine's prototype must be of the form:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>    TimerRoutine(PVOID Context);</pre>
</td>
</tr>
</table></span></div>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to a context that the class driver passes to the callback routine once the timer expires.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>
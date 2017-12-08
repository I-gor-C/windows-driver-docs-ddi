---
UID: NC.strmini.PHW_QUERY_CLOCK_ROUTINE
title: PHW_QUERY_CLOCK_ROUTINE
author: windows-driver-content
description: Each stream may have a clock associated to it. The class driver queries the clock by calling the stream minidriver-supplied StrMiniClock function, provided in each stream's HW_STREAM_OBJECT.
old-location: stream\strminiclock.htm
old-project: stream
ms.assetid: ea230363-e2e8-48fb-982b-025615753e83
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StrMiniClock
req.alt-loc: strmini.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PHW_QUERY_CLOCK_ROUTINE callback



## -description
<p>Each stream may have a clock associated to it. The class driver queries the clock by calling the stream minidriver-supplied <i>StrMiniClock</i> function, provided in each stream's <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>.</p>


## -prototype

````
PHW_QUERY_CLOCK_ROUTINE StrMiniClock;

VOID StrMiniClock(
  _In_ PHW_TIME_CONTEXT HwTimeContext
)
{ ... }
````


## -parameters
<dl>

### -param HwTimeContext [in]

<dd>
<p>Pointer to the <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a> structure that <i>StrMiniClock</i> must fill out with the requested information.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A stream specifies its <i>StrMiniClock</i> function within the <b>HwClockFunction</b> member of the <a href="..\strmini\ns-strmini--hw-clock-object.md">HW_CLOCK_OBJECT</a> substructure of its <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>. The minidriver fills out the <b>HW_STREAM_OBJECT</b> for a stream within its <a href="stream.strminireceivedevicepacket">StrMiniReceiveDevicePacket</a> routine in response to a SRB_OPEN_STREAM request.</p>

<p>When the class driver calls <i>StrMiniClock</i>, it fills in the <b>HwDeviceExtension</b>, <b>HwStreamObject</b>, and <b>Function</b> members of the <i>HwTimeContext</i> parameter. It expects <i>StrMiniClock</i> to fill in the <b>Time</b> member with the time value, in 100-nanosecond units, specified in the <i>Function</i> parameter. <i>StrMiniClock</i> must also fill in the <b>SystemTime</b> member with the current system time, by calling <a href="..\wdm\nf-wdm-kequeryperformancecounter.md">KeQueryPerformanceCounter</a>, and converting the result to 100-nanosecond units.</p>

<p>The <i>StrMiniClock</i> routine must handle the functions specified in the <b>ClockSupportFlags</b> of the clock's HW_CLOCK_OBJECT. See <a href="..\strmini\ns-strmini--hw-clock-object.md">HW_CLOCK_OBJECT</a> for details.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\strmini\ns-strmini--hw-clock-object.md">HW_CLOCK_OBJECT</a>
</dt>
<dt>
<a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StrMiniClock routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

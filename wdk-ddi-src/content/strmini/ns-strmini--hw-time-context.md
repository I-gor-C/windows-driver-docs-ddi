---
UID: NS.strmini._HW_TIME_CONTEXT
title: HW_TIME_CONTEXT
author: windows-driver-content
description: The class driver passes an HW_TIME_CONTEXT structure as a parameter to be filled in by a stream's StrMiniClock routine, or returns a completed HW_TIME_CONTEXT structure when it responds to a StreamClassQueryMasterClock or StreamClassQueryMasterClockSync request.
old-location: stream\hw_time_context.htm
old-project: stream
ms.assetid: 4f349089-ff50-4f69-941f-ba3e9225abec
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: HW_TIME_CONTEXT, HW_TIME_CONTEXT, *PHW_TIME_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HW_TIME_CONTEXT
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

# HW_TIME_CONTEXT structure



## -description
<p>The class driver passes an HW_TIME_CONTEXT structure as a parameter to be filled in by a stream's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568452">StrMiniClock</a> routine, or returns a completed HW_TIME_CONTEXT structure when it responds to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568249">StreamClassQueryMasterClock</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568251">StreamClassQueryMasterClockSync</a> request.</p>


## -syntax

````
typedef struct _HW_TIME_CONTEXT {
  struct _HW_DEVICE_EXTENSION  *HwDeviceExtension;
  struct _HW_STREAM_OBJECT  *HwStreamObject;
  TIME_FUNCTION               Function;
  ULONGLONG                   Time;
  ULONGLONG                   SystemTime;
} HW_TIME_CONTEXT, *PHW_TIME_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>HwDeviceExtension</b>

<dd>
<p>Points to the minidriver's device extension buffer. The class driver fills in this member when it passes the structure to a stream's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568452">StrMiniClock</a>, or to the callback passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff568249">StreamClassQueryMasterClock</a>. When passed as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff568251">StreamClassQueryMasterClockSync</a>, the caller must fill in this member itself.</p>
<p>The minidriver may use its device extension to record private information global to the minidriver. The minidriver sets the size of this buffer in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>. The class driver also passes pointers to this buffer in the <b>HwDeviceExtension</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -field <b>HwStreamObject</b>

<dd>
<p>When the class driver passes HW_TIME_CONTEXT to a stream's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568452">StrMiniClock</a> routine, this member points to the stream's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a> structure.</p>
<p>When the class driver passes a completed HW_TIME_CONTEXT structure to the callback provided by <a href="https://msdn.microsoft.com/library/windows/hardware/ff568249">StreamClassQueryMasterClock</a>, it fills in this member with a pointer to the stream object of the stream that makes the query request.</p>
</dd>

### -field <b>Function</b>

<dd>
<p>Specifies the type of time value that is stored in the <b>Time</b> member. The possible values are:</p>
<p></p>
<dl>

### -field <a id="TIME_GET_STREAM_TIME"></a><a id="time_get_stream_time"></a>TIME_GET_STREAM_TIME

<dd>
<p>The <b>Time</b> member holds the current presentation time stamp.</p>
</dd>

### -field <a id="TIME_READ_ONBOARD_CLOCK"></a><a id="time_read_onboard_clock"></a>TIME_READ_ONBOARD_CLOCK

<dd>
<p>The <b>Time</b> member holds the current clock time.</p>
</dd>
</dl>
</dd>

### -field <b>Time</b>

<dd>
<p>The time value, in 100-nanosecond units, specified by the <b>Function</b> member.</p>
</dd>

### -field <b>SystemTime</b>

<dd>
<p>The current system time, in 100-nanosecond units.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559671">HW_CLOCK_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568249">StreamClassQueryMasterClock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568251">StreamClassQueryMasterClockSync</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568452">StrMiniClock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HW_TIME_CONTEXT structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

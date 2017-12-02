---
UID: NS.strmini._HW_CLOCK_OBJECT
title: HW_CLOCK_OBJECT
author: windows-driver-content
description: The HW_CLOCK_OBJECT structure describes the clock associated with a stream.
old-location: stream\hw_clock_object.htm
old-project: stream
ms.assetid: d6afe946-90cb-4b17-94ed-2e7c508985a3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HW_CLOCK_OBJECT, HW_CLOCK_OBJECT, *PHW_CLOCK_OBJECT
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
req.alt-api: HW_CLOCK_OBJECT
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

# HW_CLOCK_OBJECT structure



## -description
<p>The HW_CLOCK_OBJECT structure describes the clock associated with a stream.</p>


## -syntax

````
typedef struct _HW_CLOCK_OBJECT {
  PHW_CLOCK_FUNCTION HwClockFunction;
  ULONG              ClockSupportFlags;
  ULONG              Reserved[2];
} HW_CLOCK_OBJECT, *PHW_CLOCK_OBJECT;
````


## -struct-fields
<dl>

### -field HwClockFunction

<dd>
<p>Pointer to the stream's <a href="stream.strminiclock">StrMiniClock</a> routine.</p>
</dd>

### -field ClockSupportFlags

<dd>
<p>Specifies which options the <i>StrMiniClock</i> routine supports.</p>
<p></p>
<dl>

### -field CLOCK_SUPPORT_CAN_READ_ONBOARD_CLOCK

<dd>
<p>The <i>StrMiniClock</i> routine can return the current clock value for the stream's clock. The <i>StrMiniClock</i> routine must be able to handle a <b>Function</b> setting of TIME_READ_ONBOARD_CLOCK in the <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a> structure passed as a parameter.</p>
</dd>

### -field CLOCK_SUPPORT_CAN_RETURN_STREAM_TIME

<dd>
<p>The <i>StrMiniClock</i> routine can return the current presentation time stamp for the stream. The <i>StrMiniClock</i> routine must be able to handle a <b>Function</b> setting of TIME_GET_STREAM_TIME in the <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a> structure passed as a parameter.</p>
</dd>
</dl>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use. Do not use.</p>
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
<a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>
</dt>
<dt>
<a href="stream.strminiclock">StrMiniClock</a>
</dt>
<dt>
<a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HW_CLOCK_OBJECT structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

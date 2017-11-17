---
UID: NF.wdm.RtlTimeFieldsToTime
title: RtlTimeFieldsToTime
author: windows-driver-content
description: The RtlTimeFieldsToTime routine converts TIME_FIELDS information to a system time value.
old-location: kernel\rtltimefieldstotime.htm
ms.assetid: 5873b627-6ef4-4e2c-8a53-921f37b729bc
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlTimeFieldsToTime
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level (See Remarks section)
ms.keywords: RtlTimeFieldsToTime
req.iface: 
req.product: Windows 10 or later.
---

# RtlTimeFieldsToTime function



## -description
<p>The <b>RtlTimeFieldsToTime</b> routine converts <b>TIME_FIELDS</b> information to a system time value.</p>


## -syntax

````
BOOLEAN RtlTimeFieldsToTime(
  _In_  PTIME_FIELDS   TimeFields,
  _Out_ PLARGE_INTEGER Time
);
````


## -parameters
<dl>

### -param <i>TimeFields</i> [in]

<dd>
<p>Pointer to the following structure, containing the time information to be converted:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct TIME_FIELDS {
    CSHORT Year;
    CSHORT Month;
    CSHORT Day;
    CSHORT Hour;
    CSHORT Minute;
    CSHORT Second;
    CSHORT Milliseconds;
    CSHORT Weekday;
} TIME_FIELDS;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="Year"></a><a id="year"></a><a id="YEAR"></a><b>Year</b>

<dd>
<p>Specifies a value from 1601 on.</p>
</dd>

### -param <a id="Month"></a><a id="month"></a><a id="MONTH"></a><b>Month</b>

<dd>
<p>Specifies a value from 1 to 12.</p>
</dd>

### -param <a id="Day"></a><a id="day"></a><a id="DAY"></a><b>Day</b>

<dd>
<p>Specifies a value from 1 to 31.</p>
</dd>

### -param <a id="Hour"></a><a id="hour"></a><a id="HOUR"></a><b>Hour</b>

<dd>
<p>Specifies a value from 0 to 23.</p>
</dd>

### -param <a id="Minute"></a><a id="minute"></a><a id="MINUTE"></a><b>Minute</b>

<dd>
<p>Specifies a value from 0 to 59.</p>
</dd>

### -param <a id="Second"></a><a id="second"></a><a id="SECOND"></a><b>Second</b>

<dd>
<p>Specifies a value from 0 to 59.</p>
</dd>

### -param <a id="Milliseconds"></a><a id="milliseconds"></a><a id="MILLISECONDS"></a><b>Milliseconds</b>

<dd>
<p>Specifies a value from 0 to 999.</p>
</dd>

### -param <a id="Weekday"></a><a id="weekday"></a><a id="WEEKDAY"></a><b>Weekday</b>

<dd>
<p>Specifies a value from 0 to 6 (Sunday to Saturday). </p>
</dd>
</dl>
</dd>

### -param <i>Time</i> [out]

<dd>
<p>Pointer to a buffer, which is to contain the converted system time value as a large integer. </p>
</dd>
</dl>

## -returns
<p><b>RtlTimeFieldsToTime</b> returns <b>TRUE</b> if the input <i>TimeFields</i> data was successfully converted.</p>

## -remarks
<p><b>RtlTimeFieldsToTime</b> ignores the <b>Weekday</b> value in <i>TimeFields</i>.</p>

<p>Callers of <b>RtlTimeFieldsToTime</b> can be running at any IRQL if both input buffers are resident.</p>

<p><b>RtlTimeFieldsToTime</b> ignores the <b>Weekday</b> value in <i>TimeFields</i>.</p>

<p>Callers of <b>RtlTimeFieldsToTime</b> can be running at any IRQL if both input buffers are resident.</p>

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
<p>Any level (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545483">ExLocalTimeToSystemTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545622">ExSystemTimeToLocalTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553068">KeQuerySystemTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562884">RtlTimeToTimeFields</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlTimeFieldsToTime routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

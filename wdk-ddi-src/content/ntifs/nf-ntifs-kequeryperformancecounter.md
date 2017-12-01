---
UID: NF.ntifs.KeQueryPerformanceCounter
title: KeQueryPerformanceCounter
author: windows-driver-content
description: The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements.
old-location: kernel\kequeryperformancecounter.htm
old-project: kernel
ms.assetid: ee1dbd20-5502-4448-b39a-4629ddc73d01
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeQueryPerformanceCounter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryPerformanceCounter
req.alt-loc: Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: Hal.dll
req.irql: Any level
req.iface: 
---

# KeQueryPerformanceCounter function



## -description
<p>The <b>KeQueryPerformanceCounter</b> routine retrieves the current value and frequency of the performance counter.</p>
<p>Use <b>KeQueryPerformanceCounter</b> to acquire high resolution (&lt;1us) time stamps for time interval measurements.</p>


## -syntax

````
LARGE_INTEGER KeQueryPerformanceCounter(
  _Out_opt_ PLARGE_INTEGER PerformanceFrequency
);
````


## -parameters
<dl>

### -param <i>PerformanceFrequency</i> [out, optional]

<dd>
<p>A pointer to a variable to which <b>KeQueryPerformanceCounter</b> writes the performance counter frequency, in ticks per second. This parameter is optional and can be NULL if the caller does not need the counter frequency value.</p>
</dd>
</dl>

## -returns
<p><b>KeQueryPerformanceCounter</b> returns the performance counter value in units of ticks.</p>

## -remarks
<p><b>KeQueryPerformanceCounter</b> returns a 64-bit integer that represents the current value of a high-resolution monotonically nondecreasing counter. </p>

<p>To obtain the frequency of the performance counter, specify a non-<b>NULL</b> pointer value for the <i>PerformanceFrequency</i> parameter. The frequency of the performance counter is fixed at system boot and is consistent across all processors. Therefore, a driver can cache the frequency of the performance counter during initialization.  </p>

<p>For more info about this function and its usage, see <a href="base.acquiring_high-resolution_time_stamps">Acquiring high-resolution time stamps</a>. </p>

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
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hal.dll</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-kequeryinterrupttime.md">KeQueryInterruptTime</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kequerysystemtime.md">KeQuerySystemTime</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-kequerytickcount.md">KeQueryTickCount</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kequerytimeincrement.md">KeQueryTimeIncrement</a>
</dt>
<dt>
<a href="base.queryperformancecounter">QueryPerformanceCounter</a>
</dt>
<dt>
<a href="base.queryperformancefrequency">QueryPerformanceFrequency</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryPerformanceCounter routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

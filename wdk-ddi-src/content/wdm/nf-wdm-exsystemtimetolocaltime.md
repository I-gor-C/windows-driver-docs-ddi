---
UID: NF.wdm.ExSystemTimeToLocalTime
title: ExSystemTimeToLocalTime
author: windows-driver-content
description: The ExSystemTimeToLocalTime routine converts a GMT system time value to the local system time for the current time zone.
old-location: kernel\exsystemtimetolocaltime.htm
old-project: kernel
ms.assetid: d77ce60e-7b23-4f60-af63-d613ceba281e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExSystemTimeToLocalTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExSystemTimeToLocalTime
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
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# ExSystemTimeToLocalTime function



## -description
<p>The <b>ExSystemTimeToLocalTime</b> routine converts a GMT system time value to the local system time for the current time zone.</p>


## -syntax

````
VOID ExSystemTimeToLocalTime(
  _In_  PLARGE_INTEGER SystemTime,
  _Out_ PLARGE_INTEGER LocalTime
);
````


## -parameters
<dl>

### -param <i>SystemTime</i> [in]

<dd>
<p>A pointer to a variable set to the unbiased, GMT system time.</p>
</dd>

### -param <i>LocalTime</i> [out]

<dd>
<p>A pointer to the returned value for the current locale.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ExSystemTimeToLocalTime</b> subtracts the time-zone bias from the GMT system time value to compute the corresponding time at the current locale.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exlocaltimetosystemtime.md">ExLocalTimeToSystemTime</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExSystemTimeToLocalTime routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

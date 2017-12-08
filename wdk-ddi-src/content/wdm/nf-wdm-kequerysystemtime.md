---
UID: NF.wdm.KeQuerySystemTime
title: KeQuerySystemTime function
author: windows-driver-content
description: The KeQuerySystemTime routine obtains the current system time.
old-location: kernel\kequerysystemtime.htm
old-project: kernel
ms.assetid: de271bd2-93cf-444d-889d-09c7e654e688
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeQuerySystemTime
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
req.alt-api: KeQuerySystemTime
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
req.product: Windows 10 or later.
---

# KeQuerySystemTime function



## -description
The <b>KeQuerySystemTime</b> routine obtains the current system time.


## -syntax

````
VOID KeQuerySystemTime(
  _Out_ PLARGE_INTEGER CurrentTime
);
````


## -parameters

### -param CurrentTime [out]

Pointer to the current time on return from <b>KeQuerySystemTime</b>. 

## -returns
None

## -remarks
System time is a count of 100-nanosecond intervals since January 1, 1601. System time is typically updated approximately every ten milliseconds. This value is computed for the GMT time zone. To adjust this value for the local time zone use <a href="kernel.exsystemtimetolocaltime">ExSystemTimeToLocalTime</a>. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows 2000.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exsystemtimetolocaltime">ExSystemTimeToLocalTime</a>
</dt>
<dt>
<a href="kernel.kequeryperformancecounter">KeQueryPerformanceCounter</a>
</dt>
<dt>
<a href="kernel.kequerytickcount">KeQueryTickCount</a>
</dt>
<dt>
<a href="kernel.kequerytimeincrement">KeQueryTimeIncrement</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQuerySystemTime routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

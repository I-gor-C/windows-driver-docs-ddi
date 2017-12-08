---
UID: NF.wdm.KeQueryTimeIncrement
title: KeQueryTimeIncrement function
author: windows-driver-content
description: The KeQueryTimeIncrement routine returns the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts.
old-location: kernel\kequerytimeincrement.htm
old-project: kernel
ms.assetid: f8291e2b-a7a1-4a19-9137-fcd93e62bbaf
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeQueryTimeIncrement
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
req.alt-api: KeQueryTimeIncrement
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

# KeQueryTimeIncrement function



## -description
The <b>KeQueryTimeIncrement</b> routine returns the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts.


## -syntax

````
ULONG KeQueryTimeIncrement(void);
````


## -parameters


## -returns
<b>KeQueryTimeIncrement</b> returns a ULONG value indicating the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts.

<b>KeQueryTimeIncrement</b> returns a ULONG value indicating the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts.

<b>KeQueryTimeIncrement</b> returns a ULONG value indicating the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts.

## -remarks
At startup time, the operating system determines the time increment to use for the system time. This time increment remains constant until the computer restarts. During this time, calls to <b>KeQueryTimeIncrement</b> always return the same time increment value. The time increment does not change while the computer is running, and it does not change as the result of a suspend-resume cycle.

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
<a href="kernel.kequeryperformancecounter">KeQueryPerformanceCounter</a>
</dt>
<dt>
<a href="kernel.kequerysystemtime">KeQuerySystemTime</a>
</dt>
<dt>
<a href="kernel.kequerytickcount">KeQueryTickCount</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryTimeIncrement routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

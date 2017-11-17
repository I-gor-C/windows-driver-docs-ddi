---
UID: NF.wdm.KeQueryUnbiasedInterruptTime
title: KeQueryUnbiasedInterruptTime
author: windows-driver-content
description: The KeQueryUnbiasedInterruptTime routine returns the current value of the system interrupt time count.
old-location: kernel\kequeryunbiasedinterrupttime.htm
ms.assetid: 2a041946-0335-466e-b2f9-b486031e777a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryUnbiasedInterruptTime
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
ms.keywords: KeQueryUnbiasedInterruptTime
req.iface: 
req.product: Windows 10 or later.
---

# KeQueryUnbiasedInterruptTime function



## -description
<p>The <b>KeQueryUnbiasedInterruptTime</b> routine returns the current value of the system <a href="http://go.microsoft.com/fwlink/p/?linkid=201082">interrupt time</a> count.</p>


## -syntax

````
ULONGLONG KeQueryUnbiasedInterruptTime(void);
````


## -parameters


## -returns
<p><b>KeQueryUnbiasedInterruptTime</b> returns the current interrupt time count in 100-nanosecond units. The count begins at zero when the computer starts. Updates to this count are suspended when the computer enters a sleep state and are resumed when the computer awakens. </p>

<p><b>KeQueryUnbiasedInterruptTime</b> returns the current interrupt time count in 100-nanosecond units. The count begins at zero when the computer starts. Updates to this count are suspended when the computer enters a sleep state and are resumed when the computer awakens. </p>

<p><b>KeQueryUnbiasedInterruptTime</b> returns the current interrupt time count in 100-nanosecond units. The count begins at zero when the computer starts. Updates to this count are suspended when the computer enters a sleep state and are resumed when the computer awakens. </p>

## -remarks
<p>Kernel-mode drivers can call this routine to measure relatively fine-grained durations.</p>

<p>This routine returns the system interrupt time, which is the amount of time since the operating system was last started. The interrupt-time count begins at zero when the operating system starts and is incremented at each clock interrupt by the length of a clock tick. For various reasons, such as hardware differences, the length of a system clock tick can vary between computers. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553075">KeQueryTimeIncrement</a> routine to determine the size of a system clock tick.</p>

<p>The <b>KeQueryUnbiasedInterruptTime</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553025">KeQueryInterruptTime</a> routines are similar, but they differ in the way in which they account for periods in which the operating system suspends updates of the interrupt time count. For example, these updates are suspended while the computer is in a system sleep state. To compensate for periods in which updates of the count are suspended, <b>KeQueryInterruptTime</b> returns a biased count value that it calculates by adding a bias count to the raw interrupt time count. The bias count is the estimated sum of all of the updates to the interrupt time count that the operating system missed while counting was suspended. In contrast, <b>KeQueryUnbiasedInterruptTime</b> returns the raw, unbiased count.</p>

<p>Unlike the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553068">KeQuerySystemTime</a> routine, <b>KeQueryUnbiasedInterruptTime</b> returns a count value that is not affected by operations that set or reset the system time. In addition, the system time that is reported by <b>KeQuerySystemTime</b> is typically updated approximately every ten milliseconds. In contrast, the count that is returned by <b>KeQueryUnbiasedInterruptTime</b> is updated at least once per system clock tick.</p>

<p>In Windows 2000 and later versions of the Windows operating system, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553053">KeQueryPerformanceCounter</a> routine provides the finest grained running count that is available from the operating system.</p>

<p>Kernel-mode drivers can call this routine to measure relatively fine-grained durations.</p>

<p>This routine returns the system interrupt time, which is the amount of time since the operating system was last started. The interrupt-time count begins at zero when the operating system starts and is incremented at each clock interrupt by the length of a clock tick. For various reasons, such as hardware differences, the length of a system clock tick can vary between computers. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553075">KeQueryTimeIncrement</a> routine to determine the size of a system clock tick.</p>

<p>The <b>KeQueryUnbiasedInterruptTime</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553025">KeQueryInterruptTime</a> routines are similar, but they differ in the way in which they account for periods in which the operating system suspends updates of the interrupt time count. For example, these updates are suspended while the computer is in a system sleep state. To compensate for periods in which updates of the count are suspended, <b>KeQueryInterruptTime</b> returns a biased count value that it calculates by adding a bias count to the raw interrupt time count. The bias count is the estimated sum of all of the updates to the interrupt time count that the operating system missed while counting was suspended. In contrast, <b>KeQueryUnbiasedInterruptTime</b> returns the raw, unbiased count.</p>

<p>Unlike the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553068">KeQuerySystemTime</a> routine, <b>KeQueryUnbiasedInterruptTime</b> returns a count value that is not affected by operations that set or reset the system time. In addition, the system time that is reported by <b>KeQuerySystemTime</b> is typically updated approximately every ten milliseconds. In contrast, the count that is returned by <b>KeQueryUnbiasedInterruptTime</b> is updated at least once per system clock tick.</p>

<p>In Windows 2000 and later versions of the Windows operating system, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553053">KeQueryPerformanceCounter</a> routine provides the finest grained running count that is available from the operating system.</p>

<p>Kernel-mode drivers can call this routine to measure relatively fine-grained durations.</p>

<p>This routine returns the system interrupt time, which is the amount of time since the operating system was last started. The interrupt-time count begins at zero when the operating system starts and is incremented at each clock interrupt by the length of a clock tick. For various reasons, such as hardware differences, the length of a system clock tick can vary between computers. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553075">KeQueryTimeIncrement</a> routine to determine the size of a system clock tick.</p>

<p>The <b>KeQueryUnbiasedInterruptTime</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553025">KeQueryInterruptTime</a> routines are similar, but they differ in the way in which they account for periods in which the operating system suspends updates of the interrupt time count. For example, these updates are suspended while the computer is in a system sleep state. To compensate for periods in which updates of the count are suspended, <b>KeQueryInterruptTime</b> returns a biased count value that it calculates by adding a bias count to the raw interrupt time count. The bias count is the estimated sum of all of the updates to the interrupt time count that the operating system missed while counting was suspended. In contrast, <b>KeQueryUnbiasedInterruptTime</b> returns the raw, unbiased count.</p>

<p>Unlike the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553068">KeQuerySystemTime</a> routine, <b>KeQueryUnbiasedInterruptTime</b> returns a count value that is not affected by operations that set or reset the system time. In addition, the system time that is reported by <b>KeQuerySystemTime</b> is typically updated approximately every ten milliseconds. In contrast, the count that is returned by <b>KeQueryUnbiasedInterruptTime</b> is updated at least once per system clock tick.</p>

<p>In Windows 2000 and later versions of the Windows operating system, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553053">KeQueryPerformanceCounter</a> routine provides the finest grained running count that is available from the operating system.</p>

<p>Kernel-mode drivers can call this routine to measure relatively fine-grained durations.</p>

<p>This routine returns the system interrupt time, which is the amount of time since the operating system was last started. The interrupt-time count begins at zero when the operating system starts and is incremented at each clock interrupt by the length of a clock tick. For various reasons, such as hardware differences, the length of a system clock tick can vary between computers. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553075">KeQueryTimeIncrement</a> routine to determine the size of a system clock tick.</p>

<p>The <b>KeQueryUnbiasedInterruptTime</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553025">KeQueryInterruptTime</a> routines are similar, but they differ in the way in which they account for periods in which the operating system suspends updates of the interrupt time count. For example, these updates are suspended while the computer is in a system sleep state. To compensate for periods in which updates of the count are suspended, <b>KeQueryInterruptTime</b> returns a biased count value that it calculates by adding a bias count to the raw interrupt time count. The bias count is the estimated sum of all of the updates to the interrupt time count that the operating system missed while counting was suspended. In contrast, <b>KeQueryUnbiasedInterruptTime</b> returns the raw, unbiased count.</p>

<p>Unlike the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553068">KeQuerySystemTime</a> routine, <b>KeQueryUnbiasedInterruptTime</b> returns a count value that is not affected by operations that set or reset the system time. In addition, the system time that is reported by <b>KeQuerySystemTime</b> is typically updated approximately every ten milliseconds. In contrast, the count that is returned by <b>KeQueryUnbiasedInterruptTime</b> is updated at least once per system clock tick.</p>

<p>In Windows 2000 and later versions of the Windows operating system, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553053">KeQueryPerformanceCounter</a> routine provides the finest grained running count that is available from the operating system.</p>

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
<p>Available starting with Windows 7.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553025">KeQueryInterruptTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn903729">KeQueryInterruptTimePrecise</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553053">KeQueryPerformanceCounter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553068">KeQuerySystemTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553075">KeQueryTimeIncrement</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryUnbiasedInterruptTime routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

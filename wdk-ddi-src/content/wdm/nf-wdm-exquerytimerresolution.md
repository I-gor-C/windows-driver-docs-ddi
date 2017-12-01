---
UID: NF.wdm.ExQueryTimerResolution
title: ExQueryTimerResolution
author: windows-driver-content
description: The ExQueryTimerResolution routine reports the range of timer resolutions that are supported by the system clock.
old-location: kernel\exquerytimerresolution.htm
old-project: kernel
ms.assetid: 2648AD10-B2D7-4F24-A508-239DA6AF551D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExQueryTimerResolution
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExQueryTimerResolution
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: Any level.
req.iface: 
req.product: Windows 10 or later.
---

# ExQueryTimerResolution function



## -description
<p>The <b>ExQueryTimerResolution</b> routine reports the range of timer resolutions that are supported by the system clock.</p>


## -syntax

````
VOID ExQueryTimerResolution(
  _Out_ PULONG MaximumTime,
  _Out_ PULONG MinimumTime,
  _Out_ PULONG CurrentTime
);
````


## -parameters
<dl>

### -param <i>MaximumTime</i> [out]

<dd>
<p>A pointer to a location to which the routine writes the maximum time interval, in 100-nanosecond units, between successive ticks of the system clock. A <i>tick</i> is an interrupt caused by the system clock timer.</p>
</dd>

### -param <i>MinimumTime</i> [out]

<dd>
<p>A pointer to a location to which the routine writes the minimum time interval, in 100-nanosecond units, between successive ticks of the system clock.</p>
</dd>

### -param <i>CurrentTime</i> [out]

<dd>
<p>A pointer to a location to which the routine writes the current time interval, in 100-nanosecond units, between successive ticks of the system clock.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>If your driver calls the <a href="..\wdm\nf-wdm-exsettimerresolution.md">ExSetTimerResolution</a> routine to change the time interval between successive system clock interrupts, the driver can first call <b>ExQueryTimerResolution</b> to determine the range of intervals supported by the system clock.</p>

<p>When your driver calls a routine such as <a href="..\wdm\nf-wdm-kesettimerex.md">KeSetTimerEx</a> to set a timer, the accuracy of the timer depends on the resolution of the system clock. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj602805">Timer Accuracy</a>.</p>

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
<p>Available starting with Windows 8.</p>
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
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exsettimerresolution.md">ExSetTimerResolution</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kesettimerex.md">KeSetTimerEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExQueryTimerResolution routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

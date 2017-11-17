---
UID: NF.wdm.ExSetTimerResolution
title: ExSetTimerResolution
author: windows-driver-content
description: The ExSetTimerResolution routine modifies the frequency at which the system clock interrupts. Use this routine with extreme caution (see the following Remarks section).
old-location: kernel\exsettimerresolution.htm
ms.assetid: 968d57fa-7a8e-42cf-b73b-d669ecbbaf48
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
req.alt-api: ExSetTimerResolution
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExApcLte2, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
ms.keywords: ExSetTimerResolution
req.iface: 
req.product: Windows 10 or later.
---

# ExSetTimerResolution function



## -description
<p>The <b>ExSetTimerResolution</b> routine modifies the frequency at which the system clock interrupts. <u>Use this routine with extreme caution (see the following Remarks section).</u></p>


## -syntax

````
ULONG ExSetTimerResolution(
  _In_ ULONG   DesiredTime,
  _In_ BOOLEAN SetResolution
);
````


## -parameters
<dl>

### -param <i>DesiredTime</i> [in]

<dd>
<p>Specifies the amount of time that should elapse between each timer interrupt, in 100-nanosecond units. The minimum value is approximately 10,000 (1 millisecond) but can vary slightly by platform. (This parameter is ignored if <i>SetResolution</i> is <b>FALSE</b>.) </p>
</dd>

### -param <i>SetResolution</i> [in]

<dd>
<p>If <b>TRUE</b>, the call is a request to set the clock interrupt frequency to the value specified by <i>DesiredTime</i>. If <b>FALSE</b>, the call is a request to restore the clock interrupt frequency to the system's default value, which is platform-specific. </p>
</dd>
</dl>

## -returns
<p><b>ExSetTimerResolution</b> returns the new timer resolution, in 100-nanosecond units.</p>

## -remarks
<p>To set the timer resolution, a driver calls this routine passing <b>TRUE</b> as the parameter for <i>SetResolution</i>. The following rules apply:</p>

<p>The routine changes the clock interrupt frequency <u>only</u> if the specified  <i>DesiredTime</i> value is less than the current setting.</p>

<p>If a driver requests a <i>DesiredTime</i> value that is greater than what is currently set, the routine just returns the current setting.</p>

<p>If a driver requests a <i>DesiredTime</i> value that is less than the system clock can support, the routine uses the smallest resolution the system can support, and returns that value.</p>

<p>If you use this routine to change the clock interrupt frequency, your driver <u>must</u> restore the default interrupt frequency, typically by making the following call before being unloaded:</p>

<p>(If multiple drivers have attempted to modify the clock interrupt frequency, the system does not restore the default frequency until all of these drivers have called this routine with a <i>SetResolution</i> value of <b>FALSE</b>.)</p>

<p><u>Note that the result of changing the clock interrupt frequency is system-wide and can have a severely negative effect on system performance. Also note that higher clock interrupt frequencies can shorten a system's battery life.</u></p>

<p>During the processing of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a> request, the power manager holds a lock on a resource that <b>ExSetTimerResolution</b> must acquire to complete. Consequently, a deadlock will occur if a driver directly or indirectly calls <b>ExSetTimerResolution</b> while processing a power request, and then waits for the call to <b>ExSetTimerResolution</b> to return before the driver completes the power request. For more information about safely calling <b>ExSetTimerResolution</b> while processing a power IRP, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540721">Calling ExSetTimerResolution While Processing a Power IRP</a>.</p>

<p>To set the timer resolution, a driver calls this routine passing <b>TRUE</b> as the parameter for <i>SetResolution</i>. The following rules apply:</p>

<p>The routine changes the clock interrupt frequency <u>only</u> if the specified  <i>DesiredTime</i> value is less than the current setting.</p>

<p>If a driver requests a <i>DesiredTime</i> value that is greater than what is currently set, the routine just returns the current setting.</p>

<p>If a driver requests a <i>DesiredTime</i> value that is less than the system clock can support, the routine uses the smallest resolution the system can support, and returns that value.</p>

<p>If you use this routine to change the clock interrupt frequency, your driver <u>must</u> restore the default interrupt frequency, typically by making the following call before being unloaded:</p>

<p>(If multiple drivers have attempted to modify the clock interrupt frequency, the system does not restore the default frequency until all of these drivers have called this routine with a <i>SetResolution</i> value of <b>FALSE</b>.)</p>

<p><u>Note that the result of changing the clock interrupt frequency is system-wide and can have a severely negative effect on system performance. Also note that higher clock interrupt frequencies can shorten a system's battery life.</u></p>

<p>During the processing of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a> request, the power manager holds a lock on a resource that <b>ExSetTimerResolution</b> must acquire to complete. Consequently, a deadlock will occur if a driver directly or indirectly calls <b>ExSetTimerResolution</b> while processing a power request, and then waits for the call to <b>ExSetTimerResolution</b> to return before the driver completes the power request. For more information about safely calling <b>ExSetTimerResolution</b> while processing a power IRP, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540721">Calling ExSetTimerResolution While Processing a Power IRP</a>.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547751">IrqlExApcLte2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExSetTimerResolution routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

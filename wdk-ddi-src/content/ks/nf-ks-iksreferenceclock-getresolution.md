---
UID: NF.ks.IKsReferenceClock.GetResolution
title: IKsReferenceClock::GetResolution
author: windows-driver-content
description: The IKsReferenceClock::GetResolution method queries the associated reference clock for its resolution.
old-location: stream\iksreferenceclock_getresolution.htm
ms.assetid: 7fb70431-db09-470b-b795-826aba3a8b77
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsReferenceClock.GetResolution
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: IKsReferenceClock, GetResolution, IKsReferenceClock::GetResolution
req.iface: IKsReferenceClock
---

# IKsReferenceClock::GetResolution method



## -description
<p>The <b>IKsReferenceClock::GetResolution</b> method queries the associated reference clock for its resolution.</p>


## -syntax

````
NTSTATUS GetResolution(
  [out] PKSRESOLUTION Resolution
);
````


## -parameters
<dl>

### -param <i>Resolution</i> [out]

<dd>
<p>Specifies granularity and notification error of the clock in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566806">KSRESOLUTION</a> structure.</p>
</dd>
</dl>

## -returns
<p>The <b>IKsReferenceClock::GetResolution</b> method returns STATUS_SUCCESS or the error code that the relevant clock returned from its <b>GetResolution</b> property. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a>. May return STATUS_DEVICE_NOT_READY if no clock is assigned.</p>

## -remarks
<p>This method retrieves the underlying clock's resolution property, which specifies the clock's increment granularity and notification error in 100-nanosecond units. The finest granularity is one unit; less granular increments contain larger numbers.</p>

<p>The least amount of notification error greater than the clock granularity is zero units; less accurate clocks use larger numbers to indicate  error. The proxy can use this resolution property to determine maximum error and resolution in event notification and synchronization.</p>

<p>For more information, see <a href="NULL">AVStream Clocks</a>.</p>

<p>AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a> property to retrieve the clock resolution.</p>

<p>This method retrieves the underlying clock's resolution property, which specifies the clock's increment granularity and notification error in 100-nanosecond units. The finest granularity is one unit; less granular increments contain larger numbers.</p>

<p>The least amount of notification error greater than the clock granularity is zero units; less accurate clocks use larger numbers to indicate  error. The proxy can use this resolution property to determine maximum error and resolution in event notification and synchronization.</p>

<p>For more information, see <a href="NULL">AVStream Clocks</a>.</p>

<p>AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a> property to retrieve the clock resolution.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563517">KsPinGetReferenceClockInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsReferenceClock::GetResolution method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

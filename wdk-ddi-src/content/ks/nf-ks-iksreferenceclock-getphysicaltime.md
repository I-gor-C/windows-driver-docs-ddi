---
UID: NF.ks.IKsReferenceClock.GetPhysicalTime
title: IKsReferenceClock::GetPhysicalTime
author: windows-driver-content
description: The IKsReferenceClock::GetPhysicalTime method queries the associated reference clock for the current physical time.
old-location: stream\iksreferenceclock_getphysicaltime.htm
old-project: stream
ms.assetid: 96c8d5ef-e9ab-40a6-88e1-56efdb7157b7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsReferenceClock, GetPhysicalTime, IKsReferenceClock::GetPhysicalTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsReferenceClock.GetPhysicalTime
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
req.iface: IKsReferenceClock
---

# IKsReferenceClock::GetPhysicalTime method



## -description
<p>The <b>IKsReferenceClock::GetPhysicalTime</b> method queries the associated reference clock for the current physical time.</p>


## -syntax

````
LONGLONG GetPhysicalTime();
````


## -parameters


## -returns
<p>The <b>IKsReferenceClock::GetPhysicalTime</b> method returns the current physical time for the associated pin, specified by default in 100-nanosecond units.</p>

<p>The <b>IKsReferenceClock::GetPhysicalTime</b> method returns the current physical time for the associated pin, specified by default in 100-nanosecond units.</p>

<p>The <b>IKsReferenceClock::GetPhysicalTime</b> method returns the current physical time for the associated pin, specified by default in 100-nanosecond units.</p>

## -remarks
<p>Physical time is tied to a physical clock, either the system clock or an on-board hardware clock.</p>

<p>The physical clock time progresses continuously. Unlike the presentation time, it is not reversible.</p>

<p>Clocks are not required to support a 100-nanosecond resolution. To determine the clock resolution, clients can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a> request.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/fc1d5bca-72e3-48e2-b46f-09a13bba83b4">AVStream Clocks</a>.</p>

<p>AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565088">KSPROPERTY_CLOCK_PHYSICALTIME</a> property to retrieve the physical time.</p>

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
<a href="..\ks\nf-ks-kspingetreferenceclockinterface.md">KsPinGetReferenceClockInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsReferenceClock::GetPhysicalTime method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

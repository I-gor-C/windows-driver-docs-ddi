---
UID: NF.ks.IKsReferenceClock.GetCorrelatedPhysicalTime
title: IKsReferenceClock::GetCorrelatedPhysicalTime
author: windows-driver-content
description: The IKsReferenceClock::GetCorrelatedPhysicalTime method queries the associated reference clock for the current physical time and retrieves the correlated system time.
old-location: stream\iksreferenceclock_getcorrelatedphysicaltime.htm
old-project: stream
ms.assetid: b80f6e20-410d-4984-8535-782a84c6af7e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsReferenceClock, GetCorrelatedPhysicalTime, IKsReferenceClock::GetCorrelatedPhysicalTime
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
req.alt-api: IKsReferenceClock.GetCorrelatedPhysicalTime
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

# IKsReferenceClock::GetCorrelatedPhysicalTime method



## -description
<p>The <b>IKsReferenceClock::GetCorrelatedPhysicalTime</b> method queries the associated reference clock for the current physical time and retrieves the correlated system time.  </p>


## -syntax

````
LONGLONG GetCorrelatedPhysicalTime(
  [out] PLONGLONG SystemTime
);
````


## -parameters
<dl>

### -param <i>SystemTime</i> [out]

<dd>
<p>Specifies the current system time in 100 nanosecond units.</p>
</dd>
</dl>

## -returns
<p>The <b>IKsReferenceClock::GetCorrelatedPhysicalTime</b> method returns the current physical clock time, specified by default in 100-nanosecond units. The correlated system time is returned in <i>SystemTime</i>.</p>

## -remarks
<p>Use this method to determine the difference between physical time and system time. <b>IKsReferenceClock::GetCorrelatedPhysicalTime</b> returns the times that both clocks show at the same moment.</p>

<p>For more information, see <a href="NULL">AVStream Clocks</a>.</p>

<p>AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564461">KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME</a> property to retrieve the correlated physical time.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsReferenceClock::GetCorrelatedPhysicalTime method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ksproxy.IKsClockPropertySet.KsGetCorrelatedTime
title: IKsClockPropertySet::KsGetCorrelatedTime
author: windows-driver-content
description: The KsGetCorrelatedTime method retrieves the current time and the correlated system time from the underlying clock.
old-location: stream\iksclockpropertyset_ksgetcorrelatedtime.htm
old-project: stream
ms.assetid: b91f33b3-2706-4c94-9960-ceea023891af
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsClockPropertySet, KsGetCorrelatedTime, IKsClockPropertySet::KsGetCorrelatedTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsClockPropertySet.KsGetCorrelatedTime
req.alt-loc: ksproxy.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IKsClockPropertySet
---

# IKsClockPropertySet::KsGetCorrelatedTime method



## -description
<p>The <b>KsGetCorrelatedTime</b> method retrieves the current time and the correlated system time from the underlying clock. </p>


## -syntax

````
HRESULT KsGetCorrelatedTime(
  [out] KSCORRELATED_TIME *CorrelatedTime
);
````


## -parameters
<dl>

### -param <i>CorrelatedTime</i> [out]

<dd>
<p>Pointer to a variable that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561033">KSCORRELATED_TIME</a> structure that contains the current clock time along with the correlated system time.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The <b>KsGetCorrelatedTime</b> method retrieves the current time and the correlated system in an atomic operation. </p>

<p>The proxy uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564465">KSPROPERTY_CLOCK_CORRELATEDTIME</a> property to retrieve the correlated time. </p>

<p>The <b>KsGetCorrelatedTime</b> method retrieves the current time and the correlated system in an atomic operation. </p>

<p>The proxy uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564465">KSPROPERTY_CLOCK_CORRELATEDTIME</a> property to retrieve the correlated time. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559756">IKsClockPropertySet::KsSetCorrelatedTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561033">KSCORRELATED_TIME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564465">KSPROPERTY_CLOCK_CORRELATEDTIME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsClockPropertySet::KsGetCorrelatedTime method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

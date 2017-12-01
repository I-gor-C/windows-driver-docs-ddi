---
UID: NF.ksproxy.IKsClockPropertySet.KsSetCorrelatedTime
title: IKsClockPropertySet::KsSetCorrelatedTime
author: windows-driver-content
description: The KsSetCorrelatedTime method sets the current time with the correlated system time on the underlying clock.
old-location: stream\iksclockpropertyset_kssetcorrelatedtime.htm
old-project: stream
ms.assetid: 58281b50-14b6-4e24-972a-ab3b1d88eb50
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsClockPropertySet, KsSetCorrelatedTime, IKsClockPropertySet::KsSetCorrelatedTime
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
req.alt-api: IKsClockPropertySet.KsSetCorrelatedTime
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

# IKsClockPropertySet::KsSetCorrelatedTime method



## -description
<p>The <b>KsSetCorrelatedTime</b> method sets the current time with the correlated system time on the underlying clock. </p>


## -syntax

````
HRESULT KsSetCorrelatedTime(
  [in] KSCORRELATED_TIME *CorrelatedTime
);
````


## -parameters
<dl>

### -param <i>CorrelatedTime</i> [in]

<dd>
<p>Pointer to a <a href="stream.kscorrelated_time">KSCORRELATED_TIME</a> structure that contains the current clock time along with the correlated system time to which to set the underlying clock. </p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The proxy uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564465">KSPROPERTY_CLOCK_CORRELATEDTIME</a> property to set the correlated time. </p>

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
<a href="stream.iksclockpropertyset_ksgetcorrelatedtime">IKsClockPropertySet::KsGetCorrelatedTime</a>
</dt>
<dt>
<a href="stream.kscorrelated_time">KSCORRELATED_TIME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564465">KSPROPERTY_CLOCK_CORRELATEDTIME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsClockPropertySet::KsSetCorrelatedTime method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ksproxy.IKsClockPropertySet.KsSetPhysicalTime
title: IKsClockPropertySet::KsSetPhysicalTime
author: windows-driver-content
description: The KsSetPhysicalTime method sets the physical time on the underlying clock.
old-location: stream\iksclockpropertyset_kssetphysicaltime.htm
old-project: stream
ms.assetid: 2f8eb011-1fe1-40f6-b833-50d3e853bffd
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsClockPropertySet, KsSetPhysicalTime, IKsClockPropertySet::KsSetPhysicalTime
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
req.alt-api: IKsClockPropertySet.KsSetPhysicalTime
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

# IKsClockPropertySet::KsSetPhysicalTime method



## -description
<p>The <b>KsSetPhysicalTime</b> method sets the physical time on the underlying clock. </p>


## -syntax

````
HRESULT KsSetPhysicalTime(
  [in] LONGLONG Time
);
````


## -parameters
<dl>

### -param <i>Time</i> [in]

<dd>
<p>Physical time to which to set the underlying clock.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The physical time is based on some underlying physical clock that always progresses, even if the physical type of clock must be changed on the fly. Other physical clocks use an underlying clock's physical time for rate matching.</p>

<p>The proxy uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565088">KSPROPERTY_CLOCK_PHYSICALTIME</a> property to set the physical time. </p>

<p>The physical time is based on some underlying physical clock that always progresses, even if the physical type of clock must be changed on the fly. Other physical clocks use an underlying clock's physical time for rate matching.</p>

<p>The proxy uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565088">KSPROPERTY_CLOCK_PHYSICALTIME</a> property to set the physical time. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559742">IKsClockPropertySet::KsGetPhysicalTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565088">KSPROPERTY_CLOCK_PHYSICALTIME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsClockPropertySet::KsSetPhysicalTime method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ks.IKsReferenceClock.GetState
title: IKsReferenceClock::GetState
author: windows-driver-content
description: The IKsReferenceClock::GetState method queries the associated reference clock for its current streaming state.
old-location: stream\iksreferenceclock_getstate.htm
ms.assetid: 5a77a8bc-b477-41b3-bc4e-07c6c14291a1
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
req.alt-api: IKsReferenceClock.GetState
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
ms.keywords: IKsReferenceClock, GetState, IKsReferenceClock::GetState
req.iface: IKsReferenceClock
---

# IKsReferenceClock::GetState method



## -description
<p>The <b>IKsReferenceClock::GetState</b> method queries the associated reference clock for its current streaming state.</p>


## -syntax

````
NTSTATUS GetState(
  [out] PKSSTATE State
);
````


## -parameters
<dl>

### -param <i>State</i> [out]

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a> structure that indicates the streaming state of the underlying clock.</p>
</dd>
</dl>

## -returns
<p>The <b>IKsReferenceClock::GetState</b> method returns STATUS_SUCCESS or  the error code that the relevant clock returned from its <b>GetState</b> property. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565093">KSPROPERTY_CLOCK_STATE</a>.  May return STATUS_DEVICE_NOT_READY if no clock is assigned.</p>

## -remarks
<p>For more information, see <a href="NULL">AVStream Clocks</a>.</p>

<p>AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565093">KSPROPERTY_CLOCK_STATE</a> property to retrieve the correlated time.</p>

<p>For more information, see <a href="NULL">AVStream Clocks</a>.</p>

<p>AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565093">KSPROPERTY_CLOCK_STATE</a> property to retrieve the correlated time.</p>

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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsReferenceClock::GetState method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

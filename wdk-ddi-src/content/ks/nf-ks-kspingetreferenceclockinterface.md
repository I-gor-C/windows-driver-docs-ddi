---
UID: NF.ks.KsPinGetReferenceClockInterface
title: KsPinGetReferenceClockInterface
author: windows-driver-content
description: The KsPinGetReferenceClockInterface function returns a COM style interface to the reference clock associated with Pin. This interface pointer will be an IKsReferenceClock interface.
old-location: stream\kspingetreferenceclockinterface.htm
ms.assetid: 49c78b4e-aa3a-4c4b-8720-0302a537c84c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinGetReferenceClockInterface
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: KsPinGetReferenceClockInterface
req.iface: 
---

# KsPinGetReferenceClockInterface function



## -description
<p>The<b> KsPinGetReferenceClockInterface</b> function returns a COM style interface to the reference clock associated with <i>Pin</i>. This interface pointer will be an <b>IKsReferenceClock</b> interface.</p>


## -syntax

````
NTSTATUS KsPinGetReferenceClockInterface(
  _In_  PKSPIN             Pin,
  _Out_ PIKSREFERENCECLOCK *Interface
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure for which to return the reference clock interface.</p>
</dd>

### -param <i>Interface</i> [out]

<dd>
<p>A pointer to a memory location that receives the address of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560725">IKsReferenceClock</a> interface. This is a COM style interface with an associated reference count. Minidrivers must release the interface when finished with it.</p>
</dd>
</dl>

## -returns
<p><b>KsPinGetReferenceClockInterface</b> returns STATUS_SUCCESS and deposits the address of the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff560725">IKsReferenceClock</a> interface into <i>Interface</i> if the pin implements the clock or has received notification of the master clock through the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565713">KSPROPERTY_STREAM_MASTERCLOCK</a> property. Returns STATUS_DEVICE_NOT_READY if the pin has not yet received notification of the master clock.</p>

## -remarks
<p>The most common time to call <b>KsPinGetReferenceClockInterface</b> is in a state transition to KSSTATE_ACQUIRE.</p>

<p>See <a href="NULL">AVStream Clocks</a> for more information about using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560725">IKsReferenceClock</a> interface that this routine returns.</p>

<p>The most common time to call <b>KsPinGetReferenceClockInterface</b> is in a state transition to KSSTATE_ACQUIRE.</p>

<p>See <a href="NULL">AVStream Clocks</a> for more information about using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560725">IKsReferenceClock</a> interface that this routine returns.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563509">KsPinGetConnectedPinInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563506">KsPinGetConnectedFilterInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563528">KsPinSetPinClockTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562655">KsGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559766">IKsControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560725">IKsReferenceClock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562547">KsFilterGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566767">KsRegisterAggregatedClientUnknown</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetReferenceClockInterface function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

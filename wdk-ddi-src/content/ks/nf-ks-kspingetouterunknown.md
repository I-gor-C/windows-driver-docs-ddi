---
UID: NF.ks.KsPinGetOuterUnknown
title: KsPinGetOuterUnknown
author: windows-driver-content
description: The KsPinGetOuterUnknown function returns the outer IUnknown of the pin specified by Pin.
old-location: stream\kspingetouterunknown.htm
old-project: stream
ms.assetid: 58b14ddd-6698-487a-925d-7d559057e55d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinGetOuterUnknown
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinGetOuterUnknown
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
req.iface: 
---

# KsPinGetOuterUnknown function



## -description
<p>The<b> KsPinGetOuterUnknown</b> function returns the outer <b>IUnknown</b> of the pin specified by <i>Pin</i>.</p>


## -syntax

````
PUNKNOWN __inline KsPinGetOuterUnknown(
  _In_ PKSPIN Pin
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure for which to return the outer <b>IUnknown</b>.</p>
</dd>
</dl>

## -returns
<p><b>KsPinGetOuterUnknown</b> returns a pointer to the outer <b>IUnknown</b> interface of <i>Pin</i>. This can subsequently be used to query for other interfaces.</p>

## -remarks
<p><b>KsPinGetOuterUnknown</b> is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562655">KsGetOuterUnknown</a>. </p>

<p><b>KsPinGetOuterUnknown</b> is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562655">KsGetOuterUnknown</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562655">KsGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566767">KsRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="NULL">AVStream Overview</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562547">KsFilterGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559766">IKsControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562535">KsFilterFactoryGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561686">KsDeviceGetOuterUnknown</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetOuterUnknown function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

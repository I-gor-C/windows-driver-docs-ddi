---
UID: NF.ks.KsGetDevice
title: KsGetDevice
author: windows-driver-content
description: The KsGetDevice function returns the AVStream device structure to which Object belongs.
old-location: stream\ksgetdevice.htm
old-project: stream
ms.assetid: 27fb223f-9e6b-42af-b3d8-1018dc5416c2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGetDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetDevice
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
req.iface: 
---

# KsGetDevice function



## -description
<p>The<b> KsGetDevice</b> function returns the AVStream device structure to which <i>Object </i>belongs.</p>


## -syntax

````
PKSDEVICE KsGetDevice(
  _In_ PVOID Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>The object to query for the device to which it belongs.</p>
</dd>
</dl>

## -returns
<p><b>KsGetDevice</b> returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> structure that is the AVStream device to which <i>Object</i> belongs.</p>

## -remarks
<p><i>Object</i> should be one of: PKSPIN, PKSFILTER, or PKSFILTERFACTORY. Callers must perform appropriate typecasting to PVOID.</p>

<p>Minidrivers typically do not call this function directly. There are a number of functions that perform inline calls to <b>KsGetDevice</b> and that perform typecasting automatically: <a href="https://msdn.microsoft.com/library/windows/hardware/ff562532">KsFilterFactoryGetDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562544">KsFilterGetDevice</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563511">KsPinGetDevice</a>.</p>

<p><i>Object</i> should be one of: PKSPIN, PKSFILTER, or PKSFILTERFACTORY. Callers must perform appropriate typecasting to PVOID.</p>

<p>Minidrivers typically do not call this function directly. There are a number of functions that perform inline calls to <b>KsGetDevice</b> and that perform typecasting automatically: <a href="https://msdn.microsoft.com/library/windows/hardware/ff562532">KsFilterFactoryGetDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562544">KsFilterGetDevice</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563511">KsPinGetDevice</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562532">KsFilterFactoryGetDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562544">KsFilterGetDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563511">KsPinGetDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetDevice function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

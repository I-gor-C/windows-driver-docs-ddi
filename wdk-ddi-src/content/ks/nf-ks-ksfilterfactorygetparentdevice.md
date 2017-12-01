---
UID: NF.ks.KsFilterFactoryGetParentDevice
title: KsFilterFactoryGetParentDevice
author: windows-driver-content
description: The KsFilterFactoryGetParentDevice function returns the parent device of the given filter factory.
old-location: stream\ksfilterfactorygetparentdevice.htm
old-project: stream
ms.assetid: ac1d10dc-d3cb-4a83-9f52-34ea90d2193b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFilterFactoryGetParentDevice
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
req.alt-api: KsFilterFactoryGetParentDevice
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

# KsFilterFactoryGetParentDevice function



## -description
<p>The<b> KsFilterFactoryGetParentDevice</b> function returns the parent device of the given filter factory.</p>


## -syntax

````
PKSDEVICE __inline KsFilterFactoryGetParentDevice(
  _In_ PKSFILTERFACTORY FilterFactory
);
````


## -parameters
<dl>

### -param <i>FilterFactory</i> [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksfilterfactory.md">KSFILTERFACTORY</a> structure for which to return the parent device.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterFactoryGetParentDevice</b> returns a pointer to a <a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a> structure representing the parent device of the filter factory. This is the AVStream device to which the filter factory belongs.</p>

## -remarks
<p>This call is an inline function call to <a href="..\ks\nf-ks-ksgetparent.md">KsGetParent</a>. Note that the object hierarchy is guaranteed to be stable only while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksfilterfactory.md">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetparent.md">KsGetParent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterFactoryGetParentDevice function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

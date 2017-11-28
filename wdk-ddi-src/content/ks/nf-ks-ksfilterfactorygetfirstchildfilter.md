---
UID: NF.ks.KsFilterFactoryGetFirstChildFilter
title: KsFilterFactoryGetFirstChildFilter
author: windows-driver-content
description: The KsFilterFactoryGetFirstChildFilter function returns the first instantiated filter created by FilterFactory.
old-location: stream\ksfilterfactorygetfirstchildfilter.htm
old-project: stream
ms.assetid: 72eb23aa-4f0e-4ef5-baee-c0735253684e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterFactoryGetFirstChildFilter
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
req.alt-api: KsFilterFactoryGetFirstChildFilter
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

# KsFilterFactoryGetFirstChildFilter function



## -description
<p>The<b> KsFilterFactoryGetFirstChildFilter</b> function returns the first instantiated filter created by <i>FilterFactory</i>.</p>


## -syntax

````
PKSFILTER __inline KsFilterFactoryGetFirstChildFilter(
  _In_ PKSFILTERFACTORY FilterFactory
);
````


## -parameters
<dl>

### -param <i>FilterFactory</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a> structure for which to find the first instantiated child filter.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterFactoryGetFirstChildFilter</b> returns a pointer to the first instantiated <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure created by <i>FilterFactory</i>. If there are no instantiated filters created by <i>FilterFactory</i>, <b>NULL</b> is returned.</p>

## -remarks
<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562626">KsGetFirstChild</a>. Note that the object hierarchy is guaranteed to be stable only while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562626">KsGetFirstChild</a>. Note that the object hierarchy is guaranteed to be stable only while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562626">KsGetFirstChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562546">KsFilterGetNextSiblingFilter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterFactoryGetFirstChildFilter function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ks.KsGetNextSibling
title: KsGetNextSibling
author: windows-driver-content
description: The KsGetNextSibling function returns the next sibling of a given object.
old-location: stream\ksgetnextsibling.htm
old-project: stream
ms.assetid: 509cf778-2b0c-4dd2-982d-0c7be95ad407
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGetNextSibling
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
req.alt-api: KsGetNextSibling
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

# KsGetNextSibling function



## -description
<p>The<b> KsGetNextSibling </b>function returns the next sibling of a given object.</p>


## -syntax

````
PVOID KsGetNextSibling(
  _In_ PVOID Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>The object for which to find the next sibling.</p>
</dd>
</dl>

## -returns
<p><b>KsGetNextSibling</b> returns the next sibling object of <i>Object</i>. If no such sibling object exists, it returns <b>NULL</b>.</p>

## -remarks
<p>If <i>Object</i> is a filter factory, <b>KsGetNextSibling </b>returns the next filter factory belonging to the parent device, and so on. Callers must perform appropriate typecasting to and from PVOID.</p>

<p>The object hierarchy is guaranteed stable only while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">AVStream Overview</a> and <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Minidrivers rarely call <b>KsGetNextSibling</b> directly. There are a number of functions that are inline calls to <b>KsGetNextSibling</b> and that perform the typecasting for you: <a href="https://msdn.microsoft.com/library/windows/hardware/ff562534">KsFilterFactoryGetNextSiblingFilterFactory</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562546">KsFilterGetNextSiblingFilter</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563514">KsPinGetNextSiblingPin</a>.</p>

<p>If <i>Object</i> is a filter factory, <b>KsGetNextSibling </b>returns the next filter factory belonging to the parent device, and so on. Callers must perform appropriate typecasting to and from PVOID.</p>

<p>The object hierarchy is guaranteed stable only while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">AVStream Overview</a> and <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Minidrivers rarely call <b>KsGetNextSibling</b> directly. There are a number of functions that are inline calls to <b>KsGetNextSibling</b> and that perform the typecasting for you: <a href="https://msdn.microsoft.com/library/windows/hardware/ff562534">KsFilterFactoryGetNextSiblingFilterFactory</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562546">KsFilterGetNextSiblingFilter</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563514">KsPinGetNextSiblingPin</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562534">KsFilterFactoryGetNextSiblingFilterFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562546">KsFilterGetNextSiblingFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563514">KsPinGetNextSiblingPin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetNextSibling function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

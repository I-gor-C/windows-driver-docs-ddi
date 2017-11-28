---
UID: NF.ks.KsFilterGetNextSiblingFilter
title: KsFilterGetNextSiblingFilter
author: windows-driver-content
description: The KsFilterGetNextSiblingFilter function returns the next instantiated filter belonging to the parent filter factory of Filter.
old-location: stream\ksfiltergetnextsiblingfilter.htm
old-project: stream
ms.assetid: 0b0a306a-6066-4a7d-ae2d-12eb8bb3adc0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterGetNextSiblingFilter
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
req.alt-api: KsFilterGetNextSiblingFilter
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

# KsFilterGetNextSiblingFilter function



## -description
<p>The<b> KsFilterGetNextSiblingFilter</b> function returns the next instantiated filter belonging to the parent filter factory of <i>Filter</i>.</p>


## -syntax

````
PKSFILTER __inline KsFilterGetNextSiblingFilter(
  _In_ PKSFILTER Filter
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure for which to find the next sibling filter.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterGetNextSiblingFilter</b> returns a pointer to the next sibling <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure of <i>Filter</i>. If no such instantiated filter exists, it returns <b>NULL</b>.</p>

## -remarks
<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562643">KsGetNextSibling</a>. Note that the object hierarchy is only guaranteed stable while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562643">KsGetNextSibling</a>. Note that the object hierarchy is only guaranteed stable while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562533">KsFilterFactoryGetFirstChildFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562643">KsGetNextSibling</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterGetNextSiblingFilter function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

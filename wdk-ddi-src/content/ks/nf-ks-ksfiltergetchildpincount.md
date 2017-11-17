---
UID: NF.ks.KsFilterGetChildPinCount
title: KsFilterGetChildPinCount
author: windows-driver-content
description: The KsFilterGetChildPinCountfunctionreturns the number of pins of a given type that are currently instantiated on a given filter.
old-location: stream\ksfiltergetchildpincount.htm
ms.assetid: 29e78bc3-0dc2-4e76-b683-c1e9a2d454d4
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
req.alt-api: KsFilterGetChildPinCount
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
ms.keywords: KsFilterGetChildPinCount
req.iface: 
---

# KsFilterGetChildPinCount function



## -description
<p>The<b> KsFilterGetChildPinCount</b><b></b>function<b></b>returns the number of pins of a given type that are currently instantiated on a given filter.</p>


## -syntax

````
ULONG KsFilterGetChildPinCount(
  _In_ PKSFILTER Filter,
  _In_ ULONG     PinId
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure for which to find the number of instantiated pins of type <i>PinID</i>.</p>
</dd>

### -param <i>PinId</i> [in]

<dd>
<p>The pin type for which to find the number of instantiated pins. <i>PinID</i> is an index into the array of pin descriptors for the filter to which the pin belongs.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterGetChildPinCount</b> returns the number of pins of type <i>PinID</i> that are currently instantiated on <i>Filter</i>. If no such pins exist or if <i>PinID</i> is out of range, zero is returned.</p>

## -remarks
<p>The count returned by this call is guaranteed to be correct only if the function is called while the filter control mutex is held. The count remains correct after the call as long as this mutex continues to be held. As soon as the mutex is released, other pins can be added or removed, thereby altering the actual pin count.</p>

<p>For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>The count returned by this call is guaranteed to be correct only if the function is called while the filter control mutex is held. The count remains correct after the call as long as this mutex continues to be held. As soon as the mutex is released, other pins can be added or removed, thereby altering the actual pin count.</p>

<p>For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562545">KsFilterGetFirstChildPin</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563514">KsPinGetNextSiblingPin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterGetChildPinCount function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ks.KsFilterGetFirstChildPin
title: KsFilterGetFirstChildPin
author: windows-driver-content
description: The KsFilterGetFirstChildPin function returns the first instantiated pin of type PinID on the filter specified by Filter.
old-location: stream\ksfiltergetfirstchildpin.htm
old-project: stream
ms.assetid: b026908a-51d4-45a8-9c0e-1c163563bfbf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterGetFirstChildPin
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
req.alt-api: KsFilterGetFirstChildPin
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

# KsFilterGetFirstChildPin function



## -description
<p>The<b> KsFilterGetFirstChildPin</b> function returns the first instantiated pin of type <i>PinID</i> on the filter specified by <i>Filter</i>.</p>


## -syntax

````
PKSPIN KsFilterGetFirstChildPin(
  _In_ PKSFILTER Filter,
  _In_ ULONG     PinId
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure to query for instantiated pins.</p>
</dd>

### -param <i>PinId</i> [in]

<dd>
<p>The numeric ID of the pin type for which to find the first instantiated member.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterGetFirstChildPin</b> returns a pointer to the first instantiated <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure of type <i>PinID</i> on the specified filter.</p>

## -remarks
<p>Note that the object hierarchy is guaranteed stable only while the appropriate mutex is held, in this case the filter control mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Note that the object hierarchy is guaranteed stable only while the appropriate mutex is held, in this case the filter control mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562543">KsFilterGetChildPinCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563514">KsPinGetNextSiblingPin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterGetFirstChildPin function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

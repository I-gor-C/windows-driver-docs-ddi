---
UID: NF.ks.KsFilterGetAndGate
title: KsFilterGetAndGate
author: windows-driver-content
description: The KsFilterGetAndGate function returns Filter's AND gate.
old-location: stream\ksfiltergetandgate.htm
old-project: stream
ms.assetid: b5f7c4ed-0596-4e88-b987-fd454e4b4971
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFilterGetAndGate
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
req.alt-api: KsFilterGetAndGate
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
req.irql: 
req.iface: 
---

# KsFilterGetAndGate function



## -description
<p>The<b> KsFilterGetAndGate </b>function returns <i>Filter</i>'s AND gate.</p>


## -syntax

````
PKSGATE KsFilterGetAndGate(
  _In_ PKSFILTER Filter
);
````


## -parameters
<dl>

### -param Filter [in]

<dd>
<p>A pointer to the <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> structure for which to acquire the corresponding AND gate.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterGetAndGate</b> returns <i>Filter</i>'s AND gate as a pointer to a <a href="..\ks\ns-ks--ksgate.md">KSGATE</a> structure.</p>

## -remarks
<p>A minidriver can use AND gates on a filter as a processing control mechanism for that filter.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksgate.md">KSGATE</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgatecapturethreshold.md">KsGateCaptureThreshold</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgateturninputon.md">KsGateTurnInputOn</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgateturninputoff.md">KsGateTurnInputOff</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinattachandgate.md">KsPinAttachAndGate</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingetandgate.md">KsPinGetAndGate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterGetAndGate function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

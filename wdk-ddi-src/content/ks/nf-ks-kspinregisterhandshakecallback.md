---
UID: NF.ks.KsPinRegisterHandshakeCallback
title: KsPinRegisterHandshakeCallback
author: windows-driver-content
description: The KsPinRegisterHandshakeCallback function registers a minidriver-provided callback routine for a given pin.
old-location: stream\kspinregisterhandshakecallback.htm
old-project: stream
ms.assetid: a5b9f731-e029-40c2-9fbb-d7a3b63615df
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinRegisterHandshakeCallback
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
req.alt-api: KsPinRegisterHandshakeCallback
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

# KsPinRegisterHandshakeCallback function



## -description
<p>The<b> KsPinRegisterHandshakeCallback</b> function registers a minidriver-provided callback routine for a given pin. AVStream calls the callback routine when it receives a handshake request for the pin that specifies a protocol that AVStream does not handle by default. </p>


## -syntax

````
void KsPinRegisterHandshakeCallback(
  _In_ PKSPIN            Pin,
  _In_ PFNKSPINHANDSHAKE Handshake
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="..\ks\ns-ks--kspin.md">KSPIN</a> structure for which to register a handshake callback.</p>
</dd>

### -param <i>Handshake</i> [in]

<dd>
<dl>
<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinhandshake">AVStrMiniPinHandshake</a> routine to be called when AVStream receives a protocol handshake request on <i>Pin</i> that it does not handle.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Pins that support private protocol connections with other AVStream pins should register a handshake callback.</p>

<p>Minidrivers that support private protocols between a given pin and another AVStream pin should call this routine as soon as possible to register a callback. Then if another pin requests a handshake, the minidriver can return the request. </p>

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
<a href="..\ks\nf-ks-kspinhandshake.md">KsPinHandshake</a>
</dt>
<dt>
<a href="stream.kshandshake">KSHANDSHAKE</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilterregisterpowercallbacks.md">KsFilterRegisterPowerCallbacks</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinregisterpowercallbacks.md">KsPinRegisterPowerCallbacks</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksregisteraggregatedclientunknown.md">KsRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="stream.avstrminipinhandshake">AVStrMiniPinHandshake</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinRegisterHandshakeCallback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ks.KsRegisterAggregatedClientUnknown
title: KsRegisterAggregatedClientUnknown
author: windows-driver-content
description: In a manner very similar to COM, the KsRegisterAggregatedClientUnknown function aggregates two objects: the specified AVStream object and a client unknown object.
old-location: stream\ksregisteraggregatedclientunknown.htm
old-project: stream
ms.assetid: b0e18e39-2435-4823-aab4-ba52d218294a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsRegisterAggregatedClientUnknown
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
req.alt-api: KsRegisterAggregatedClientUnknown
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

# KsRegisterAggregatedClientUnknown function



## -description
<p>In a manner very similar to COM, the <b>KsRegisterAggregatedClientUnknown</b> function aggregates two objects: the specified AVStream object and a client unknown object.</p>


## -syntax

````
PUNKNOWN KsRegisterAggregatedClientUnknown(
  _In_ PVOID    Object,
  _In_ PUNKNOWN ClientUnknown
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A pointer to the AVStream object to become the outer unknown interface.</p>
</dd>

### -param <i>ClientUnknown</i> [in]

<dd>
<p>A pointer to an <b>IUnknown</b> interface.</p>
</dd>
</dl>

## -returns
<p>Returns the newly created aggregate object.</p>

## -remarks
<p>The client unknown becomes the inner part of the aggregate object, and the AVStream object becomes the outer unknown. When an interface is queried that AVStream does not handle, AVStream passes the query is to the inner aggregate.</p>

<p>If a client unknown is already aggregated on the AVStream object, AVStream releases the previously registered aggregate and uses the unknown passed to <b>KsRegisterAggregatedClientUnknown</b> as the new inner unknown.</p>

<p>There are four wrappers to <b>KsRegisterAggregatedClientUnknown</b> that perform typecasts.</p>

<p>Minidrivers do not need to be running in a C++ environment to use this function.</p>

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
<a href="..\ks\nf-ks-ksdeviceregisteraggregatedclientunknown.md">KsDeviceRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilterfactoryregisteraggregatedclientunknown.md">KsFilterFactoryRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilterregisteraggregatedclientunknown.md">KsFilterRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinregisteraggregatedclientunknown.md">KsPinRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetouterunknown.md">KsGetOuterUnknown</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsRegisterAggregatedClientUnknown function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

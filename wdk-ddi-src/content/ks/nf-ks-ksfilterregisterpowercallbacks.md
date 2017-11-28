---
UID: NF.ks.KsFilterRegisterPowerCallbacks
title: KsFilterRegisterPowerCallbacks
author: windows-driver-content
description: The KsFilterRegisterPowerCallbacks function registers power management callbacks for Filter.
old-location: stream\ksfilterregisterpowercallbacks.htm
old-project: stream
ms.assetid: 9b4a7932-7371-48d2-95fb-1c3e3ca170be
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterRegisterPowerCallbacks
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
req.alt-api: KsFilterRegisterPowerCallbacks
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

# KsFilterRegisterPowerCallbacks function



## -description
<p>The<b> KsFilterRegisterPowerCallbacks </b>function registers power management callbacks for <i>Filter</i>.</p>


## -syntax

````
void KsFilterRegisterPowerCallbacks(
  _In_     PKSFILTER        Filter,
  _In_opt_ PFNKSFILTERPOWER Sleep,
  _In_opt_ PFNKSFILTERPOWER Wake
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure for which to register power callbacks. In order to receive power notification messages, <i>Filter</i> must be filter-centric.</p>
</dd>

### -param <i>Sleep</i> [in, optional]

<dd>
<p>A pointer to a function that handles sleep requests for the device. If <b>NULL</b>, no sleep callback is registered. For more information, see the Remarks section below.</p>
</dd>

### -param <i>Wake</i> [in, optional]

<dd>
<p>A pointer to a function that handles wake requests for the device. If <b>NULL</b>, no wake callback is specified. For more information, see the Remarks section below.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The two callbacks should be prototyped as follows:</p>

<p>The <i>Sleep</i> callback is made if <i>Filter</i> is a filter-centric filter and the device is going to sleep. The <i>Wake</i> callback is made if <i>Filter</i> is a filter-centric filter and the device is waking.</p>

<p>For information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543162">Device Power States</a>. </p>

<p>Also see <a href="NULL">Initializing an AVStream Minidriver</a> and <a href="NULL">Filter-Centric Processing</a>.</p>

<p>The two callbacks should be prototyped as follows:</p>

<p>The <i>Sleep</i> callback is made if <i>Filter</i> is a filter-centric filter and the device is going to sleep. The <i>Wake</i> callback is made if <i>Filter</i> is a filter-centric filter and the device is waking.</p>

<p>For information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543162">Device Power States</a>. </p>

<p>Also see <a href="NULL">Initializing an AVStream Minidriver</a> and <a href="NULL">Filter-Centric Processing</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563525">KsPinRegisterPowerCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterRegisterPowerCallbacks function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

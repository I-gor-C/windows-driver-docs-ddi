---
UID: NF.ks.KsPinRegisterPowerCallbacks
title: KsPinRegisterPowerCallbacks
author: windows-driver-content
description: The KsPinRegisterPowerCallbacks function registers power management callbacks for Pin.
old-location: stream\kspinregisterpowercallbacks.htm
ms.assetid: e498a907-8d20-4d00-9411-8e82030af223
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
req.alt-api: KsPinRegisterPowerCallbacks
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
ms.keywords: KsPinRegisterPowerCallbacks
req.iface: 
---

# KsPinRegisterPowerCallbacks function



## -description
<p>The<b> KsPinRegisterPowerCallbacks </b>function registers power management callbacks for <i>Pin</i>.</p>


## -syntax

````
void KsPinRegisterPowerCallbacks(
  _In_     PKSPIN        Pin,
  _In_opt_ PFNKSPINPOWER Sleep,
  _In_opt_ PFNKSPINPOWER Wake
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure for which to register power callbacks. Note that the pin must actually process (be pin-centric) in order to receive power notification messages.</p>
</dd>

### -param <i>Sleep</i> [in, optional]

<dd>
<p>This parameter supplies the address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556345">AVStrMiniPinPower</a>  function that handles sleep requests for the device. Optional.</p>
</dd>

### -param <i>Wake</i> [in, optional]

<dd>
<p>This parameter supplies the address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556345">AVStrMiniPinPower</a>  function that handles wake requests for the device. Optional.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>At least one of the callbacks must be specified when calling <b>KsPinRegisterPowerCallbacks</b>.</p>

<p>At least one of the callbacks must be specified when calling <b>KsPinRegisterPowerCallbacks</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562550">KsFilterRegisterPowerCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556345">AVStrMiniPinPower</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinRegisterPowerCallbacks function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

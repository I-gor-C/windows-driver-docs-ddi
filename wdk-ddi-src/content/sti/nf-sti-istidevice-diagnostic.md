---
UID: NF.sti.IStiDevice.Diagnostic
title: IStiDevice::Diagnostic
author: windows-driver-content
description: The IStiDevice::Diagnostic method executes diagnostic tests on a still image device.
old-location: image\istidevice_diagnostic.htm
old-project: image
ms.assetid: eee5c6d7-17a3-461f-85e0-17f6b7114b19
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, Diagnostic, IStiDevice::Diagnostic
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sti.h
req.include-header: Sti.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDevice.Diagnostic
req.alt-loc: sti.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IStiDevice
req.product: Windows 10 or later.
---

# IStiDevice::Diagnostic method



## -description
<p>The <b>IStiDevice::Diagnostic</b> method executes diagnostic tests on a still image device.</p>


## -syntax

````
HRESULT Diagnostic(
  [in, out] LPSTI_DIAG pBuffer
);
````


## -parameters
<dl>

### -param <i>pBuffer</i> [in, out]

<dd>
<p>Caller-supplied pointer to an <a href="..\sti\ns-sti--sti-diag.md">STI_DIAG</a> structure specifying the type of tests to be run. On return, the structure contains status information.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::Diagnostic</b> method calls <a href="image.istiusd_diagnostic">IStiUSD::Diagnostic</a>, which is exported by vendor-supplied minidrivers. The Scanners and Cameras Control Panel calls <b>IStiDevice::Diagnostic</b> when a user presses the Test button.</p>

<p>Before calling <b>IStiDevice::Diagnostic</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::Diagnostic</b> must be preceded by a call to <a href="image.istidevice_lockdevice">IStiDevice::LockDevice</a> and followed by a call to <a href="image.istidevice_unlockdevice">IStiDevice::UnLockDevice</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>
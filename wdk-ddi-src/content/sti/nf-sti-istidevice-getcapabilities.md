---
UID: NF.sti.IStiDevice.GetCapabilities
title: IStiDevice::GetCapabilities
author: windows-driver-content
description: The IStiDevice::GetCapabilities method returns a still image device's capabilities.
old-location: image\istidevice_getcapabilities.htm
old-project: image
ms.assetid: 4c5d8834-a78d-443e-bfec-1d9fcddb9331
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, GetCapabilities, IStiDevice::GetCapabilities
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
req.alt-api: IStiDevice.GetCapabilities
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

# IStiDevice::GetCapabilities method



## -description
<p>The <b>IStiDevice::GetCapabilities</b> method returns a still image device's capabilities.</p>


## -syntax

````
HRESULT GetCapabilities(
  [in, out] PSTI_DEV_CAPS pDevCaps
);
````


## -parameters
<dl>

### -param <i>pDevCaps</i> [in, out]

<dd>
<p>Caller-supplied pointer to an empty <a href="..\sti\ns-sti--sti-dev-caps.md">STI_DEV_CAPS</a> structure.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::GetCapabilities</b> method returns device capability flags in the caller-supplied <a href="..\sti\ns-sti--sti-dev-caps.md">STI_DEV_CAPS</a> structure.</p>

<p>Before calling <b>IStiDevice::GetCapabilities</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

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
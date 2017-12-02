---
UID: NF.sti.IStiDevice.GetLastError
title: IStiDevice::GetLastError
author: windows-driver-content
description: The IStiDevice::GetLastError method returns the last known error associated with a still image device.
old-location: image\istidevice_getlasterror.htm
old-project: image
ms.assetid: 20ad609d-454a-4d43-a58e-184cbb8e8da7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IStiDevice, GetLastError, IStiDevice::GetLastError
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
req.alt-api: IStiDevice.GetLastError
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

# IStiDevice::GetLastError method



## -description
<p>The <b>IStiDevice::GetLastError</b> method returns the last known error associated with a still image device.</p>


## -syntax

````
HRESULT GetLastError(
  [out] LPDWORD pdwLastDeviceError
);
````


## -parameters
<dl>

### -param pdwLastDeviceError [out]

<dd>
<p>Caller-supplied pointer to a buffer in which the error code will be stored.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>Before calling IStiDevice::GetLastError, clients of the IStiDevice COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an IStiDevice interface pointer, which provides access to a specified device.</p>

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
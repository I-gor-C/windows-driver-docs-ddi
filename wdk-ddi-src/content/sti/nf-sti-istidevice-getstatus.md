---
UID: NF.sti.IStiDevice.GetStatus
title: IStiDevice::GetStatus
author: windows-driver-content
description: The IStiDevice::GetStatus method returns a still image device's status information.
old-location: image\istidevice_getstatus.htm
old-project: image
ms.assetid: e9539565-e13f-42ea-9566-066e2c9ae2ae
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IStiDevice, GetStatus, IStiDevice::GetStatus
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
req.alt-api: IStiDevice.GetStatus
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

# IStiDevice::GetStatus method



## -description
<p>The <b>IStiDevice::GetStatus</b> method returns a still image device's status information.</p>


## -syntax

````
HRESULT GetStatus(
  [in, out] PSTI_DEVICE_STATUS pDevStatus
);
````


## -parameters
<dl>

### -param pDevStatus [in, out]

<dd>
<p>Caller-supplied pointer to an <a href="..\sti\ns-sti--sti-device-status.md">STI_DEVICE_STATUS</a> structure. The caller must set the <b>dwSize</b> and <b>StatusMask</b> members.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::GetStatus</b> method returns device status information in the caller-supplied <a href="..\sti\ns-sti--sti-device-status.md">STI_DEVICE_STATUS</a> structure. It obtains the status by calling <a href="image.istiusd_getstatus">IStiUSD::GetStatus</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::GetStatus</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::GetStatus</b> must be preceded by a call to <a href="image.istidevice_lockdevice">IStiDevice::LockDevice</a> and followed by a call to <a href="image.istidevice_unlockdevice">IStiDevice::UnLockDevice</a>.</p>

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
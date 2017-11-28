---
UID: NF.sti.IStiDevice.DeviceReset
title: IStiDevice::DeviceReset
author: windows-driver-content
description: The IStiDevice::DeviceReset method resets a still image device to a known state.
old-location: image\istidevice_devicereset.htm
old-project: image
ms.assetid: 8a52c452-9a80-45d5-9bc8-85e17654eb6a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, DeviceReset, IStiDevice::DeviceReset
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
req.alt-api: IStiDevice.DeviceReset
req.alt-loc: Sti.h
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

# IStiDevice::DeviceReset method



## -description
<p>The <b>IStiDevice::DeviceReset</b> method resets a still image device to a known state.</p>


## -syntax

````
HRESULT DeviceReset();
````


## -parameters


## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::DeviceReset</b> method resets the device by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543812">IStiUSD::DeviceReset</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::DeviceReset</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::DeviceReset</b> must be preceded by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a> and followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543770">IStiDevice::UnLockDevice</a>.</p>

<p>The <b>IStiDevice::DeviceReset</b> method resets the device by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543812">IStiUSD::DeviceReset</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::DeviceReset</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::DeviceReset</b> must be preceded by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a> and followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543770">IStiDevice::UnLockDevice</a>.</p>

<p>The <b>IStiDevice::DeviceReset</b> method resets the device by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543812">IStiUSD::DeviceReset</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::DeviceReset</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::DeviceReset</b> must be preceded by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a> and followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543770">IStiDevice::UnLockDevice</a>.</p>

<p>The <b>IStiDevice::DeviceReset</b> method resets the device by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543812">IStiUSD::DeviceReset</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::DeviceReset</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::DeviceReset</b> must be preceded by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a> and followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543770">IStiDevice::UnLockDevice</a>.</p>

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
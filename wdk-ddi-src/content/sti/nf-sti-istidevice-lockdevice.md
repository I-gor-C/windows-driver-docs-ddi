---
UID: NF.sti.IStiDevice.LockDevice
title: IStiDevice::LockDevice method
author: windows-driver-content
description: The IStiDevice::LockDevice method locks a device for exclusive use by the caller.
old-location: image\istidevice_lockdevice.htm
old-project: Image
ms.assetid: 208d9dc3-736b-4684-b8d3-802f6df78142
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IStiDevice, IStiDevice::LockDevice, LockDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: sti.h
req.include-header: Sti.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDevice.LockDevice
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
req.product: Windows 10 or later.
---

# IStiDevice::LockDevice method



## -description
The <b>IStiDevice::LockDevice </b>method locks a device for exclusive use by the caller.



## -syntax

````
HRESULT LockDevice(
  [in] DWORD dwTimeOut
);
````


## -parameters

### -param dwTimeOut [in]

Caller-supplied time-out value, in milliseconds. If the lock is not obtained in this time period, an error is returned.


## -returns
If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.


## -remarks
Clients of the <b>IStiDevice</b> COM interface must call <b>IStiDevice::LockDevice</b> before calling the following methods:


<a href="image.istidevice_devicereset">IStiDevice::DeviceReset</a>



<a href="image.istidevice_diagnostic">IStiDevice::Diagnostic</a>



<a href="image.istidevice_escape">IStiDevice::Escape</a>



<a href="image.istidevice_getstatus">IStiDevice::GetStatus</a>



<a href="image.istidevice_rawreadcommand">IStiDevice::RawReadCommand</a>



<a href="image.istidevice_rawreaddata">IStiDevice::RawReadData</a>



<a href="image.istidevice_rawwritecommand">IStiDevice::RawWriteCommand</a>



<a href="image.istidevice_rawwritedata">IStiDevice::RawWriteData</a>


If the <b>IStiDevice::LockDevice</b> method is able to obtain an <b>IStiDevice</b>-level lock on the device within the specified time-out period, it then calls <a href="image.istiusd_lockdevice">IStiUSD::LockDevice</a> in the appropriate vendor-supplied minidriver.

Each call to <b>IStiDevice::LockDevice</b> must be paired with a call to <a href="image.istidevice_unlockdevice">IStiDevice::UnLockDevice</a>.

Before calling <b>IStiDevice::LockDevice</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>
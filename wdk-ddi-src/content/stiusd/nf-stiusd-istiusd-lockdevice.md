---
UID: NF.stiusd.IStiUSD.LockDevice
title: IStiUSD::LockDevice
author: windows-driver-content
description: A still image minidriver's IStiUSD::LockDevice method locks a device for exclusive use by the caller.
old-location: image\istiusd_lockdevice.htm
ms.assetid: cb91ef14-53d7-42fa-b3e5-54eb3b0925b8
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiUSD.LockDevice
req.alt-loc: Stiusd.h
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
ms.keywords: IStiUSD, LockDevice, IStiUSD::LockDevice
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# IStiUSD::LockDevice method



## -description
<p>A still image minidriver's <b>IStiUSD::LockDevice</b> method locks a device for exclusive use by the caller.</p>


## -syntax

````
STDMETHODIMP LockDevice();
````


## -parameters


## -returns
<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>If you are writing a driver for a device connected to a serial port, you might want to call <a href="fs.createfile">CreateFile</a> from within the driver's <b>IStiUSD::LockDevice</b> method if the device was opened in status mode. This will prohibit other applications from using the port (which might be supporting other devices) while status information is being obtained. For more information, see <a href="NULL">Transfer Modes</a>.</p>

<p>If you are writing a driver for a device connected to a serial port, you might want to call <a href="fs.createfile">CreateFile</a> from within the driver's <b>IStiUSD::LockDevice</b> method if the device was opened in status mode. This will prohibit other applications from using the port (which might be supporting other devices) while status information is being obtained. For more information, see <a href="NULL">Transfer Modes</a>.</p>

<p>If you are writing a driver for a device connected to a serial port, you might want to call <a href="fs.createfile">CreateFile</a> from within the driver's <b>IStiUSD::LockDevice</b> method if the device was opened in status mode. This will prohibit other applications from using the port (which might be supporting other devices) while status information is being obtained. For more information, see <a href="NULL">Transfer Modes</a>.</p>

<p>If you are writing a driver for a device connected to a serial port, you might want to call <a href="fs.createfile">CreateFile</a> from within the driver's <b>IStiUSD::LockDevice</b> method if the device was opened in status mode. This will prohibit other applications from using the port (which might be supporting other devices) while status information is being obtained. For more information, see <a href="NULL">Transfer Modes</a>.</p>

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
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiUSD::LockDevice method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.sti.IStiDevice.RawReadData
title: IStiDevice::RawReadData
author: windows-driver-content
description: The IStiDevice::RawReadData method reads data from a still image device.
old-location: image\istidevice_rawreaddata.htm
old-project: image
ms.assetid: b4510fac-839b-4744-9525-2bf96c5c724e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, RawReadData, IStiDevice::RawReadData
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
req.alt-api: IStiDevice.RawReadData
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

# IStiDevice::RawReadData method



## -description
<p>The <b>IStiDevice::RawReadData</b> method reads data from a still image device.</p>


## -syntax

````
HRESULT RawReadData(
  [in, out]      LPVOID       lpBuffer,
  [in, out]      LPDWORD      lpdwNumberOfBytes,
  [in, optional] LPOVERLAPPED lpOverlapped
);
````


## -parameters
<dl>

### -param <i>lpBuffer</i> [in, out]

<dd>
<p>Caller-supplied pointer to a buffer to receive data read from the device.</p>
</dd>

### -param <i>lpdwNumberOfBytes</i> [in, out]

<dd>
<p>Caller-supplied pointer to a DWORD. The caller must load the DWORD with the number of bytes in the buffer pointed to by <i>lpBuffer</i>. On return, it will contain the number of bytes actually read.</p>
</dd>

### -param <i>lpOverlapped</i> [in, optional]

<dd>
<p>Optional, caller-supplied pointer to an OVERLAPPED structure (described in the Microsoft Windows SDK documentation).</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::RawReadData</b> method calls <a href="image.istiusd_rawreaddata">IStiUSD::RawReadData</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::RawReadData</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::RawReadData</b> must be preceded by a call to <a href="image.istidevice_lockdevice">IStiDevice::LockDevice</a> and followed by a call to <a href="image.istidevice_unlockdevice">IStiDevice::UnLockDevice</a>.</p>

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

## -see-also
<dl>
<dt>
<a href="image.istidevice_rawreadcommand">IStiDevice::RawReadCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiDevice::RawReadData method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

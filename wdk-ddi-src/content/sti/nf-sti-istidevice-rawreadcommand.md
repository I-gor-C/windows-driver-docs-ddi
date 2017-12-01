---
UID: NF.sti.IStiDevice.RawReadCommand
title: IStiDevice::RawReadCommand
author: windows-driver-content
description: The IStiDevice::RawReadCommand method reads command information from a still image device.
old-location: image\istidevice_rawreadcommand.htm
old-project: image
ms.assetid: fc6b46af-d3e3-4a49-a354-c0effee6a005
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, RawReadCommand, IStiDevice::RawReadCommand
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
req.alt-api: IStiDevice.RawReadCommand
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

# IStiDevice::RawReadCommand method



## -description
<p>The <b>IStiDevice::RawReadCommand</b> method reads command information from a still image device.</p>


## -syntax

````
HRESULT RawReadCommand(
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
<p>The <b>IStiDevice::RawReadCommand</b> method calls <a href="image.istiusd_rawreadcommand">IStiUSD::RawReadCommand</a>, which is exported by vendor-supplied minidrivers. The meaning of buffer contents are vendor-defined.</p>

<p>It is only necessary to call <b>IStiDevice::RawReadCommand</b> if command and data information are read from a device by different methods. For other devices, <a href="image.istidevice_rawreaddata">IStiDevice::RawReadData</a> can be used for both commands and data.</p>

<p>Before calling <b>IStiDevice::RawReadCommand</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::RawReadCommand</b> must be preceded by a call to <a href="image.istidevice_lockdevice">IStiDevice::LockDevice</a> and followed by a call to <a href="image.istidevice_unlockdevice">IStiDevice::UnLockDevice</a>.</p>

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
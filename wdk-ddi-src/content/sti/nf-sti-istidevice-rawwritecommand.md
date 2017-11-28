---
UID: NF.sti.IStiDevice.RawWriteCommand
title: IStiDevice::RawWriteCommand
author: windows-driver-content
description: The IStiDevice::RawWriteCommand method sends command information to a still image device.
old-location: image\istidevice_rawwritecommand.htm
old-project: image
ms.assetid: 6260fd33-96b3-43d7-a7eb-35322247076b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, RawWriteCommand, IStiDevice::RawWriteCommand
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
req.alt-api: IStiDevice.RawWriteCommand
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

# IStiDevice::RawWriteCommand method



## -description
<p>The <b>IStiDevice::RawWriteCommand</b> method sends command information to a still image device.</p>


## -syntax

````
HRESULT RawWriteCommand(
  [in]           LPVOID       lpBuffer,
                 DWORD        nNumberOfBytes,
  [in, optional] LPOVERLAPPED lpOverlapped
);
````


## -parameters
<dl>

### -param <i>lpBuffer</i> [in]

<dd>
<p>Caller-supplied pointer to a buffer containing data to be sent to the device.</p>
</dd>

### -param <i>nNumberOfBytes</i> 

<dd>
<p>Caller-supplied number of bytes to be written. This is the number of bytes in the buffer pointed to by <i>lpBuffer</i>.</p>
</dd>

### -param <i>lpOverlapped</i> [in, optional]

<dd>
<p>Optional, caller-supplied pointer to an OVERLAPPED structure (described in the Microsoft Windows SDK documentation).</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::RawWriteCommand</b> method calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff543836">IStiUSD::RawWriteCommand</a>, which is exported by vendor-supplied minidrivers. The meaning of buffer contents are vendor-defined.</p>

<p>It is only necessary to call <b>IStiDevice::RawWriteCommand</b> if commands and data are written to a device by different methods. For other devices, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543764">IStiDevice::RawWriteData</a> can be used for both commands and data.</p>

<p>Before calling <b>IStiDevice::RawWriteCommand</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::RawWriteCommand</b> must be preceded by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a> and followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543770">IStiDevice::UnLockDevice</a>.</p>

<p>The <b>IStiDevice::RawWriteCommand</b> method calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff543836">IStiUSD::RawWriteCommand</a>, which is exported by vendor-supplied minidrivers. The meaning of buffer contents are vendor-defined.</p>

<p>It is only necessary to call <b>IStiDevice::RawWriteCommand</b> if commands and data are written to a device by different methods. For other devices, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543764">IStiDevice::RawWriteData</a> can be used for both commands and data.</p>

<p>Before calling <b>IStiDevice::RawWriteCommand</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>A call to <b>IStiDevice::RawWriteCommand</b> must be preceded by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543756">IStiDevice::LockDevice</a> and followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543770">IStiDevice::UnLockDevice</a>.</p>

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
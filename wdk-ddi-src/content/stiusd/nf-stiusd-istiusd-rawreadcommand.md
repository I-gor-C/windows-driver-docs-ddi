---
UID: NF.stiusd.IStiUSD.RawReadCommand
title: IStiUSD::RawReadCommand
author: windows-driver-content
description: A still image minidriver's IStiUSD::RawReadCommand method reads command information from a still image device.
old-location: image\istiusd_rawreadcommand.htm
old-project: image
ms.assetid: 603f8b76-eb3b-41aa-932c-322f5405a29b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiUSD, RawReadCommand, IStiUSD::RawReadCommand
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiUSD.RawReadCommand
req.alt-loc: stiusd.h
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
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# IStiUSD::RawReadCommand method



## -description
<p>A still image minidriver's <b>IStiUSD::RawReadCommand</b> method reads command information from a still image device.</p>


## -syntax

````
HRESULT RawReadCommand(
   LPVOID       lpBuffer,
   LPDWORD      lpdwNumberOfBytes,
   LPOVERLAPPED lpOverlapped
);
````


## -parameters
<dl>

### -param <i>lpBuffer</i> 

<dd>
<p>Caller-supplied pointer to a buffer to receive data read from the device.</p>
</dd>

### -param <i>lpdwNumberOfBytes</i> 

<dd>
<p>Caller-supplied pointer to a DWORD. The caller loads the DWORD with the number of bytes in the buffer pointed to by <i>lpBuffer</i>. The driver must replace this value with the number of bytes actually read.</p>
</dd>

### -param <i>lpOverlapped</i> 

<dd>
<p>Optional, caller-supplied pointer to an OVERLAPPED structure (described in the Microsoft Windows SDK documentation).</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>It is only necessary to implement <b>IStiUSD::RawReadCommand</b> if command and data information are read from a device by different methods. For other devices, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543834">IStiUSD::RawReadData</a> can be used for both commands and data. If the call is not implemented, it must return STIERR_UNSUPPORTED.</p>

<p>Implementation of this method, along with the meaning of buffer contents, are vendor-defined.</p>

<p>It is only necessary to implement <b>IStiUSD::RawReadCommand</b> if command and data information are read from a device by different methods. For other devices, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543834">IStiUSD::RawReadData</a> can be used for both commands and data. If the call is not implemented, it must return STIERR_UNSUPPORTED.</p>

<p>Implementation of this method, along with the meaning of buffer contents, are vendor-defined.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543758">IStiDevice::RawReadCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiUSD::RawReadCommand method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

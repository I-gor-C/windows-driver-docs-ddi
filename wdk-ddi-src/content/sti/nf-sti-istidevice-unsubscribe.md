---
UID: NF.sti.IStiDevice.UnSubscribe
title: IStiDevice::UnSubscribe
author: windows-driver-content
description: The IStiDevice::UnSubscribe method removes the caller from the list of applications registered to receive notification of device events.
old-location: image\istidevice_unsubscribe.htm
old-project: image
ms.assetid: ee0bfafa-9f4b-4b4a-8b26-4bab81253500
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IStiDevice, UnSubscribe, IStiDevice::UnSubscribe
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
req.alt-api: IStiDevice.UnSubscribe
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

# IStiDevice::UnSubscribe method



## -description
<p>The<b> IStiDevice::UnSubscribe</b> method removes the caller from the list of applications registered to receive notification of device events.</p>


## -syntax

````
HRESULT UnSubscribe();
````


## -parameters


## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>Before calling <b>IStiDevice::UnSubscribe</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

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
<a href="image.istidevice_subscribe">IStiDevice::Subscribe</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiDevice::UnSubscribe method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

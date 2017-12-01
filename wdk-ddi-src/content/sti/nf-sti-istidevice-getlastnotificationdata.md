---
UID: NF.sti.IStiDevice.GetLastNotificationData
title: IStiDevice::GetLastNotificationData
author: windows-driver-content
description: The IStiDevice::GetLastNotificationData method returns a description of the most recent event that occurred on a still image device.
old-location: image\istidevice_getlastnotificationdata.htm
old-project: image
ms.assetid: dd073fde-d2ba-45c0-a52c-22e86718901a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, GetLastNotificationData, IStiDevice::GetLastNotificationData
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
req.alt-api: IStiDevice.GetLastNotificationData
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

# IStiDevice::GetLastNotificationData method



## -description
<p>The <b>IStiDevice::GetLastNotificationData</b> method returns a description of the most recent event that occurred on a still image device.</p>


## -syntax

````
HRESULT GetLastNotificationData(
  [out] LPSTINOTIFY lpNotify
);
````


## -parameters
<dl>

### -param <i>lpNotify</i> [out]

<dd>
<p>Caller-supplied pointer to an <a href="..\sti\ns-sti--stinotify.md">STINOTIFY</a> structure to receive event information.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>Each time a <a href="NULL">Still Image Device Events</a> occurs, the still image event monitor calls <a href="image.istiusd_getnotificationdata">IStiUSD::GetNotificationData</a> (exported by a vendor-supplied minidriver) to obtain an event description. These descriptions are added to a linked list. If a client of the <b>IStiDevice</b> COM interface has called <a href="image.istidevice_subscribe">IStiDevice::Subscribe</a>, it is notified each time a device event occurs. It can then call <b>IStiDevice::GetLastNotificationData</b> to obtain the most recent addition to the linked list of events.</p>

<p>Before calling <b>IStiDevice::GetLastNotificationData</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

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
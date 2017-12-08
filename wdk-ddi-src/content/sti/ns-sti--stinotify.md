---
UID: NS.sti._STINOTIFY
title: STINOTIFY
author: windows-driver-content
description: The STINOTIFY structure is used as a parameter to the IStillImage::LaunchApplicationForDevice, IStiDevice::GetLastNotificationData, and IStiUSD::GetNotificationData methods.
old-location: image\stinotify.htm
old-project: image
ms.assetid: 7dc42f9a-2e55-4ae5-a951-7d1d3b14564b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: STINOTIFY, STINOTIFY, *LPSTINOTIFY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sti.h
req.include-header: Sti.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STINOTIFY
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

# STINOTIFY structure



## -description
<p>The STINOTIFY structure is used as a parameter to the <a href="image.istillimage_launchapplicationfordevice">IStillImage::LaunchApplicationForDevice</a>, <a href="image.istidevice_getlastnotificationdata">IStiDevice::GetLastNotificationData</a>, and <a href="image.istiusd_getnotificationdata">IStiUSD::GetNotificationData</a> methods.</p>


## -syntax

````
typedef struct _STINOTIFY {
  DWORD dwSize;
  GUID  guidNotificationCode;
  BYTE  abNotificationData[MAX_NOTIFICATION_DATA];
} STINOTIFY, *LPSTINOTIFY;
````


## -struct-fields
<dl>

### -field dwSize

<dd>
<p>Caller-supplied size, in bytes, of the STINOTIFY structure.</p>
</dd>

### -field guidNotificationCode

<dd>
<p>GUID of the event. For more information, see <a href="https://msdn.microsoft.com/5f9be89c-8442-4894-b2f6-a4d3558464bf">Still Image Device Events</a>.</p>
</dd>

### -field abNotificationData

<dd>
<p>Byte array containing optional, vendor-defined information.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
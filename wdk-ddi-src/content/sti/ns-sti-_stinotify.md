---
UID: NS.STI._STINOTIFY
title: _STINOTIFY
author: windows-driver-content
description: The STINOTIFY structure is used as a parameter to the IStillImage::LaunchApplicationForDevice, IStiDevice::GetLastNotificationData, and IStiUSD::GetNotificationData methods.
old-location: image\stinotify.htm
old-project: image
ms.assetid: 7dc42f9a-2e55-4ae5-a951-7d1d3b14564b
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _STINOTIFY, STINOTIFY, *LPSTINOTIFY
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
req.product: Windows 10 or later.
---

# _STINOTIFY structure



## -description
The STINOTIFY structure is used as a parameter to the <a href="image.istillimage_launchapplicationfordevice">IStillImage::LaunchApplicationForDevice</a>, <a href="image.istidevice_getlastnotificationdata">IStiDevice::GetLastNotificationData</a>, and <a href="image.istiusd_getnotificationdata">IStiUSD::GetNotificationData</a> methods.



## -syntax

````
typedef struct _STINOTIFY {
  DWORD dwSize;
  GUID  guidNotificationCode;
  BYTE  abNotificationData[MAX_NOTIFICATION_DATA];
} STINOTIFY, *LPSTINOTIFY;
````


## -struct-fields

### -field dwSize

Caller-supplied size, in bytes, of the STINOTIFY structure.


### -field guidNotificationCode

GUID of the event. For more information, see <a href="https://msdn.microsoft.com/5f9be89c-8442-4894-b2f6-a4d3558464bf">Still Image Device Events</a>.


### -field abNotificationData

Byte array containing optional, vendor-defined information.


## -remarks


## -requirements
<table>
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
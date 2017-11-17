---
UID: NS.sti._STINOTIFY
title: STINOTIFY
author: windows-driver-content
description: The STINOTIFY structure is used as a parameter to the IStillImage::LaunchApplicationForDevice, IStiDevice::GetLastNotificationData, and IStiUSD::GetNotificationData methods.
old-location: image\stinotify.htm
ms.assetid: 7dc42f9a-2e55-4ae5-a951-7d1d3b14564b
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: image
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
ms.keywords: STINOTIFY, STINOTIFY, *LPSTINOTIFY
req.iface: IStiDevice
req.product: Windows 10 or later.
---

# STINOTIFY structure



## -description
<p>The STINOTIFY structure is used as a parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543796">IStillImage::LaunchApplicationForDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543751">IStiDevice::GetLastNotificationData</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543821">IStiUSD::GetNotificationData</a> methods.</p>


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

### -field <b>dwSize</b>

<dd>
<p>Caller-supplied size, in bytes, of the STINOTIFY structure.</p>
</dd>

### -field <b>guidNotificationCode</b>

<dd>
<p>GUID of the event. For more information, see <a href="NULL">Still Image Device Events</a>.</p>
</dd>

### -field <b>abNotificationData</b>

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
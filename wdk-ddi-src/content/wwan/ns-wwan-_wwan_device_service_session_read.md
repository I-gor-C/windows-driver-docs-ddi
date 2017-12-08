---
UID: NS.WWAN._WWAN_DEVICE_SERVICE_SESSION_READ
title: _WWAN_DEVICE_SERVICE_SESSION_READ
author: windows-driver-content
description: The WWAN_DEVICE_SERVICE_SESSION_READ structure represents data associated with a device service session read notification.
old-location: netvista\wwan_device_service_session_read.htm
old-project: netvista
ms.assetid: 248C5386-B835-4806-8DD8-39327EDADA0C
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _WWAN_DEVICE_SERVICE_SESSION_READ, WWAN_DEVICE_SERVICE_SESSION_READ, *PWWAN_DEVICE_SERVICE_SESSION_READ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DEVICE_SERVICE_SESSION_READ
req.alt-loc: wwan.h
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

# _WWAN_DEVICE_SERVICE_SESSION_READ structure



## -description
The WWAN_DEVICE_SERVICE_SESSION_READ structure represents data associated with a device service session read notification.


## -syntax

````
typedef struct _WWAN_DEVICE_SERVICE_SESSION_READ {
  ULONG uSessionID;
  ULONG uDataSize;
} WWAN_DEVICE_SERVICE_SESSION_READ, *PWWAN_DEVICE_SERVICE_SESSION_READ;
````


## -struct-fields

### -field uSessionID

The session ID of the device service.

### -field uDataSize

The size, in bytes, of the device service data that follows the structure instance in memory. This value should not exceed the value of the <b>uMaxSessionDataSize</b> member of the <a href="netvista.wwan_supported_device_services">WWAN_SUPPORTED_DEVICE_SERVICES</a> structure.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported starting with  Windows 8.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_wwan_device_service_session_read">NDIS_WWAN_DEVICE_SERVICE_SESSION_READ</a>
</dt>
<dt>
<a href="netvista.wwan_supported_device_services">WWAN_SUPPORTED_DEVICE_SERVICES</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_SERVICE_SESSION_READ structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

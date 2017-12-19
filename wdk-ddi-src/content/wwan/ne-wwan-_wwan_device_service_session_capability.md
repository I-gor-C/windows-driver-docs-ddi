---
UID: NE.wwan._WWAN_DEVICE_SERVICE_SESSION_CAPABILITY
title: _WWAN_DEVICE_SERVICE_SESSION_CAPABILITY
author: windows-driver-content
description: The WWAN_DEVICE_SERVICE_SESSION_CAPABILITY enumeration lists the different device service session operations that are supported by the device service.
old-location: netvista\wwan_device_service_session_capability.htm
old-project: NetVista
ms.assetid: 57B41604-0189-48ED-847F-74C09C7746E8
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WWAN_DEVICE_SERVICE_SESSION_CAPABILITY, *PWWAN_DEVICE_SERVICE_SESSION_CAPABILITY, WWAN_DEVICE_SERVICE_SESSION_CAPABILITY, PWWAN_DEVICE_SERVICE_SESSION_CAPABILITY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DEVICE_SERVICE_SESSION_CAPABILITY
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

# _WWAN_DEVICE_SERVICE_SESSION_CAPABILITY enumeration



## -description
The WWAN_DEVICE_SERVICE_SESSION_CAPABILITY enumeration lists the different device service session operations that are supported by the device service.



## -syntax

````
typedef enum _WWAN_DEVICE_SERVICE_SESSION_CAPABILITY { 
  WwanDeviceServiceSessionNotSupported    = 0x00,
  WwanDeviceServiceSessionWriteSupported  = 0x01,
  WwanDeviceServiceSessionReadSupported   = 0x02
} WWAN_DEVICE_SERVICE_SESSION_CAPABILITY;
````


## -enum-fields

### -field WwanDeviceServiceSessionNotSupported

The device service does not support device service sessions.


### -field WwanDeviceServiceSessionWriteSupported

The device service supports write operations from Windows to the miniport driver.


### -field WwanDeviceServiceSessionReadSupported

The device service supports read indication  notifications on a session for data read from the device.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 8.

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
<a href="netvista.wwan_device_service_entry">WWAN_DEVICE_SERVICE_ENTRY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20WWAN_DEVICE_SERVICE_SESSION_CAPABILITY enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


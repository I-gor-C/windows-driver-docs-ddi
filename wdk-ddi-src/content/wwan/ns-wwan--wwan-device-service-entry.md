---
UID: NS.wwan._WWAN_DEVICE_SERVICE_ENTRY
title: WWAN_DEVICE_SERVICE_ENTRY
author: windows-driver-content
description: The WWAN_DEVICE_SERVICE_ENTRY structure describes information about a device service.
old-location: netvista\wwan_device_service_entry.htm
old-project: netvista
ms.assetid: 26B26715-0C1E-4FF1-B3FA-B6952BF70572
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_DEVICE_SERVICE_ENTRY, WWAN_DEVICE_SERVICE_ENTRY, *PWWAN_DEVICE_SERVICE_ENTRY
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
req.alt-api: WWAN_DEVICE_SERVICE_ENTRY
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_DEVICE_SERVICE_ENTRY structure



## -description
<p>The WWAN_DEVICE_SERVICE_ENTRY structure describes information about a device service.</p>


## -syntax

````
typedef struct _WWAN_DEVICE_SERVICE_ENTRY {
  GUID                                   DeviceServiceGuid;
  WWAN_DEVICE_SERVICE_SESSION_CAPABILITY SessionCapability;
  ULONG                                  uMaxSessionInstances;
} WWAN_DEVICE_SERVICE_ENTRY, *PWWAN_DEVICE_SERVICE_ENTRY;
````


## -struct-fields
<dl>

### -field <b>DeviceServiceGuid</b>

<dd>
<p>The GUID of the device service. This GUID is used to identify the device service in any of the other device OIDs/indications.</p>
</dd>

### -field <b>SessionCapability</b>

<dd>
<p>Flags indicating the capabilities of a device service session.</p>
</dd>

### -field <b>uMaxSessionInstances</b>

<dd>
<p>The maximum number of sessions supported by the device service.</p>
</dd>
</dl>

## -remarks
<p>Device service OIDs and NDIS Status Notifications use the device service's GUID to identify the device service.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831874">WWAN_DEVICE_SERVICE_SESSION_CAPABILITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_SERVICE_ENTRY structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

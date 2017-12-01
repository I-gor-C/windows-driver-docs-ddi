---
UID: NS.wwan._WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS
title: WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS
author: windows-driver-content
description: The WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure represents a list of commands supported by a device service.
old-location: netvista\wwan_device_service_supported_commands.htm
old-project: netvista
ms.assetid: 2AFE312D-8CCE-4A91-A23E-D5C6D2B0B01A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS, WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS, *PWWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS
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
req.alt-api: WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS
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

# WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure



## -description
<p>The WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure represents a list of commands supported by a device service.</p>


## -syntax

````
typedef struct _WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS {
  GUID             DeviceServiceGuid;
  WWAN_LIST_HEADER ListHeader;
} WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS, *PWWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS;
````


## -struct-fields
<dl>

### -field <b>DeviceServiceGuid</b>

<dd>
<p>The GUID of the device service command.</p>
</dd>

### -field <b>ListHeader</b>

<dd>
<p>A formatted 
     <a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a> object that represents the
     list of commands supported by the device service.</p>
</dd>
</dl>

## -remarks


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
<a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

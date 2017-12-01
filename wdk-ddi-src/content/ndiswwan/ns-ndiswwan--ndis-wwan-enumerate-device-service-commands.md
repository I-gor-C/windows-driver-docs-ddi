---
UID: NS.ndiswwan._NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS
title: NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS
author: windows-driver-content
description: The NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS structure represents the commands supported by a device service.
old-location: netvista\ndis_wwan_enumerate_device_service_commands.htm
old-project: netvista
ms.assetid: 9D30F8BE-C376-48FD-A76C-6069F332BC11
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS, NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS, *PNDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS
req.alt-loc: ndiswwan.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS structure



## -description
<p>The NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS structure represents the commands supported by a device service.</p>


## -syntax

````
typedef struct _NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS {
  NDIS_OBJECT_HEADER Header;
  GUID               DeviceServiceGuid;
} NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS, *PNDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS
     structure. The MB Service sets the header with the values that are shown in the following table when it
     sends the data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>DeviceServiceGuid</b>

<dd>
<p>The GUID of the device service for which commands should be enumerated.</p>
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
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.windot11._DOT11_WFD_DEVICE_INFO
title: DOT11_WFD_DEVICE_INFO
author: windows-driver-content
description: the DOT11_WFD_DEVICE_INFO structure is included with a OID_DOT11_WFD_DEVICE_INFO request. The structure contains Wi-Fi Direct (WFD) device information related to Peer-to-Peer (P2P) attributes.
old-location: netvista\_dot11_wfd_device_info.htm
old-project: netvista
ms.assetid: 6E0E9BC9-9C84-4511-A28E-2BB2D6367F74
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_WFD_DEVICE_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_WFD_DEVICE_INFO
req.alt-loc: Windot11.h
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

# DOT11_WFD_DEVICE_INFO structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_DEVICE_INFO {
  NDIS_OBJECT_HEADER    Header;
  DOT11_MAC_ADDRESS     DeviceAddress;
  USHORT                ConfigMethods;
  DOT11_WPS_DEVICE_TYPE PrimaryDeviceType;
  DOT11_WPS_DEVICE_NAME DeviceName;
} DOT11_WFD_DEVICE_INFO, *PDOT11_WFD_DEVICE_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Specifies the type, revision and size of the <b>DOT11_WFD_DEVICE_INFO</b> structure. The required settings for the members of <b>Header</b> are the following:</p>
<table>
<tr>
<th>Member</th>
<th>Setting</th>
</tr>
<tr>
<td><b>Type</b></td>
<td>NDIS_OBJECT_TYPE_DEFAULT</td>
</tr>
<tr>
<td><b>Revision</b></td>
<td>DOT11_WFD_DEVICE_INFO_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_WFD_DEVICE_INFO_REVISION_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DeviceAddress</b>

<dd>
<p>The device address to assign to a WFD port. This address is used when constructing P2P Information Elements (IEs).</p>
</dd>

### -field <b>ConfigMethods</b>

<dd>
<p>The configuration methods supported by the WFD device.</p>
</dd>

### -field <b>PrimaryDeviceType</b>

<dd>
<p>The primary device type for the WFD device.</p>
</dd>

### -field <b>DeviceName</b>

<dd>
<p>A friendly name assigned to the WFD device.</p>
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
<p>Versions: Supported in Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>
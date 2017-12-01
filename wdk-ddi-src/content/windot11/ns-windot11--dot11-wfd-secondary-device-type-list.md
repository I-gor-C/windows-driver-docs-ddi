---
UID: NS.windot11._DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST
title: DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST
author: windows-driver-content
description: the DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST structure is included with a OID_DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST request. The structure contains the list of secondary device types advertised by a Wi-Fi Direct device.
old-location: netvista\_dot11_wfd_secondary_device_type_list.htm
old-project: netvista
ms.assetid: ABD61A6C-EE0A-49AF-AE8C-75014C2A09D4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST,
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
req.alt-api: DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST
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

# DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST {
  NDIS_OBJECT_HEADER    Header;
  ULONG                 uNumOfEntries;
  ULONG                 uTotalNumOfEntries;
  DOT11_WFD_DEVICE_TYPE SecondaryDeviceTypes[1];
}  DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST, *PDOT11_WFD_SECONDARY_DEVICE_TYPE_LIST;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Specifies the type, revision and size of the <b>DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST</b> structure. The required settings for the members of <b>Header</b> are the following:</p>
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
<td>DOT11_WFD_SECONDARY_DEVICE_TYPE_LIST_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_WFD_SECONDARY_DEVICE_TYPE_LIST_REVISION_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>uNumOfEntries</b>

<dd>
<p>The number of entries present in <b>SecondaryDeviceTypes</b>.</p>
</dd>

### -field <b>uTotalNumOfEntries</b>

<dd>
<p>The maximum number of entries the <b>SecondaryDeviceTypes</b> array can contain.</p>
</dd>

### -field <b>SecondaryDeviceTypes</b>

<dd>
<p>An array of secondary device types.</p>
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
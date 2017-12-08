---
UID: NS.windot11._DOT11_WFD_DEVICE_TYPE
title: DOT11_WFD_DEVICE_TYPE
author: windows-driver-content
description: The DOT11_WFD_DEVICE_TYPE structure is used to specify primary and secondary device types.
old-location: netvista\dot11_wfd_device_type.htm
old-project: netvista
ms.assetid: 4AE7C35B-D2EA-4987-8195-EDD472C39681
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_WFD_DEVICE_TYPE, DOT11_WFD_DEVICE_TYPE, *PDOT11_WFD_DEVICE_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_WFD_DEVICE_TYPE
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

# DOT11_WFD_DEVICE_TYPE structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_DEVICE_TYPE {
  USHORT   CategoryID;
  USHORT   SubCategoryID;
  UCHAR    OUI[4];
} DOT11_WFD_DEVICE_TYPE, *PDOT11_WFD_DEVICE_TYPE;
````


## -struct-fields
<dl>

### -field CategoryID

<dd>
<p>The identifier of the main type category.</p>
</dd>

### -field SubCategoryID

<dd>
<p>The identifier of the type subcategory.</p>
</dd>

### -field OUI[4]

<dd>
<p>The Organizationally Unique Identifier (OUI) assigned to a device.</p>
</dd>
</dl>

## -remarks
<p>The <b>DOT11_WFD_DEVICE_TYPE</b> data is provided in host byte-ordering. The miniport may need to convert the data to an ordering appropriate for inclusion in Peer-to-Peer Information Elements.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with   Windows 8.</p>
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
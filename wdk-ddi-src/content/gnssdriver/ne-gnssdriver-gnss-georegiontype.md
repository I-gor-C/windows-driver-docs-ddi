---
UID: NE.gnssdriver.GNSS_GEOREGIONTYPE
title: GNSS_GEOREGIONTYPE
author: windows-driver-content
description: This enumeration is used for defining a geographical shape. A shape is used to define a geofence. Windows 10 currently only supports circular geofences.
old-location: sensors\gnss_georegiontype.htm
ms.assetid: 736A1D63-A96E-4E29-ADFD-F441AC4757C6
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_GEOREGIONTYPE
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
req.iface: 
---

# GNSS_GEOREGIONTYPE enumeration



## -description
<p>This enumeration is used for defining a geographical shape. A shape is used to define a geofence. Windows 10 currently only supports circular geofences.</p>


## -syntax

````
typedef enum  { 
  GNSS_GeoRegion_Circle  = 0x01
} GNSS_GEOREGIONTYPE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_GeoRegion_Circle"></a><a id="gnss_georegion_circle"></a><a id="GNSS_GEOREGION_CIRCLE"></a><b>GNSS_GeoRegion_Circle</b>

<dd>
<p>Defines a circular geofence.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>
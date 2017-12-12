---
UID: NS.GNSSDRIVER.PGNSS_GEOREGION
title: PGNSS_GEOREGION
author: windows-driver-content
description: This structure defines the geographical shape of a geofence.
old-location: sensors\gnss_georegion.htm
old-project: sensors
ms.assetid: 70FC3BCE-3869-4263-8870-BB97438CB5F1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PGNSS_GEOREGION, GNSS_GEOREGION, *PGNSS_GEOREGION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_GEOREGION
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
req.irql: 
---

# PGNSS_GEOREGION structure



## -description
This structure defines the geographical shape of  a geofence.



## -syntax

````
typedef struct {
  ULONG              Size;
  ULONG              Version;
  GNSS_GEOREGIONTYPE GeoRegionType;
  union {
    GNSS_GEOREGION_CIRCLE Circle;
    BYTE                  Unused[512];
  };
} GNSS_GEOREGION, *PGNSS_GEOREGION;
````


## -struct-fields

### -field Size

Structure size.


### -field Version

Version number.


### -field GeoRegionType


<a href="..\gnssdriver\ne-gnssdriver-gnss_georegiontype.md">GNSS_GEOREGIONTYP</a>E enumeration that defines the georegion type of a geofence.


### -field Circle


<a href="sensors.gnss_georegion_circle">GNSS_GEOREGION_CIRCLE</a> structure that defines a circular geofence.


### -field Unused[512]

Padding buffer.


## -remarks
A geographical shape is used to define a geofence.  Windows 10 currently supports only circular geofences.




## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.gnssdriver.PGNSS_FIXDATA_SATELLITE
title: PGNSS_FIXDATA_SATELLITE
author: windows-driver-content
description: This structure defines satellite-related information of a fix.
old-location: sensors\gnss_fixdata_satellite.htm
old-project: sensors
ms.assetid: D1454F07-3CBA-498B-B054-6A0D5020A164
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PGNSS_FIXDATA_SATELLITE, GNSS_FIXDATA_SATELLITE, *PGNSS_FIXDATA_SATELLITE
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
req.alt-api: GNSS_FIXDATA_SATELLITE
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
req.iface: 
---

# PGNSS_FIXDATA_SATELLITE structure



## -description
<p>This structure defines satellite-related information of a fix.</p>


## -syntax

````
typedef struct {
  ULONG              Size;
  ULONG              Version;
  ULONG              SatelliteCount;
  GNSS_SATELLITEINFO SatelliteArray[GNSS_MAXSATELLITE];
} GNSS_FIXDATA_SATELLITE, *PGNSS_FIXDATA_SATELLITE;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Structure size.</p>
</dd>

### -field Version

<dd>
<p>Version number.</p>
</dd>

### -field SatelliteCount

<dd>
<p>Number of satellites in this structure. Not all satellites are actually used for positioning.</p>
</dd>

### -field SatelliteArray[GNSS_MAXSATELLITE]

<dd>
<p>An array of satellites with each array element representing information about a specific satellite.</p>
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
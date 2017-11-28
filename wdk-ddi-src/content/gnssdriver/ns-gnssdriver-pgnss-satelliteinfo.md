---
UID: NS.gnssdriver.PGNSS_SATELLITEINFO
title: PGNSS_SATELLITEINFO
author: windows-driver-content
description: This structure defines satellite-related information of a fix.
old-location: sensors\gnss_satelliteinfo.htm
old-project: sensors
ms.assetid: 27F537D8-45B2-43D9-A614-3558534C9DBA
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_SATELLITEINFO, GNSS_SATELLITEINFO, *PGNSS_SATELLITEINFO
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
req.alt-api: GNSS_SATELLITEINFO
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

# PGNSS_SATELLITEINFO structure



## -description
<p>This structure defines satellite-related information of a fix.</p>


## -syntax

````
typedef struct {
  ULONG  SatelliteId;
  BOOL   UsedInPositiong;
  double Elevation;
  double Azimuth;
  double SignalToNoiseRatio;
} GNSS_SATELLITEINFO, *PGNSS_SATELLITEINFO;
````


## -struct-fields
<dl>

### -field <b>SatelliteId</b>

<dd>
<p>Pseudorandom noise (PRN) code or other identification for the satellite.</p>
</dd>

### -field <b>UsedInPositiong</b>

<dd>
<p>Indicates whether this was simply a visible satellite or actually used in the positioning.</p>
</dd>

### -field <b>Elevation</b>

<dd>
<p>Elevation value</p>
</dd>

### -field <b>Azimuth</b>

<dd>
<p>Azimuth value.</p>
</dd>

### -field <b>SignalToNoiseRatio</b>

<dd>
<p>Signal to noise ratio.</p>
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
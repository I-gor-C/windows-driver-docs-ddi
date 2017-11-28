---
UID: NS.gnssdriver.PGNSS_BREADCRUMB_V1
title: PGNSS_BREADCRUMB_V1
author: windows-driver-content
description: This structure contains an individual breadcrumb. The order and types of the fields are designed to pack densely.
old-location: sensors\gnss_breadcrumb_v1.htm
old-project: sensors
ms.assetid: BE1D09C4-8EC0-4BF3-A943-20EDD44F9CF1
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_BREADCRUMB_V1, GNSS_BREADCRUMB_V1, *PGNSS_BREADCRUMB_V1
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
req.alt-api: GNSS_BREADCRUMB_V1
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

# PGNSS_BREADCRUMB_V1 structure



## -description
<p>This structure contains an individual breadcrumb. The order and types of the fields are designed  to pack densely.</p>


## -syntax

````
typedef struct {
  FILETIME       FixTimeStamp;
  double         Latitude;
  double         Longitude;
  ULONG          HorizontalAccuracy;
  unsigned short Speed;
  unsigned short SpeedAccuracy;
  short          Altitude;
  unsigned short AltitudeAccuracy;
  short          Heading;
  unsigned char  HeadingAccuracy;
  unsigned char  FixSuccess;
} GNSS_BREADCRUMB_V1, *PGNSS_BREADCRUMB_V1;
````


## -struct-fields
<dl>

### -field <b>FixTimeStamp</b>

<dd>
<p>Contains the breadcrumb fix timestamp value.</p>
</dd>

### -field <b>Latitude</b>

<dd>
<p>Contains the breadcrumb longitude value at the time of the fix.</p>
</dd>

### -field <b>Longitude</b>

<dd>
<p>Contains the breadcrumb latitude at the time of the fix.</p>
</dd>

### -field <b>HorizontalAccuracy</b>

<dd>
<p>Contains the breadcrumb horizontal altitude value.</p>
</dd>

### -field <b>Speed</b>

<dd>
<p>Contains the speed value at the time of the breadcrumb fix.</p>
</dd>

### -field <b>SpeedAccuracy</b>

<dd>
<p>Contains the breadcrumb speed accuracy value.</p>
</dd>

### -field <b>Altitude</b>

<dd>
<p>Contains the breadcrumb altitude value at the time of the fix.</p>
</dd>

### -field <b>AltitudeAccuracy</b>

<dd>
<p>Contains the breadcrumb altitude accuracy value.</p>
</dd>

### -field <b>Heading</b>

<dd>
<p>Contains the breadcrumb heading value at the time of the fix.</p>
</dd>

### -field <b>HeadingAccuracy</b>

<dd>
<p>Contains the breadcrumb heading accuracy value.</p>
</dd>

### -field <b>FixSuccess</b>

<dd>
<p>A Boolean type that contains the fix success value.</p>
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
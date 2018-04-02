---
UID: NS:gnssdriver.GNSS_GEOREGION_CIRCLE
title: GNSS_GEOREGION_CIRCLE
author: windows-driver-content
description: This structure is used for defining a circular geofence.
old-location: sensors\gnss_georegion_circle.htm
old-project: sensors
ms.assetid: 498F8325-C887-4FDE-8BCF-A713639E3B35
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: "*PGNSS_GEOREGION_CIRCLE, GNSS_GEOREGION_CIRCLE, GNSS_GEOREGION_CIRCLE structure [Sensor Devices], PGNSS_GEOREGION_CIRCLE, PGNSS_GEOREGION_CIRCLE structure pointer [Sensor Devices], gnssdriver/GNSS_GEOREGION_CIRCLE, gnssdriver/PGNSS_GEOREGION_CIRCLE, sensors.gnss_georegion_circle"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	gnssdriver.h
api_name:
-	GNSS_GEOREGION_CIRCLE
product: Windows
targetos: Windows
req.typenames: GNSS_GEOREGION_CIRCLE, *PGNSS_GEOREGION_CIRCLE
---

# GNSS_GEOREGION_CIRCLE structure
This structure is used for defining a circular geofence.

## Syntax
```
typedef struct GNSS_GEOREGION_CIRCLE {
  double Latitude;
  double Longitude;
  double RadiusInMeters;
} *PGNSS_GEOREGION_CIRCLE, GNSS_GEOREGION_CIRCLE;
```

## Members


`Latitude`

Latitude of the center of the circle.

`Longitude`

Longitude of the center of the circle.

`RadiusInMeters`

Radius of the circle in meters.

## Remarks
A geographical shape is used to define a geofence.  Windows 10 currently supports only circular geofences.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |
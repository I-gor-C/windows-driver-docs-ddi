---
UID: NS:gnssdriver.GNSS_FIXDATA_BASIC
title: GNSS_FIXDATA_BASIC
author: windows-driver-content
description: This structure defines basic position information.
old-location: sensors\gnss_fixdata_basic.htm
old-project: sensors
ms.assetid: D293366B-13FA-438E-BEBD-1F0EAA693400
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: "*PGNSS_FIXDATA_BASIC, GNSS_FIXDATA_BASIC, GNSS_FIXDATA_BASIC structure [Sensor Devices], PGNSS_FIXDATA_BASIC, PGNSS_FIXDATA_BASIC structure pointer [Sensor Devices], gnssdriver/GNSS_FIXDATA_BASIC, gnssdriver/PGNSS_FIXDATA_BASIC, sensors.gnss_fixdata_basic"
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
-	GNSS_FIXDATA_BASIC
product:
- Windows
targetos: Windows
req.typenames: GNSS_FIXDATA_BASIC, *PGNSS_FIXDATA_BASIC
---

# GNSS_FIXDATA_BASIC structure
This structure defines basic position information.

## Syntax
```
typedef struct GNSS_FIXDATA_BASIC {
  ULONG  Size;
  ULONG  Version;
  double Latitude;
  double Longitude;
  double Altitude;
  double Speed;
  double Heading;
}  *PGNSS_FIXDATA_BASIC;
```

## Members


`Size`

Structure size.

`Version`

Version number.

`Latitude`

Latitude value. Valid range is -180.0 to + 180.0. NaN indicates unavailable.

`Longitude`

Longitude value. Valid range is -90.0 to + 90.0. NaN indicates unavailable.

`Altitude`

Altitude value in meters (in relation to sea level). NaN indicates unavailable.

`Speed`

Speed in meters per second. Zero or positive value. NaN indicates unavailable.

`Heading`

Heading/direction in degrees. Valid range is 0 to 360. Zero indicates true north. NaN indicates unavailable.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |
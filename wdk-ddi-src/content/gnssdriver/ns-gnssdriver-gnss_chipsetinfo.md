---
UID: NS:gnssdriver.GNSS_CHIPSETINFO
title: GNSS_CHIPSETINFO
author: windows-driver-content
description: This structure defines the specific data elements associated with the GNSS hardware.
old-location: sensors\gnss_chipsetinfo.htm
old-project: sensors
ms.assetid: DE45805C-09E6-44B8-A4DA-BF73EC444AA9
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: "*PGNSS_CHIPSETINFO, GNSS_CHIPSETINFO, GNSS_CHIPSETINFO structure [Sensor Devices], PGNSS_CHIPSETINFO, PGNSS_CHIPSETINFO structure pointer [Sensor Devices], gnssdriver/GNSS_CHIPSETINFO, gnssdriver/PGNSS_CHIPSETINFO, sensors.gnss_chipsetinfo"
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
-	GNSS_CHIPSETINFO
product: Windows
targetos: Windows
req.typenames: GNSS_CHIPSETINFO, *PGNSS_CHIPSETINFO
---

# GNSS_CHIPSETINFO structure
This structure defines the specific data elements associated with the GNSS hardware.

## Syntax
````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR ManufacturerID[25];
  WCHAR HardwareID[25];
  WCHAR FirmwareVersion[20];
  BYTE  Unused[512];
} GNSS_CHIPSETINFO, *PGNSS_CHIPSETINFO;
````

## Members


`FirmwareVersion`



`HardwareID`



`ManufacturerID`



`Size`

Structure size.

`Unused`



`Version`

Version number.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |
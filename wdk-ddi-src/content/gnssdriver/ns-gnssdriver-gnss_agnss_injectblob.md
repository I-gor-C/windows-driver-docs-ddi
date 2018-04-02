---
UID: NS:gnssdriver.GNSS_AGNSS_INJECTBLOB
title: GNSS_AGNSS_INJECTBLOB
author: windows-driver-content
description: This structure defines the format for AGNSS extended ephemeris injection.
old-location: sensors\gnss_agnss_injectblob.htm
old-project: sensors
ms.assetid: DAC91C40-C9B3-433C-AA64-CE4C021CD8C5
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: "*PGNSS_AGNSS_INJECTBLOB, GNSS_AGNSS_INJECTBLOB, GNSS_AGNSS_INJECTBLOB structure [Sensor Devices], PGNSS_AGNSS_INJECTBLOB, PGNSS_AGNSS_INJECTBLOB structure pointer [Sensor Devices], gnssdriver/GNSS_AGNSS_INJECTBLOB, gnssdriver/PGNSS_AGNSS_INJECTBLOB, sensors.gnss_agnss_injectblob"
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
-	GNSS_AGNSS_INJECTBLOB
product:
- Windows
targetos: Windows
req.typenames: GNSS_AGNSS_INJECTBLOB, *PGNSS_AGNSS_INJECTBLOB
---

# GNSS_AGNSS_INJECTBLOB structure
This structure defines the format for AGNSS extended ephemeris injection.

## Syntax
```
typedef struct GNSS_AGNSS_INJECTBLOB {
  ULONG Size;
  ULONG Version;
  ULONG BlobOui;
  ULONG BlobVersion;
  ULONG AgnssFormat;
  ULONG BlobSize;
  BYTE  BlobData[ANYSIZE_ARRAY];
}  *PGNSS_AGNSS_INJECTBLOB;
```

## Members


`Size`

Structure size.

`Version`

Version number.

`BlobOui`

This field indicates the 3-byte OUI of silicon vendor or device maker.

`BlobVersion`

Version of the blob from the same vendor.

`AgnssFormat`

Data format of the blob.

The formats are defined as macros (GNSS_AGNSSFORMAT_*).

`BlobSize`

Size of the blob data in bytes.

`BlobData`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |
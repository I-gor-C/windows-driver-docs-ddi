---
UID: NS:ehstorbandmgmt._BAND_LOCATION_INFO
title: "_BAND_LOCATION_INFO"
author: windows-driver-content
description: The BAND_LOCATION_INFO structure specifies the location information for a band table entry query.
old-location: storage\band_location_info.htm
old-project: storage
ms.assetid: A9E28600-45B2-4082-917F-29B3237DEC84
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PBAND_LOCATION_INFO, BAND_LOCATION_INFO, BAND_LOCATION_INFO structure [Storage Devices], PBAND_LOCATION_INFO, PBAND_LOCATION_INFO structure pointer [Storage Devices], _BAND_LOCATION_INFO, ehstorbandmgmt/BAND_LOCATION_INFO, ehstorbandmgmt/PBAND_LOCATION_INFO, storage.band_location_info"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ehstorbandmgmt.h
req.include-header: EhStorBandMgmt.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8
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
-	EhStorBandMgmt.h
api_name:
-	BAND_LOCATION_INFO
product:
- Windows
targetos: Windows
req.typenames: BAND_LOCATION_INFO, *PBAND_LOCATION_INFO
---

# _BAND_LOCATION_INFO structure
The <b>BAND_LOCATION_INFO</b> structure specifies the location information for a band table entry query.

## Syntax
```
typedef struct _BAND_LOCATION_INFO {
  ULONG         StructSize;
  ULONG         Reserved;
  LARGE_INTEGER BandStart;
  LARGE_INTEGER BandSize;
  BYTE          Metadata[32];
} *PBAND_LOCATION_INFO, BAND_LOCATION_INFO;
```

## Members


`StructSize`

The size of the structure in bytes. Set to <b>sizeof</b>(BAND_LOCATION_INFO).

`Reserved`

Reserved.

`BandStart`

The offset in bytes of this band location on the storage device. This value is always 0 for the global band.

`BandSize`

The size in bytes of the band configured at this location. This value is set to the maximum size possible for the global band.

`Metadata`

A metadata field used as a data area for a band management application.

## Remarks
<b>BandStart</b> and <b>BandSize</b> must be a multiple of the sector size of the underlying storage device.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8 Available starting with Windows 8 |
| **Header** | ehstorbandmgmt.h (include EhStorBandMgmt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439578">BAND_TABLE_ENTRY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451372">IOCTL_EHSTOR_BANDMGMT_CREATE_BAND</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451380">IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS</a>
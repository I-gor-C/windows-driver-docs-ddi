---
UID: NS:ntddmmc._FEATURE_DATA_DVD_PLUS_R
title: "_FEATURE_DATA_DVD_PLUS_R"
author: windows-driver-content
description: The FEATURE_DATA_DVD_PLUS_R structure contains information about the DVD+R feature.
old-location: storage\feature_data_dvd_plus_r.htm
old-project: storage
ms.assetid: e1501ea9-a55b-4fbc-990b-2172c7369bb1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFEATURE_DATA_DVD_PLUS_R, FEATURE_DATA_DVD_PLUS_R, FEATURE_DATA_DVD_PLUS_R structure [Storage Devices], PFEATURE_DATA_DVD_PLUS_R, PFEATURE_DATA_DVD_PLUS_R structure pointer [Storage Devices], _FEATURE_DATA_DVD_PLUS_R, ntddmmc/FEATURE_DATA_DVD_PLUS_R, ntddmmc/PFEATURE_DATA_DVD_PLUS_R, storage.feature_data_dvd_plus_r, structs-CD-ROM_fb4a1383-3c8f-48e8-8fc8-3796e00f80a6.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddmmc.h
api_name:
-	FEATURE_DATA_DVD_PLUS_R
product: Windows
targetos: Windows
req.typenames: FEATURE_DATA_DVD_PLUS_R, *PFEATURE_DATA_DVD_PLUS_R
---

# _FEATURE_DATA_DVD_PLUS_R structure
The FEATURE_DATA_DVD_PLUS_R structure contains information about the DVD+R feature.

## Syntax
```
typedef struct _FEATURE_DATA_DVD_PLUS_R {
  FEATURE_HEADER Header;
  UCHAR  : 1     Write;
  UCHAR  : 7     Reserved1;
  UCHAR          Reserved2[3];
} *PFEATURE_DATA_DVD_PLUS_R, FEATURE_DATA_DVD_PLUS_R;
```

## Members


`Header`

Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor.

`Write`

Indicates, when set to 1, that the device has an ability that was not specified in the DVD-ROM profile, to write to DVD+R discs according to <i>DVD+R 4.7 Gbytes Basic Format Specifications.</i> When set to 0, the device has no extra ability beyond what is specified in the profile.

`Reserved1`

Reserved.

`Reserved2`

Reserved.

## Remarks
This structure holds data for the feature named "DVD+R" by the <i>MMC-3 </i>specification. Devices that support this feature can specify whether they are able to perform writes to DVD+R discs, even though this ability was not indicated in the device's DVD-ROM profile.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddmmc.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>
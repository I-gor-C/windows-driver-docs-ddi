---
UID: NS:ntddmmc._FEATURE_DATA_CD_TRACK_AT_ONCE
title: "_FEATURE_DATA_CD_TRACK_AT_ONCE"
author: windows-driver-content
description: The FEATURE_DATA_CD_TRACK_AT_ONCE structure holds information about the CD Track at Once feature.
old-location: storage\feature_data_cd_track_at_once.htm
old-project: storage
ms.assetid: e3ce42a6-0d94-46cb-9831-c29f92a677cd
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFEATURE_DATA_CD_TRACK_AT_ONCE, FEATURE_DATA_CD_TRACK_AT_ONCE, FEATURE_DATA_CD_TRACK_AT_ONCE structure [Storage Devices], PFEATURE_DATA_CD_TRACK_AT_ONCE, PFEATURE_DATA_CD_TRACK_AT_ONCE structure pointer [Storage Devices], _FEATURE_DATA_CD_TRACK_AT_ONCE, ntddmmc/FEATURE_DATA_CD_TRACK_AT_ONCE, ntddmmc/PFEATURE_DATA_CD_TRACK_AT_ONCE, storage.feature_data_cd_track_at_once, structs-CD-ROM_d2648aa5-b3d5-49f2-98d1-01e90dd72332.xml"
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
-	FEATURE_DATA_CD_TRACK_AT_ONCE
product:
- Windows
targetos: Windows
req.typenames: FEATURE_DATA_CD_TRACK_AT_ONCE, *PFEATURE_DATA_CD_TRACK_AT_ONCE
---

# _FEATURE_DATA_CD_TRACK_AT_ONCE structure
The FEATURE_DATA_CD_TRACK_AT_ONCE structure holds information about the CD Track at Once feature.

## Syntax
```
typedef struct _FEATURE_DATA_CD_TRACK_AT_ONCE {
  FEATURE_HEADER Header;
  UCHAR  : 1     RWSubchannelsRecordable;
  UCHAR  : 1     CdRewritable;
  UCHAR  : 1     TestWriteOk;
  UCHAR  : 1     RWSubchannelPackedOk;
  UCHAR  : 1     RWSubchannelRawOk;
  UCHAR  : 1     Reserved1;
  UCHAR  : 1     BufferUnderrunFree;
  UCHAR  : 1     Reserved3;
  UCHAR          Reserved2;
  UCHAR          DataTypeSupported[2];
} FEATURE_DATA_CD_TRACK_AT_ONCE, *PFEATURE_DATA_CD_TRACK_AT_ONCE;
```

## Members


`Header`

Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor.

`RWSubchannelsRecordable`

Indicates, when set to 1, that the device can record the read/write subchannels with user-supplied data.

`CdRewritable`

Indicates, when set to 1, that the device supports overwriting a Track-at-Once track with another track's information.

`TestWriteOk`

Indicates, when set to 1, that the device can perform test writes.

`RWSubchannelPackedOk`

Indicates, when set to 1, that the device supports writing R-W sub code in the packed mode.

`RWSubchannelRawOk`

Indicates, when set to 1, that the device supports writing R-W sub code in the raw mode.

`Reserved1`

Reserved.

`BufferUnderrunFree`

Indicates, when set to 1, that the device is capable of zero-loss linking.

`Reserved3`

Reserved.

`Reserved2`

Reserved.

`DataTypeSupported`

Indicates the data types that the device supports. See the <i>SCSI Multimedia 3</i> (<i>MMC-3</i>) specification for a description of the values that this member can take. <b>DataTypeSupported</b>[0] holds the most significant byte of value that indicates the data types. <b>DataTypeSupported</b>[1] holds the least significant byte of that value.

## Remarks
This structure holds data for the feature named "CD Track at Once" by the <i>MMC-3 </i>specification. Devices that support this feature can write data to a CD track.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddmmc.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
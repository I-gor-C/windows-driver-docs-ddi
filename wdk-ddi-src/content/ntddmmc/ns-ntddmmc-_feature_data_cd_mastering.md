---
UID: NS:ntddmmc._FEATURE_DATA_CD_MASTERING
title: "_FEATURE_DATA_CD_MASTERING"
author: windows-driver-content
description: The FEATURE_DATA_CD_MASTERING structure holds information for the CD Mastering feature.
old-location: storage\feature_data_cd_mastering.htm
old-project: storage
ms.assetid: 340e9675-9d07-4224-ac1b-86e7586c0738
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFEATURE_DATA_CD_MASTERING, FEATURE_DATA_CD_MASTERING, FEATURE_DATA_CD_MASTERING structure [Storage Devices], PFEATURE_DATA_CD_MASTERING, PFEATURE_DATA_CD_MASTERING structure pointer [Storage Devices], _FEATURE_DATA_CD_MASTERING, ntddmmc/FEATURE_DATA_CD_MASTERING, ntddmmc/PFEATURE_DATA_CD_MASTERING, storage.feature_data_cd_mastering, structs-CD-ROM_f803f10f-2ef7-4e3b-9c16-1ed2f3c5b2a5.xml"
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
-	FEATURE_DATA_CD_MASTERING
product: Windows
targetos: Windows
req.typenames: FEATURE_DATA_CD_MASTERING, *PFEATURE_DATA_CD_MASTERING
---

# _FEATURE_DATA_CD_MASTERING structure
The FEATURE_DATA_CD_MASTERING structure holds information for the CD Mastering feature.

## Syntax
```
typedef struct _FEATURE_DATA_CD_MASTERING {
  FEATURE_HEADER Header;
  UCHAR  : 1     RWSubchannelsRecordable;
  UCHAR  : 1     CdRewritable;
  UCHAR  : 1     TestWriteOk;
  UCHAR  : 1     RawRecordingOk;
  UCHAR  : 1     RawMultiSessionOk;
  UCHAR  : 1     SessionAtOnceOk;
  UCHAR  : 1     BufferUnderrunFree;
  UCHAR  : 1     Reserved1;
  UCHAR          MaximumCueSheetLength[3];
} *PFEATURE_DATA_CD_MASTERING, FEATURE_DATA_CD_MASTERING;
```

## Members


`Header`

Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor.

`RWSubchannelsRecordable`

Indicates, when set to 1, that the device can record the R-W subchannels with user-supplied information.

`CdRewritable`

Indicates, when set to 1, that the device can do mastering and TAO recording on rewritable media.

`TestWriteOk`

Indicates, when set to 1, that the device can perform test writes.

`RawRecordingOk`

Indicates, when set to 1, that the device can record using the raw write type.

`RawMultiSessionOk`

Indicates, when set to 1, that the device can record multisession in raw mode.

`SessionAtOnceOk`

Indicates, when set to 1, that the device can record using the Session-at-Once recording mode.

`BufferUnderrunFree`

Indicates, when set to 1, that the device is capable of zero-loss linking.

`Reserved1`

Reserved.

`MaximumCueSheetLength`

Indicates the maximum length of a Cue Sheet that can be accepted by the device for Session at Once recording. <b>MaximumCueSheetLength</b>[0] holds the most significant byte of the 3-byte value for the length. <b>MaximumCueSheetLength</b>[2] holds the least significant byte.

## Remarks
This structure holds data for the feature named "CD Mastering" by the <i>SCSI Multimedia - 4 (MMC-4)</i> specification. Devices that support this feature can write to a CD in either "Session-at-Once" mode or Raw mode.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddmmc.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
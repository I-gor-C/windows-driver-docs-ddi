---
UID: NS:ntddmmc._FEATURE_DATA_MRW
title: "_FEATURE_DATA_MRW"
author: windows-driver-content
description: The FEATURE_DATA_MRW structure contains information about the MRW feature.
old-location: storage\feature_data_mrw.htm
old-project: storage
ms.assetid: af0c8c50-c5a0-4395-a608-fced6ac3cfe5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFEATURE_DATA_MRW, FEATURE_DATA_MRW, FEATURE_DATA_MRW structure [Storage Devices], PFEATURE_DATA_MRW, PFEATURE_DATA_MRW structure pointer [Storage Devices], _FEATURE_DATA_MRW, ntddmmc/FEATURE_DATA_MRW, ntddmmc/PFEATURE_DATA_MRW, storage.feature_data_mrw, structs-CD-ROM_54208a52-0bc2-4e97-a3b1-4d57f5192ce4.xml"
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
-	FEATURE_DATA_MRW
product:
- Windows
targetos: Windows
req.typenames: FEATURE_DATA_MRW, *PFEATURE_DATA_MRW
---

# _FEATURE_DATA_MRW structure
The FEATURE_DATA_MRW structure contains information about the MRW feature.

## Syntax
```
typedef struct _FEATURE_DATA_MRW {
  FEATURE_HEADER Header;
  UCHAR  : 1     Write;
  UCHAR  : 1     DvdPlusRead;
  UCHAR  : 1     DvdPlusWrite;
  UCHAR  : 5     Reserved01;
  UCHAR          Reserved2[3];
} *PFEATURE_DATA_MRW, FEATURE_DATA_MRW;
```

## Members


`Header`

Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor.

`Write`

Indicates, if set to 1, that the device can format discs using the MRW format and write to discs that have been formatted in this manner. See the <i>SCSI Multimedia - 4 (MMC-4)</i> specification for more information.

`DvdPlusRead`



`DvdPlusWrite`



`Reserved01`



`Reserved2`

Reserved.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddmmc.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
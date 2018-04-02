---
UID: NS:ata._IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO
title: "_IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO"
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\identify_device_data_log_page_zoned_device_info.htm
old-project: storage
ms.assetid: 2F0B6C1F-54CC-47CF-B0D0-A53FAB80AF91
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO structure [Storage Devices], PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO structure pointer [Storage Devices], _IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, ata/IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, ata/PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, storage.identify_device_data_log_page_zoned_device_info"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ata.h
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
-	Ata.h
api_name:
-	IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO
product:
- Windows
targetos: Windows
req.typenames: IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, *PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO
---

# _IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]


<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>

## Syntax
```
typedef struct _IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO {
  IDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER Header;
  struct {
    ULONGLONG  : 62 Reserved;
    ULONGLONG  : 1  URSWRZ;
    ULONGLONG  : 1  Valid;
  } ZonedDeviceCapabilities;
  struct {
    ULONGLONG  : 63 Reserved;
    ULONGLONG  : 1  Valid;
  } ZonedDeviceSettings;
  struct {
    ULONGLONG  : 32 Number;
    ULONGLONG  : 31 Reserved;
    ULONGLONG  : 1  Valid;
  } OptimalNumberOfOpenSequentialWritePreferredZones;
  struct {
    ULONGLONG  : 32 Number;
    ULONGLONG  : 31 Reserved;
    ULONGLONG  : 1  Valid;
  } OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZones;
  struct {
    ULONGLONG  : 32 Number;
    ULONGLONG  : 31 Reserved;
    ULONGLONG  : 1  Valid;
  } MaxNumberOfOpenSequentialWriteRequiredZones;
  struct {
    ULONGLONG  : 47 Reserved0;
    ULONGLONG  : 1  Valid;
    ULONGLONG  : 16 ZacMinorVersion;
  } Version;
  UCHAR                                Reserved[456];
} IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, *PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO;
```

## Members


`Header`

N/A

`ZonedDeviceCapabilities`

#### URSWRZ

N/A



#### Reserved

N/A



#### Valid

N/A

`ZonedDeviceSettings`

#### Reserved

N/A



#### Valid

N/A

`OptimalNumberOfOpenSequentialWritePreferredZones`

#### Number

N/A



#### Reserved

N/A



#### Valid

N/A

`OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZones`

#### Number

N/A



#### Reserved

N/A



#### Valid

N/A

`MaxNumberOfOpenSequentialWriteRequiredZones`

#### Number

N/A



#### Reserved

N/A



#### Valid

N/A

`Version`

#### ZacMinorVersion

N/A



#### Reserved0

N/A



#### Valid

N/A

`Reserved`

N/A


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ata.h |
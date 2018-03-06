---
UID: NS:ntddstor._STORAGE_HW_FIRMWARE_SLOT_INFO
title: "_STORAGE_HW_FIRMWARE_SLOT_INFO"
author: windows-driver-content
description: This structure contains information about a slot on a device.
old-location: storage\storage_hw_firmware_slot_info.htm
old-project: storage
ms.assetid: D5DF9785-83E0-4137-8E5F-357F94721CAD
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PSTORAGE_HW_FIRMWARE_SLOT_INFO, PSTORAGE_HW_FIRMWARE_SLOT_INFO, PSTORAGE_HW_FIRMWARE_SLOT_INFO structure pointer [Storage Devices], STORAGE_HW_FIRMWARE_SLOT_INFO, STORAGE_HW_FIRMWARE_SLOT_INFO structure [Storage Devices], _STORAGE_HW_FIRMWARE_SLOT_INFO, ntddstor/PSTORAGE_HW_FIRMWARE_SLOT_INFO, ntddstor/STORAGE_HW_FIRMWARE_SLOT_INFO, storage.storage_hw_firmware_slot_info"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	ntddstor.h
api_name:
-	STORAGE_HW_FIRMWARE_SLOT_INFO
product: Windows
targetos: Windows
req.typenames: STORAGE_HW_FIRMWARE_SLOT_INFO, *PSTORAGE_HW_FIRMWARE_SLOT_INFO
---

# _STORAGE_HW_FIRMWARE_SLOT_INFO structure
This structure contains information about a slot on a device.

## Syntax
````
typedef struct _STORAGE_HW_FIRMWARE_SLOT_INFO {
  ULONG Version;
  ULONG Size;
  UCHAR SlotNumber;
  UCHAR ReadOnly  :1;
  UCHAR Reserved0  :7;
  UCHAR Reserved1[6];
  UCHAR Revision[STORAGE_HW_FIRMWARE_REVISION_LENGTH];
} STORAGE_HW_FIRMWARE_SLOT_INFO, *PSTORAGE_HW_FIRMWARE_SLOT_INFO;
````

## Members


`ReadOnly`

Indicates whether this slot is read-only or not.

`Reserved0`

Reserved for future use.

`Reserved1`

Reserved for future use.

`Revision`

The revision of the firmware on this slot.

`Size`

The size of this structure.

`SlotNumber`

The slot number of this slot.

`Version`

The version of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_SLOT_INFO)


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ntddstor.h (include Ntddstor.h) |
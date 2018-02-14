---
UID: NS:ntddstor._STORAGE_HW_FIRMWARE_INFO
title: "_STORAGE_HW_FIRMWARE_INFO"
author: windows-driver-content
description: This structure contains information about the device firmware.
old-location: storage\storage_hw_firmware_info.htm
old-project: storage
ms.assetid: 5A85A7EC-2333-4161-A1E7-55D3420E730C
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: storage.storage_hw_firmware_info, *PSTORAGE_HW_FIRMWARE_INFO, PSTORAGE_HW_FIRMWARE_INFO structure pointer [Storage Devices], ntddstor/PSTORAGE_HW_FIRMWARE_INFO, STORAGE_HW_FIRMWARE_INFO, PSTORAGE_HW_FIRMWARE_INFO, STORAGE_HW_FIRMWARE_INFO structure [Storage Devices], _STORAGE_HW_FIRMWARE_INFO, ntddstor/STORAGE_HW_FIRMWARE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddstor.h
apiname:
-	STORAGE_HW_FIRMWARE_INFO
product: Windows
targetos: Windows
req.typenames: STORAGE_HW_FIRMWARE_INFO, *PSTORAGE_HW_FIRMWARE_INFO
---

# _STORAGE_HW_FIRMWARE_INFO structure
This structure contains information about the device firmware.

## Syntax
````
typedef struct _STORAGE_HW_FIRMWARE_INFO {
  ULONG                         Version;
  ULONG                         Size;
  UCHAR                         SupportUpgrade  :1;
  UCHAR                         Reserved0  :7;
  UCHAR                         SlotCount;
  UCHAR                         ActiveSlot;
  UCHAR                         PendingActivateSlot;
  BOOLEAN                       FirmwareShared;
  UCHAR                         Reserved[3];
  ULONG                         ImagePayloadAlignment;
  ULONG                         ImagePayloadMaxSize;
  STORAGE_HW_FIRMWARE_SLOT_INFO Slot[ANYSIZE_ARRAY];
} STORAGE_HW_FIRMWARE_INFO, *PSTORAGE_HW_FIRMWARE_INFO;
````

## Members


`ActiveSlot`

The firmware slot containing the currently active/running firmware image.

`FirmwareShared`

Indicates that the firmware applies to both the device and controller/adapter, e.g. NVMe SSD.

`ImagePayloadAlignment`

The alignment of the image payload, in number of bytes. The maximum is PAGE_SIZE. The transfer size is a mutliple of this size. Some protocols require at least sector size. When this value is set to 0, this means that this value is invalid.

`ImagePayloadMaxSize`

The image payload maximum size, this is used for a single command.

`PendingActivateSlot`

The firmware slot that is pending activation.

`Reserved`

Reserved for future use.

`Reserved0`

Reserved for future use.

`Size`

The size of this structure as a buffer including slot.

`Slot`

Contains the slot information for each slot on the device.

`SlotCount`

The number of firmware slots on the device. This is the dimension of the Slot array.

<div class="alert"><b>Note</b>   Some devices can store more than 1 firmware image, if they have more than 1 firmware slot.</div>
<div> </div>

`SupportUpgrade`

Indicates that this firmware supports an upgrade.

`Version`

The version of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_INFO)


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ntddstor.h |
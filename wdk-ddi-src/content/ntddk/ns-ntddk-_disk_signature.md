---
UID: NS:ntddk._DISK_SIGNATURE
title: "_DISK_SIGNATURE"
author: windows-driver-content
description: DISK_SIGNATURE contains the disk signature information for a disk's partition table.
old-location: storage\disk_signature.htm
old-project: storage
ms.assetid: f3fdb436-53b6-4fb3-8746-1f852f7d928a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDISK_SIGNATURE, DISK_SIGNATURE, DISK_SIGNATURE structure [Storage Devices], PDISK_SIGNATURE, PDISK_SIGNATURE structure pointer [Storage Devices], _DISK_SIGNATURE, ntddk/DISK_SIGNATURE, ntddk/PDISK_SIGNATURE, storage.disk_signature, structs-disk_6ea56db7-c886-43f2-b9ed-24b0f7e1cb6e.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: This structure is only available on Windows XP and later.
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
-	ntddk.h
api_name:
-	DISK_SIGNATURE
product:
- Windows
targetos: Windows
req.typenames: DISK_SIGNATURE, *PDISK_SIGNATURE
---

# _DISK_SIGNATURE structure
DISK_SIGNATURE contains the disk signature information for a disk's partition table.

## Syntax
```
typedef struct _DISK_SIGNATURE {
  ULONG PartitionStyle;
  union {
    struct {
      ULONG Signature;
      ULONG CheckSum;
    } Mbr;
    struct {
      GUID DiskId;
    } Gpt;
  };
} DISK_SIGNATURE, *PDISK_SIGNATURE;
```

## Members


`PartitionStyle`

Specifies the type of partition.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff563773">PARTITION_STYLE</a> for a description of the possible values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This structure is only available on Windows XP and later. This structure is only available on Windows XP and later. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561447">IoReadDiskSignature</a>
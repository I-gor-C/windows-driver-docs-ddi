---
UID: NS:ntdddisk._DISK_PARTITION_INFO
title: "_DISK_PARTITION_INFO"
author: windows-driver-content
description: The DISK_PARTITION_INFO structure is used to report information about the disk's partition table.
old-location: storage\disk_partition_info.htm
old-project: storage
ms.assetid: 14df0604-39cd-4743-a051-894d63f4417c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDISK_PARTITION_INFO, DISK_PARTITION_INFO, DISK_PARTITION_INFO structure [Storage Devices], PDISK_PARTITION_INFO, PDISK_PARTITION_INFO structure pointer [Storage Devices], _DISK_PARTITION_INFO, ntdddisk/DISK_PARTITION_INFO, ntdddisk/PDISK_PARTITION_INFO, storage.disk_partition_info, structs-disk_307cbbb9-2940-4a87-b6b7-04e588811b8e.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
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
-	ntdddisk.h
api_name:
-	DISK_PARTITION_INFO
product:
- Windows
targetos: Windows
req.typenames: DISK_PARTITION_INFO, *PDISK_PARTITION_INFO
---

# _DISK_PARTITION_INFO structure
The <b>DISK_PARTITION_INFO</b> structure is used to report information about the disk's partition table.

## Syntax
```
typedef struct _DISK_PARTITION_INFO {
  ULONG           SizeOfPartitionInfo;
  PARTITION_STYLE PartitionStyle;
  union {
    struct {
      ULONG Signature;
      ULONG CheckSum;
    } Mbr;
    struct {
      GUID DiskId;
    } Gpt;
  } DUMMYUNIONNAME;
} *PDISK_PARTITION_INFO, DISK_PARTITION_INFO;
```

## Members


`SizeOfPartitionInfo`

Size of this structure in bytes. Set to <b>sizeof</b>(DISK_PARTITION_INFO).

`PartitionStyle`

Takes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563773">PARTITION_STYLE</a> enumerated value that specifies the type of partition table the disk contains.

`DUMMYUNIONNAME`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntdddisk.h (include Ntdddisk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552618">DISK_GEOMETRY_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563773">PARTITION_STYLE</a>
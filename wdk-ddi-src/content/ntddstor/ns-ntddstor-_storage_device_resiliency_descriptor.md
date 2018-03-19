---
UID: NS:ntddstor._STORAGE_DEVICE_RESILIENCY_DESCRIPTOR
title: "_STORAGE_DEVICE_RESILIENCY_DESCRIPTOR"
author: windows-driver-content
description: Reserved for system use.
old-location: storage\storage_device_resiliency_descriptor.htm
old-project: storage
ms.assetid: 71351CB7-1295-4797-802C-23A6B1C2C53F
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR, PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure pointer [Storage Devices], STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, STORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure [Storage Devices], _STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, ntddstor/PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR, ntddstor/STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, storage.storage_device_resiliency_descriptor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	STORAGE_DEVICE_RESILIENCY_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR
---

# _STORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure
Reserved for system use.

## Syntax
````
typedef struct _STORAGE_DEVICE_RESILIENCY_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG NameOffset;
  ULONG NumberOfLogicalCopies;
  ULONG NumberOfPhysicalCopies;
  ULONG PhysicalDiskRedundancy;
  ULONG NumberOfColumns;
  ULONG Interleave;
} STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, *PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR;
````

## Members


`Version`

Contains the size of this structure, in bytes. The value of this member will change as members are added to 
      the structure. Set to 
      <code>sizeof(STORAGE_DEVICE_RESILIENCY_DESCRIPTOR)</code>.

`Size`

Specifies the total size of the data returned, in bytes. This may include data that follows this 
      structure.

`NameOffset`

Byte offset to the null-terminated ASCII string containing the resiliency properties Name. For devices with 
      no Name property, this will be zero.

`NumberOfLogicalCopies`

Number of logical copies of data that are available.

`NumberOfPhysicalCopies`

Number of complete copies of data that are stored.

`PhysicalDiskRedundancy`

Number of disks that can fail without leading to data loss.

`NumberOfColumns`

Number of columns in the storage device.

`Interleave`

Size of a stripe unit of the storage device, in bytes. This is also referred to as the stripe width or 
      interleave of the storage device.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | ntddstor.h (include Ntddstor.h) |

## See Also

<a href="..\ntddstor\ni-ntddstor-ioctl_storage_query_property.md">IOCTL_STORAGE_QUERY_PROPERTY</a>
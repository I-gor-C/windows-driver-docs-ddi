---
UID: NS:ntddtape._TAPE_GET_MEDIA_PARAMETERS
title: "_TAPE_GET_MEDIA_PARAMETERS"
author: windows-driver-content
description: The TAPE_GET_MEDIA_PARAMETERS structure is used in conjunction with the TapeMiniGetMediaParameters routine to retrieve tape media parameters.
old-location: storage\tape_get_media_parameters.htm
old-project: storage
ms.assetid: 3e12c431-4f6d-4d07-be52-e4809e8bc798
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PTAPE_GET_MEDIA_PARAMETERS, PTAPE_GET_MEDIA_PARAMETERS, PTAPE_GET_MEDIA_PARAMETERS structure pointer [Storage Devices], TAPE_GET_MEDIA_PARAMETERS, TAPE_GET_MEDIA_PARAMETERS structure [Storage Devices], _TAPE_GET_MEDIA_PARAMETERS, ntddtape/PTAPE_GET_MEDIA_PARAMETERS, ntddtape/TAPE_GET_MEDIA_PARAMETERS, storage.tape_get_media_parameters, structs-tape_19ce668d-65dd-40d6-a668-d34e540cc686.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddtape.h
req.include-header: Ntddtape.h, Minitape.h
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
-	ntddtape.h
api_name:
-	TAPE_GET_MEDIA_PARAMETERS
product: Windows
targetos: Windows
req.typenames: TAPE_GET_MEDIA_PARAMETERS, *PTAPE_GET_MEDIA_PARAMETERS
---

# _TAPE_GET_MEDIA_PARAMETERS structure
The TAPE_GET_MEDIA_PARAMETERS structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567937">TapeMiniGetMediaParameters</a> routine to retrieve tape media parameters.

## Syntax
```
typedef struct _TAPE_GET_MEDIA_PARAMETERS {
  LARGE_INTEGER Capacity;
  LARGE_INTEGER Remaining;
  ULONG         BlockSize;
  ULONG         PartitionCount;
  BOOLEAN       WriteProtected;
} *PTAPE_GET_MEDIA_PARAMETERS, TAPE_GET_MEDIA_PARAMETERS;
```

## Members


`Capacity`

Indicates the total number of bytes of user data the tape can hold.

`Remaining`

Indicates the number of bytes from the current position to the end of the tape.

`BlockSize`

Indicates the block size, in bytes, or zero if the drive is using variable block size.

`PartitionCount`

Indicates the number of partitions on the tape. If the tape is not partitioned, <b>PartitionCount</b> is 1.

`WriteProtected`

Is set to <b>TRUE</b> if the tape is write-protected.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddtape.h (include Ntddtape.h, Minitape.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567937">TapeMiniGetMediaParameters</a>
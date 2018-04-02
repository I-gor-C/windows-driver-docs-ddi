---
UID: NS:ntddcdvd._AACS_READ_BINDING_NONCE
title: "_AACS_READ_BINDING_NONCE"
author: windows-driver-content
description: The AACS_READ_BINDING_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce.
old-location: storage\aacs_read_binding_nonce.htm
old-project: storage
ms.assetid: 5d017896-bb83-4ea3-9d28-b774213f86e9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PAACS_READ_BINDING_NONCE, AACS_READ_BINDING_NONCE, AACS_READ_BINDING_NONCE structure [Storage Devices], PAACS_READ_BINDING_NONCE, PAACS_READ_BINDING_NONCE structure pointer [Storage Devices], _AACS_READ_BINDING_NONCE, ntddcdvd/AACS_READ_BINDING_NONCE, ntddcdvd/PAACS_READ_BINDING_NONCE, storage.aacs_read_binding_nonce, structs-DVD_bc4b150f-5fa2-4c8d-b8fa-d3c3bf1c8639.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
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
-	ntddcdvd.h
api_name:
-	AACS_READ_BINDING_NONCE
product: Windows
targetos: Windows
req.typenames: AACS_READ_BINDING_NONCE, *PAACS_READ_BINDING_NONCE
---

# _AACS_READ_BINDING_NONCE structure
The AACS_READ_BINDING_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce.

## Syntax
```
typedef struct _AACS_READ_BINDING_NONCE {
  DVD_SESSION_ID SessionId;
  ULONG          NumberOfSectors;
  ULONGLONG      StartLba;
  union {
    ULONGLONG ForceStructureLengthToMatch64bit;
    HANDLE    Handle;
  };
} *PAACS_READ_BINDING_NONCE, AACS_READ_BINDING_NONCE;
```

## Members


`SessionId`

A value of type DVD_SESSION_ID that specifies an AGID. The client obtains this value by a successful call to IOCTL_AACS_START_SESSION.

`NumberOfSectors`

The number of sectors in the area for which the binding nonce is retrieved. To request the nonce for a file, the caller of IOCTL_AACS_READ_BINDING_NONCE must set this member to MAXULONGLONG.

`StartLba`

The starting logical block address of the area for which the binding nonce is retrieved. To request the nonce for a file, the caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a> must set this member to MAXULONGLONG.

## Remarks
Clients retrieve the binding nonce with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a> request or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a> request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550106">AACS_BINDING_NONCE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a>
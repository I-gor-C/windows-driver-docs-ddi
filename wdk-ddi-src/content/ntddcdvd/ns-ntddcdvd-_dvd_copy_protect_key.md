---
UID: NS:ntddcdvd._DVD_COPY_PROTECT_KEY
title: "_DVD_COPY_PROTECT_KEY"
author: windows-driver-content
description: The DVD_COPY_PROTECT_KEY structure is used in conjunction with the IOCTL_DVD_READ_KEY request to execute a report key command of the specified type.
old-location: storage\dvd_copy_protect_key.htm
old-project: storage
ms.assetid: 79f3fdaf-e23a-40ba-a1eb-5428a63cc96a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDVD_COPY_PROTECT_KEY, DVD_COPY_PROTECT_KEY, DVD_COPY_PROTECT_KEY structure [Storage Devices], PDVD_COPY_PROTECT_KEY, PDVD_COPY_PROTECT_KEY structure pointer [Storage Devices], _DVD_COPY_PROTECT_KEY, ntddcdvd/DVD_COPY_PROTECT_KEY, ntddcdvd/PDVD_COPY_PROTECT_KEY, storage.dvd_copy_protect_key, structs-DVD_3ea6aa08-28ce-42d0-855d-d2e83ce58f89.xml"
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
-	DVD_COPY_PROTECT_KEY
product: Windows
targetos: Windows
req.typenames: DVD_COPY_PROTECT_KEY, *PDVD_COPY_PROTECT_KEY
---

# _DVD_COPY_PROTECT_KEY structure
The <b>DVD_COPY_PROTECT_KEY</b> structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560425">IOCTL_DVD_READ_KEY</a> request to execute a report key command of the specified type.

## Syntax
```
typedef struct _DVD_COPY_PROTECT_KEY {
  ULONG          KeyLength;
  DVD_SESSION_ID SessionId;
  DVD_KEY_TYPE   KeyType;
  ULONG          KeyFlags;
  union {
    HANDLE        FileHandle;
    LARGE_INTEGER TitleOffset;
  } Parameters;
  UCHAR          KeyData[0];
} *PDVD_COPY_PROTECT_KEY, DVD_COPY_PROTECT_KEY;
```

## Members


`KeyLength`

Indicates the length of the key data to be retrieved.

`SessionId`

Indicates the DVD session ID. The Authentication Grant Identifier (AGID) for a secure Advanced Access Content System (AACS) session is a long integer in the range -1 to 3 inclusive.

`KeyType`

Indicates the key type. The DVD device driver uses this information to determine the key format in a report key command, as defined by the <i>SCSI Multimedia Commands - 3 (MMC-3)</i> specification. A report key command either reports key data for a specified key (challenge key, bus key, title key, RPC key, or disk key), reports the state of the authentication success flag (ASF), or invalidates an authentication grant ID (AGID). See the <i>MMC-3</i> specification for further information.

`KeyFlags`

######  This member can have any of the following values:



################

`Parameters`

#### FileHandle

Pointer to the file handle for the physical device that the copy protection is being negotiated on.



#### TitleOffset

Contains the logical block address on the media of the title.

The upper layers of the operating system use the <b>FileHandle</b> member. The file system converts the value in <b>FileHandle</b> into a logical block address and stores the result in the <b>TitleOffset</b> member. Kernel-mode drivers use the <b>TitleOffset</b> member.

`KeyData`

Contains the key data that was returned.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553731">DVD_KEY_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560425">IOCTL_DVD_READ_KEY</a>
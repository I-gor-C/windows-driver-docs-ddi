---
UID: NS:ntifs._FILE_LINK_ENTRY_INFORMATION
title: "_FILE_LINK_ENTRY_INFORMATION"
author: windows-driver-content
description: The FILE_LINK_ENTRY_INFORMATION structure describes a single NTFS hard link to an existing file.
old-location: ifsk\file_link_entry_information.htm
old-project: ifsk
ms.assetid: b42edb45-3f4f-4f65-aede-8f51149dda78
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFILE_LINK_ENTRY_INFORMATION, FILE_LINK_ENTRY_INFORMATION, FILE_LINK_ENTRY_INFORMATION structure [Installable File System Drivers], PFILE_LINK_ENTRY_INFORMATION, PFILE_LINK_ENTRY_INFORMATION structure pointer [Installable File System Drivers], _FILE_LINK_ENTRY_INFORMATION, ifsk.file_link_entry_information, ntifs/FILE_LINK_ENTRY_INFORMATION, ntifs/PFILE_LINK_ENTRY_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
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
-	ntifs.h
api_name:
-	FILE_LINK_ENTRY_INFORMATION
product: Windows
targetos: Windows
req.typenames: FILE_LINK_ENTRY_INFORMATION, *PFILE_LINK_ENTRY_INFORMATION
---

# _FILE_LINK_ENTRY_INFORMATION structure
The <b>FILE_LINK_ENTRY_INFORMATION</b> structure describes a single NTFS hard link to an existing file.

## Syntax
```
typedef struct _FILE_LINK_ENTRY_INFORMATION {
  ULONG    NextEntryOffset;
  LONGLONG ParentFileId;
  ULONG    FileNameLength;
  WCHAR    FileName[1];
} *PFILE_LINK_ENTRY_INFORMATION, FILE_LINK_ENTRY_INFORMATION;
```

## Members


`NextEntryOffset`

The offset, in bytes, to the next <b>FILE_LINK_ENTRY_INFORMATION</b> structure, or 0 if the current structure is the last  <b>FILE_LINK_ENTRY_INFORMATION</b> structure.

`ParentFileId`

The ID of the parent directory of the link.

`FileNameLength`

The length, in characters, of the <b>FileName</b> for the link.

`FileName`

The name of the link.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating system. Available in Windows Vista and later versions of the Windows operating system. |
| **Header** | ntifs.h (include FltKernel.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff728841">FILE_LINKS_INFORMATION</a>
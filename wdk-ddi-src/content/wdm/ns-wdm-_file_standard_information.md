---
UID: NS:wdm._FILE_STANDARD_INFORMATION
title: "_FILE_STANDARD_INFORMATION"
author: windows-driver-content
description: The FILE_STANDARD_INFORMATION structure is used as an argument to routines that query or set file information.
old-location: kernel\file_standard_information.htm
old-project: kernel
ms.assetid: 9ff7efec-4844-4abf-89c2-472afc959697
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PFILE_STANDARD_INFORMATION, FILE_STANDARD_INFORMATION, FILE_STANDARD_INFORMATION structure [Kernel-Mode Driver Architecture], PFILE_STANDARD_INFORMATION, PFILE_STANDARD_INFORMATION structure pointer [Kernel-Mode Driver Architecture], _FILE_STANDARD_INFORMATION, kernel.file_standard_information, kstruct_b_86abcab8-11e5-45de-983a-e78c6cb40a93.xml, wdm/FILE_STANDARD_INFORMATION, wdm/PFILE_STANDARD_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
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
req.irql: PASSIVE_LEVEL (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	FILE_STANDARD_INFORMATION
product: Windows
targetos: Windows
req.typenames: FILE_STANDARD_INFORMATION, *PFILE_STANDARD_INFORMATION
req.product: Windows 10 or later.
---

# _FILE_STANDARD_INFORMATION structure
The <b>FILE_STANDARD_INFORMATION</b> structure is used as an argument to routines that query or set file information.

## Syntax
```
typedef struct _FILE_STANDARD_INFORMATION {
  LARGE_INTEGER AllocationSize;
  LARGE_INTEGER EndOfFile;
  ULONG         NumberOfLinks;
  BOOLEAN       DeletePending;
  BOOLEAN       Directory;
} FILE_STANDARD_INFORMATION, *PFILE_STANDARD_INFORMATION;
```

## Members


`AllocationSize`

The file allocation size in bytes. Usually, this value is a multiple of the sector or cluster size of the underlying physical device.

`EndOfFile`

The end of file location as a byte offset.

`NumberOfLinks`

The number of hard links to the file.

`DeletePending`

The delete pending status. <b>TRUE</b> indicates that a file deletion has been requested.

`Directory`

The file directory status. <b>TRUE</b> indicates the file object represents a directory.

## Remarks
<b>EndOfFile</b> specifies the byte offset to the end of the file. Because this value is zero-based, it actually refers to the first free byte in the file; that is, it is the offset to the byte immediately following the last valid byte in the file.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
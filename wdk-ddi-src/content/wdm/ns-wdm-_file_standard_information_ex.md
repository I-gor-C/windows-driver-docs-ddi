---
UID: NS:wdm._FILE_STANDARD_INFORMATION_EX
title: "_FILE_STANDARD_INFORMATION_EX"
author: windows-driver-content
description: The FILE_STANDARD_INFORMATION_EX structure is used as an argument to routines that query or set file information.
old-location: kernel\file_standard_information_ex.htm
old-project: kernel
ms.assetid: 460ADE5A-0302-4695-A9E4-43B309738BE7
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PFILE_STANDARD_INFORMATION_EX, FILE_STANDARD_INFORMATION_EX, FILE_STANDARD_INFORMATION_EX structure [Kernel-Mode Driver Architecture], PFILE_STANDARD_INFORMATION_EX, PFILE_STANDARD_INFORMATION_EX structure pointer [Kernel-Mode Driver Architecture], _FILE_STANDARD_INFORMATION_EX, kernel.file_standard_information_ex, wdm/FILE_STANDARD_INFORMATION_EX, wdm/PFILE_STANDARD_INFORMATION_EX"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
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
req.irql: PASSIVE_LEVEL (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	FILE_STANDARD_INFORMATION_EX
product: Windows
targetos: Windows
req.typenames: FILE_STANDARD_INFORMATION_EX, *PFILE_STANDARD_INFORMATION_EX
req.product: Windows 10 or later.
---

# _FILE_STANDARD_INFORMATION_EX structure
The <b>FILE_STANDARD_INFORMATION_EX</b> structure is used as an argument to routines that query or set file information.

## Syntax
````
typedef struct _FILE_STANDARD_INFORMATION_EX {
  LARGE_INTEGER AllocationSize;
  LARGE_INTEGER EndOfFile;
  ULONG         NumberOfLinks;
  BOOLEAN       DeletePending;
  BOOLEAN       Directory;
  BOOLEAN       AlternateStream;
  BOOLEAN       MetadataAttribute;
} FILE_STANDARD_INFORMATION_EX, *PFILE_STANDARD_INFORMATION_EX;
````

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

`AlternateStream`

The alternate data stream status. <b>TRUE</b> indicates the file object represents an alternate data stream.

`MetadataAttribute`

The metadata attribute status. <b>TRUE</b> indicates the file object represents a metadata attribute.

## Remarks
<b>EndOfFile</b> specifies the byte offset to the end of the file. Because this value is zero-based, it actually refers to the first free byte in the file; that is, it is the offset to the byte immediately following the last valid byte in the file.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>



<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>



<a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>
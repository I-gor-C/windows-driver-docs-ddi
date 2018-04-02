---
UID: NS:ntifs._REPARSE_DATA_BUFFER
title: "_REPARSE_DATA_BUFFER"
author: windows-driver-content
description: The REPARSE_DATA_BUFFER structure contains reparse point data for a Microsoft reparse point.
old-location: ifsk\reparse_data_buffer.htm
old-project: ifsk
ms.assetid: e906a874-51f1-4623-8f0b-afdfd8169ab2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PREPARSE_DATA_BUFFER, PREPARSE_DATA_BUFFER, PREPARSE_DATA_BUFFER structure pointer [Installable File System Drivers], REPARSE_DATA_BUFFER, REPARSE_DATA_BUFFER structure [Installable File System Drivers], _REPARSE_DATA_BUFFER, fileinformationstructures_4f1b658e-1833-421f-a726-448b20b1c595.xml, ifsk.reparse_data_buffer, ntifs/PREPARSE_DATA_BUFFER, ntifs/REPARSE_DATA_BUFFER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
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
-	ntifs.h
api_name:
-	REPARSE_DATA_BUFFER
product: Windows
targetos: Windows
req.typenames: REPARSE_DATA_BUFFER, *PREPARSE_DATA_BUFFER
---

# _REPARSE_DATA_BUFFER structure
The REPARSE_DATA_BUFFER structure contains reparse point data for a Microsoft reparse point. (Third-party reparse point owners must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552014">REPARSE_GUID_DATA_BUFFER</a> structure instead.)

## Syntax
```
typedef struct _REPARSE_DATA_BUFFER {
  ULONG  ReparseTag;
  USHORT ReparseDataLength;
  USHORT Reserved;
  union {
    struct {
      USHORT SubstituteNameOffset;
      USHORT SubstituteNameLength;
      USHORT PrintNameOffset;
      USHORT PrintNameLength;
      ULONG  Flags;
      WCHAR  PathBuffer[1];
    } SymbolicLinkReparseBuffer;
    struct {
      USHORT SubstituteNameOffset;
      USHORT SubstituteNameLength;
      USHORT PrintNameOffset;
      USHORT PrintNameLength;
      WCHAR  PathBuffer[1];
    } MountPointReparseBuffer;
    struct {
      UCHAR DataBuffer[1];
    } GenericReparseBuffer;
  } DUMMYUNIONNAME;
} *PREPARSE_DATA_BUFFER, REPARSE_DATA_BUFFER;
```

## Members


`ReparseTag`

Reparse point tag. Must be a Microsoft reparse point tag. (See the following <b>Remarks</b> section.)

`ReparseDataLength`

Size, in bytes, of the reparse data in the <b>DataBuffer</b> member.

`Reserved`

Length, in bytes, of the unparsed portion of the file name pointed to by the <b>FileName</b> member of the associated file object. For more information about the <b>FileName</b> member, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a>. This member is only valid for create operations when the I/O fails with STATUS_REPARSE. For all other purposes, such as setting or querying a reparse point for the reparse data, this member is treated as reserved.

`DUMMYUNIONNAME`



## Remarks
The REPARSE_DATA_BUFFER structure is used by Microsoft file systems, filters, and minifilter drivers, as well as the I/O manager, to store data for a reparse point. 

This structure can only be used for Microsoft reparse points. Third-party reparse point owners must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552014">REPARSE_GUID_DATA_BUFFER</a> structure instead. 

Microsoft reparse points can use the REPARSE_DATA_BUFFER structure or the REPARSE_GUID_DATA_BUFFER structure. 

For more information about reparse point tags, see the Microsoft Windows SDK documentation. 

For more information about absolute and relative symbolic links, see Creating Symbolic Links in the Microsoft Windows SDK documentation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540354">FILE_REPARSE_POINT_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544705">FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544828">FSCTL_DELETE_REPARSE_POINT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544836">FSCTL_GET_REPARSE_POINT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545568">FSCTL_SET_REPARSE_POINT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542988">FltFsControlFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544589">FltTagFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550751">IRP_MJ_FILE_SYSTEM_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549452">IsReparseTagMicrosoft</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549462">IsReparseTagNameSurrogate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552014">REPARSE_GUID_DATA_BUFFER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566462">ZwFsControlFile</a>
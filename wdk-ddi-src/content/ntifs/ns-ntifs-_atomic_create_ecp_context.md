---
UID : NS:ntifs._ATOMIC_CREATE_ECP_CONTEXT
title : _ATOMIC_CREATE_ECP_CONTEXT
author : windows-driver-content
description : This structure allows supplemental operations to be performed on a file atomically during create.
old-location : ifsk\atomic_create_ecp_context.htm
old-project : ifsk
ms.assetid : CFA879CC-6124-4E1C-B440-358455A5E6EF
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _ATOMIC_CREATE_ECP_CONTEXT, *PATOMIC_CREATE_ECP_CONTEXT, ATOMIC_CREATE_ECP_CONTEXT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1607
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : ATOMIC_CREATE_ECP_CONTEXT
req.alt-loc : ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PATOMIC_CREATE_ECP_CONTEXT, ATOMIC_CREATE_ECP_CONTEXT"
---

# _ATOMIC_CREATE_ECP_CONTEXT structure
This structure allows supplemental
operations to be performed on a file atomically during create. Use the

## Syntax
````
typedef struct _ATOMIC_CREATE_ECP_CONTEXT {
  USHORT                                                           Size;
  USHORT                                                           InFlags;
  USHORT                                                           OutFlags;
  USHORT                                                           ReparseBufferLength;
  _Field_size_bytes_opt_(ReparseBufferLength) PREPARSE_DATA_BUFFER ReparseBuffer;
  LONGLONG                                                         FileSize;
  LONGLONG                                                         ValidDataLength;
#if (NTDDI_VERSION >= NTDDI_WIN10_RS2)
  PFILE_TIMESTAMPS                                                 FileTimestamps;
#endif 
#if (NTDDI_VERSION >= NTDDI_WIN10_RS3)
  ULONG                                                            FileAttributes;
  ULONG                                                            UsnSourceInfo;
  USN                                                              Usn;
#endif 
} ATOMIC_CREATE_ECP_CONTEXT, *PATOMIC_CREATE_ECP_CONTEXT;
````

## Members

        
            `FileAttributes`

            Specifies the attributes of a file.
        
            `FileSize`

            The optional value that is used with <b>ATOMIC_CREATE_ECP_IN_FLAG_EOF_SPECIFIED</b> to indicate the requested file size to be set on the file.
        
            `FileTimestamps`

            Pointer to an optional <a href="..\ntifs\ns-ntifs-_file_timestamps.md">FILE_TIMESTAMPS</a> structure which contains  the last recorded instance of specific actions on a file.
        
            `InFlags`

            Flags that indicate the requested supplemental operation(s) to be performed with the create operation.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `OutFlags`

            Flags that indicate the actual supplemental operation(s) performed with a successful create operation.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `ReparseBuffer`

            The optional value that indicates the type of buffer used in the create operation. Possible values are <b>REPARSE_DATA_BUFFER</b> or <b>REPARSE_GUID_DATA_BUFFER</b>.
        
            `ReparseBufferLength`

            The length of the <b>ReparseBuffer</b> member. This value can't exceed the <b>MAXIMUM_REPARSE_DATA_BUFFER_SIZE</b> (16K).
        
            `Size`

            The size of the context structure.
        
            `Usn`

            Specifies the Update Sequence Number (USN). This value is filled at the end of <b>GUID_ECP_ATOMIC_CREATE</b> .
        
            `UsnSourceInfo`

            Specifies optional Update Sequence Number (USN) source info flags.
        
            `ValidDataLength`

            The optional value that is used with <b>ATOMIC_CREATE_ECP_IN_FLAG_VDL_SPECIFIED</b> to indicate the requested valid data length to be set on the file.

    ## Remarks
        The GUID used for this structure is the <b>GUID_ECP_ATOMIC_CREATE</b> (<code>4720bd83-52ac-4104-a130-d1ec6a8cc8e5</code>).</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h |
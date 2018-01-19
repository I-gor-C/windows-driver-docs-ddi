---
UID : NS:ntddk._WHEA_GENERIC_ERROR_DATA_ENTRY_V2
title : _WHEA_GENERIC_ERROR_DATA_ENTRY_V2
author : windows-driver-content
description : The WHEA_GENERIC_ERROR_DATA_ENTRY structure describes an error data section in a generic error status block.
old-location : whea\whea_generic_error_data_entry.htm
old-project : whea
ms.assetid : 86834d99-34bd-487a-bbd4-4c0143d849a0
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_GENERIC_ERROR_DATA_ENTRY_V2, *PWHEA_GENERIC_ERROR_DATA_ENTRY_V2, *PWHEA_GENERIC_ERROR_DATA_ENTRY, WHEA_GENERIC_ERROR_DATA_ENTRY_V2, WHEA_GENERIC_ERROR_DATA_ENTRY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WHEA_GENERIC_ERROR_DATA_ENTRY
req.alt-loc : ntddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PWHEA_GENERIC_ERROR_DATA_ENTRY_V2, *PWHEA_GENERIC_ERROR_DATA_ENTRY, WHEA_GENERIC_ERROR_DATA_ENTRY_V2, WHEA_GENERIC_ERROR_DATA_ENTRY"
---

# _WHEA_GENERIC_ERROR_DATA_ENTRY_V2 structure
The WHEA_GENERIC_ERROR_DATA_ENTRY structure describes an error data section in a generic error status block.

## Syntax
````
typedef struct _WHEA_GENERIC_ERROR_DATA_ENTRY {
  GUID                SectionType;
  WHEA_ERROR_SEVERITY ErrorSeverity;
  WHEA_REVISION       Revision;
  UCHAR               ValidBits;
  UCHAR               Flags;
  ULONG               ErrorDataLength;
  GUID                FRUId;
  UCHAR               FRUText[20];
  UCHAR               Data[1];
} WHEA_GENERIC_ERROR_DATA_ENTRY, *PWHEA_GENERIC_ERROR_DATA_ENTRY;
````

## Members

        
            `Data`

            A variable-sized buffer that contains the error data for the error data section. The format of the data that is contained in this buffer is determined by the section type that is specified in the <b>SectionType</b> member.
        
            `ErrorDataLength`

            The length, in bytes, of the error data that is contained in the <b>Data</b> member.
        
            `ErrorSeverity`

            A <a href="..\ntddk\ne-ntddk-_whea_error_severity.md">WHEA_ERROR_SEVERITY</a>-typed value that indicates the severity of the error condition that is described by the error data section.
        
            `Flags`

            A bitwise OR'ed combination of values that describes the error data section. Possible values are:
        
            `FRUId`

            A GUID that identifies the Field Replaceable Unit (FRU) that contains the hardware where the error occurred. This member contains valid data only if the <b>0x01</b> bit is set in the <b>ValidBits</b> member.
        
            `FRUText`

            A character string that identifies the Field Replaceable Unit (FRU) that contains the hardware where the error occurred. This member contains valid data only if the <b>0x02</b> bit is set in the <b>ValidBits</b> member.
        
            `Revision`

            A <a href="..\ntddk\ns-ntddk-_whea_revision.md">WHEA_REVISION</a> union that describes the revision level of the WHEA_GENERIC_ERROR_DATA_ENTRY structure.
        
            `SectionType`

            A GUID that identifies the type of error data that is contained in the error data section. The standard section types are defined as follows:
        
            `ValidBits`

            A bitwise OR'ed combination of values that specifies which members of this structure contain valid data. Possible values are:

    ## Remarks
        A generic error status block can contain one or more WHEA_GENERIC_ERROR_DATA_ENTRY structures. Each WHEA_GENERIC_ERROR_DATA_ENTRY structure describes a section of error information that is part of the error status data for a generic error source.

The <b>Data</b> member of the <a href="..\ntddk\ns-ntddk-_whea_generic_error.md">WHEA_GENERIC_ERROR</a> structure contains a generic error status block that contains the WHEA_GENERIC_ERROR_DATA_ENTRY structures. The number of WHEA_GENERIC_ERROR_DATA_ENTRY structures that are included in the generic error status block is specified by the <b>ErrorDataEntryCount</b> member of the <a href="..\ntddk\ns-ntddk-_whea_generic_error_blockstatus.md">WHEA_GENERIC_ERROR_BLOCKSTATUS</a> union.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_generic_error.md">WHEA_GENERIC_ERROR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_generic_error_blockstatus.md">WHEA_GENERIC_ERROR_BLOCKSTATUS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_GENERIC_ERROR_DATA_ENTRY structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
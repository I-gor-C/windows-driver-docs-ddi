---
UID : NS:ntddk._WHEA_ERROR_RECORD_HEADER
title : _WHEA_ERROR_RECORD_HEADER
author : windows-driver-content
description : The WHEA_ERROR_RECORD_HEADER structure describes general information about a hardware error condition.
old-location : whea\whea_error_record_header.htm
old-project : whea
ms.assetid : 2e6476c7-d096-4756-bebb-56fe559dce6d
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_ERROR_RECORD_HEADER, *PWHEA_ERROR_RECORD_HEADER, WHEA_ERROR_RECORD_HEADER
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
req.alt-api : WHEA_ERROR_RECORD_HEADER
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
req.typenames : "*PWHEA_ERROR_RECORD_HEADER, WHEA_ERROR_RECORD_HEADER"
---

# _WHEA_ERROR_RECORD_HEADER structure
The WHEA_ERROR_RECORD_HEADER structure describes general information about a hardware error condition.

## Syntax
````
typedef struct _WHEA_ERROR_RECORD_HEADER {
  ULONG                              Signature;
  WHEA_REVISION                      Revision;
  ULONG                              SignatureEnd;
  USHORT                             SectionCount;
  WHEA_ERROR_SEVERITY                Severity;
  WHEA_ERROR_RECORD_HEADER_VALIDBITS ValidBits;
  ULONG                              Length;
  WHEA_TIMESTAMP                     Timestamp;
  GUID                               PlatformId;
  GUID                               PartitionId;
  GUID                               CreatorId;
  GUID                               NotifyType;
  ULONGLONG                          RecordId;
  WHEA_ERROR_RECORD_HEADER_FLAGS     Flags;
  WHEA_PERSISTENCE_INFO              PersistenceInfo;
  UCHAR                              Reserved[12];
} WHEA_ERROR_RECORD_HEADER, *PWHEA_ERROR_RECORD_HEADER;
````

## Members

        
            `CreatorId`

            A GUID that identifies the entity that created the error record. When the Windows kernel creates an error record, it sets this member to WHEA_RECORD_CREATOR_GUID.
        
            `Flags`

            A WHEA_ERROR_RECORD_HEADER_FLAGS union that describes the error condition. The WHEA_ERROR_RECORD_HEADER_FLAGS union is defined as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_ERROR_RECORD_HEADER_FLAGS {
  struct {
    ULONG  Recovered:1;
    ULONG  PreviousError:1;
    ULONG  Simulated:1;
    ULONG  Reserved:29;
  };
  ULONG  AsULONG;
} WHEA_ERROR_RECORD_HEADER_FLAGS, *PWHEA_ERROR_RECORD_HEADER_FLAGS;</pre>
</td>
</tr>
</table></span></div>
        
            `Length`

            The length, in bytes, of the error record.
        
            `NotifyType`

            A GUID that identifies the notification mechanism by which an error condition is reported to the operating system. The following are the GUIDs for the standard notification types:
        
            `PartitionId`

            A GUID that identifies the partition on which the hardware error occurred. This member contains valid data only if the <b>ValidBits.PartitionId</b> bit is set.
        
            `PersistenceInfo`

            A <a href="..\ntddk\ns-ntddk-_whea_persistence_info.md">WHEA_PERSISTENCE_INFO</a> union that is used by the error record persistence interface.
        
            `PlatformId`

            A GUID that identifies the platform on which the hardware error occurred. This member contains valid data only if the <b>ValidBits.PlatformId</b> bit is set.
        
            `RecordId`

            The identifier of the error record. This identifier is unique only on the system that created the error record.
        
            `Reserved`

            Reserved for system use.
        
            `Revision`

            A <a href="..\ntddk\ns-ntddk-_whea_revision.md">WHEA_REVISION</a> union that describes the revision level of the WHEA_ERROR_RECORD_HEADER structure.
        
            `SectionCount`

            The number of sections of error information that are contained in the error record.
        
            `Severity`

            A <a href="..\ntddk\ne-ntddk-_whea_error_severity.md">WHEA_ERROR_SEVERITY</a>-typed value that indicates the severity of the error condition described by the error record.
        
            `Signature`

            The signature of the error record. This member contains the value 'REPC'.
        
            `SignatureEnd`

            The end of the signature of the error record. This member contains the value 0xFFFFFFFF.
        
            `Timestamp`

            A <a href="..\ntddk\ns-ntddk-_whea_timestamp.md">WHEA_TIMESTAMP</a> union that indicates the time that the error was reported to the operating system. This member contains valid data only if the <b>ValidBits.Timestamp</b> bit is set.
        
            `ValidBits`

            A <a href="..\ntddk\ns-ntddk-_whea_error_record_header_validbits.md">WHEA_ERROR_RECORD_HEADER_VALIDBITS</a> union that specifies which members of the WHEA_ERROR_RECORD_HEADER structure contain valid data.

    ## Remarks
        A WHEA_ERROR_RECORD_HEADER structure is contained within the <a href="..\ntddk\ns-ntddk-_whea_error_record.md">WHEA_ERROR_RECORD</a> structure. The WHEA_ERROR_RECORD_HEADER structure describes general information about the hardware error condition that is described by the error record.

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
<a href="..\ntddk\ns-ntddk-_whea_error_record.md">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_error_record_header_validbits.md">WHEA_ERROR_RECORD_HEADER_VALIDBITS</a>
</dt>
<dt>
<a href="..\ntddk\ne-ntddk-_whea_error_severity.md">WHEA_ERROR_SEVERITY</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_persistence_info.md">WHEA_PERSISTENCE_INFO</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_revision.md">WHEA_REVISION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_timestamp.md">WHEA_TIMESTAMP</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_RECORD_HEADER structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
---
UID : NS:ntddk._WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
title : _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
author : windows-driver-content
description : The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure describes a section of error information that is part of an error record.
old-location : whea\whea_error_record_section_descriptor.htm
old-project : whea
ms.assetid : f1abbf2b-19c9-4d34-9975-4f7ab98792af
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR, WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
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
req.alt-api : WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
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
req.typenames : "*PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR, WHEA_ERROR_RECORD_SECTION_DESCRIPTOR"
---

# _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure
The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure describes a section of error information that is part of an <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>.

## Syntax
````
typedef struct _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR {
  ULONG                                          SectionOffset;
  ULONG                                          SectionLength;
  WHEA_REVISION                                  Revision;
  WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS ValidBits;
  UCHAR                                          Reserved;
  WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS     Flags;
  GUID                                           SectionType;
  GUID                                           FRUId;
  WHEA_ERROR_SEVERITY                            SectionSeverity;
  CCHAR                                          FRUText[20];
} WHEA_ERROR_RECORD_SECTION_DESCRIPTOR, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR;
````

## Members

        
            `Flags`

            A WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS union that describes the error record section. The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS union is defined as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS {
  struct {
    ULONG  Primary:1;
    ULONG  ContainmentWarning:1;
    ULONG  Reset:1;
    ULONG  ThresholdExceeded:1;
    ULONG  ResourceNotAvailable:1;
    ULONG  LatentError:1;
    ULONG  Reserved:26;
  };
  ULONG  AsULONG;
} WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS;</pre>
</td>
</tr>
</table></span></div>
        
            `FRUId`

            A GUID that identifies the Field Replaceable Unit (FRU) that contains the hardware where the error occurred. This member contains valid data only if the <b>ValidBits.FRUId</b> bit is set.
        
            `FRUText`

            A character string that identifies the Field Replaceable Unit (FRU) that contains the hardware where the error occurred. This member contains valid data only if the <b>ValidBits.FRUText</b> bit is set.
        
            `Reserved`

            Reserved for system use.
        
            `Revision`

            A <a href="..\ntddk\ns-ntddk-_whea_revision.md">WHEA_REVISION</a> union that describes the revision level of the WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure.
        
            `SectionLength`

            The length, in bytes, of the error data contained in the error record section.
        
            `SectionOffset`

            The offset, in bytes, from the beginning of the error record to the beginning of the error record section.
        
            `SectionSeverity`

            A <a href="..\ntddk\ne-ntddk-_whea_error_severity.md">WHEA_ERROR_SEVERITY</a>-typed value that indicates the severity of the error condition that is described by the error record section.
        
            `SectionType`

            A GUID that identifies the type of error data that is contained in the error record section. The standard section types are defined as follows:
        
            `ValidBits`

            A <a href="..\ntddk\ns-ntddk-_whea_error_record_section_descriptor_validbits.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS</a> union that specifies which members of this structure contain valid data.

    ## Remarks
        The <a href="..\ntddk\ns-ntddk-_whea_error_record.md">WHEA_ERROR_RECORD</a> structure contains an array of WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structures. Each descriptor describes a section of error information that is part of the error record.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_error_record.md">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_error_record_section_descriptor_validbits.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS</a>
</dt>
<dt>
<a href="..\ntddk\ne-ntddk-_whea_error_severity.md">WHEA_ERROR_SEVERITY</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_firmware_error_record_reference.md">WHEA_FIRMWARE_ERROR_RECORD_REFERENCE</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_processor_generic_error_section.md">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_memory_error_section.md">WHEA_MEMORY_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_nmi_error_section.md">WHEA_NMI_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_pciexpress_error_section.md">WHEA_PCIEXPRESS_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_pcixbus_error_section.md">WHEA_PCIXBUS_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_pcixdevice_error_section.md">WHEA_PCIXDEVICE_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_revision.md">WHEA_REVISION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-whea_xpf_processor_error_section.md">WHEA_XPF_PROCESSOR_ERROR_SECTION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
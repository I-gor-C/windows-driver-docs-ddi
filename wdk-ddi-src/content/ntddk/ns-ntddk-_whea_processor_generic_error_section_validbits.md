---
UID : NS:ntddk._WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS
title : _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS
author : windows-driver-content
description : The WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PROCESSOR_GENERIC_ERROR_SECTION structure contain valid data.
old-location : whea\whea_processor_generic_error_section_validbits.htm
old-project : whea
ms.assetid : f7173767-a177-4a79-917b-41acc9eff758
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS, *PWHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS, WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS, WHEA_GENERIC_PROCESSOR_ERROR_VALIDBITS, *PWHEA_GENERIC_PROCESSOR_ERROR_VALIDBITS
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
req.alt-api : WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS
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
req.typenames : "*PWHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS, WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS"
---

# _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS structure
The WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS union describes which members of a <a href="..\ntddk\ns-ntddk-_whea_processor_generic_error_section.md">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure contain valid data.

## Syntax
````
typedef union _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS {
  struct {
    ULONGLONG ProcessorType  :1;
    ULONGLONG InstructionSet  :1;
    ULONGLONG ErrorType  :1;
    ULONGLONG Operation  :1;
    ULONGLONG Flags  :1;
    ULONGLONG Level  :1;
    ULONGLONG CPUVersion  :1;
    ULONGLONG CPUBrandString  :1;
    ULONGLONG ProcessorId  :1;
    ULONGLONG TargetAddress  :1;
    ULONGLONG RequesterId  :1;
    ULONGLONG ResponderId  :1;
    ULONGLONG InstructionPointer  :1;
    ULONGLONG Reserved  :51;
  };
  ULONGLONG ValidBits;
} WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS, *PWHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS;
````

## Members

        
            `ValidBits`

            A ULONGLONG representation of the contents of the WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS union.

    ## Remarks
        A WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS union is contained within the <a href="..\ntddk\ns-ntddk-_whea_processor_generic_error_section.md">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure.

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
<a href="..\ntddk\ns-ntddk-_whea_processor_generic_error_section.md">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS union%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
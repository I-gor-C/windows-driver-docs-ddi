---
UID : NS:ntddk._WHEA_XPF_CONTEXT_INFO
title : _WHEA_XPF_CONTEXT_INFO
author : windows-driver-content
description : The WHEA_XPF_CONTEXT_INFO structure describes processor context information for an x86 or x64 processor.
old-location : whea\whea_xpf_context_info.htm
old-project : whea
ms.assetid : 044af92b-b77c-415c-9ca5-4436bfe497e5
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_XPF_CONTEXT_INFO, whea.whea_xpf_context_info, ntddk/PWHEA_XPF_CONTEXT_INFO, WHEA_XPF_CONTEXT_INFO structure [WHEA Drivers and Applications], PWHEA_XPF_CONTEXT_INFO, *PWHEA_XPF_CONTEXT_INFO, PWHEA_XPF_CONTEXT_INFO structure pointer [WHEA Drivers and Applications], whearef_3e1bae81-9b21-4b0c-bd86-b957afb95713.xml, WHEA_XPF_CONTEXT_INFO, ntddk/WHEA_XPF_CONTEXT_INFO
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PWHEA_XPF_CONTEXT_INFO, WHEA_XPF_CONTEXT_INFO"
---

# _WHEA_XPF_CONTEXT_INFO structure
The WHEA_XPF_CONTEXT_INFO structure describes processor context information for an x86 or x64 processor.

## Syntax
````
typedef struct _WHEA_XPF_CONTEXT_INFO {
  USHORT    RegisterContextType;
  USHORT    RegisterDataSize;
  ULONG     MSRAddress;
  ULONGLONG MmRegisterAddress;
  UCHAR     RegisterData[1];
} WHEA_XPF_CONTEXT_INFO, *PWHEA_XPF_CONTEXT_INFO;
````

## Members


`MmRegisterAddress`

The starting memory address of the memory mapped registers. This member contains valid data only if the <b>RegisterContextType</b> member is set to XPF_CONTEXT_INFO_MMREGISTERS. For all other types of processor context information, this member should contain zero.

`MSRAddress`

The starting address of the machine-specific registers. This member contains valid data only if the <b>RegisterContextType</b> member is set to either XPF_CONTEXT_INFO_UNCLASSIFIEDDATA or XPF_CONTEXT_INFO_MSRREGISTERS. For all other types of processor context information, this member should contain zero.

`RegisterContextType`

The type of processor context information described by the structure. Possible values are:

`RegisterDataSize`

The size, in bytes, of the register data that is contained in the <b>RegisterData</b> member.

## Remarks
The <b>VariableInfo</b> member of the <a href="..\ntddk\ns-ntddk-whea_xpf_processor_error_section.md">WHEA_XPF_PROCESSOR_ERROR_SECTION</a> structure contains zero or more WHEA_XPF_CONTEXT_INFO structures, each of which describes specific context information associated with the processor error that occurred. If the size of a particular WHEA_XPF_CONTEXT_INFO structure is not an even multiple of 16 bytes, the space that is allocated for the structure in the buffer will be padded with additional bytes that are set to zero to round the allocated space up to an even multiple of 16 bytes.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\ns-ntddk-_whea_x64_register_state.md">WHEA_X64_REGISTER_STATE</a>

<a href="..\ntddk\ns-ntddk-_whea_x86_register_state.md">WHEA_X86_REGISTER_STATE</a>

<a href="..\ntddk\ns-ntddk-whea_xpf_processor_error_section.md">WHEA_XPF_PROCESSOR_ERROR_SECTION</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_CONTEXT_INFO structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
---
UID : NS:ntddk._WHEA_ERROR_STATUS
title : _WHEA_ERROR_STATUS
author : windows-driver-content
description : The WHEA_ERROR_STATUS union describes generic error codes that are abstracted from the data contained in implementation-specific error registers.
old-location : whea\whea_error_status.htm
old-project : whea
ms.assetid : 5b11112b-e900-4894-a9ce-6895a4fa1956
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : PWHEA_ERROR_STATUS, ntddk/PWHEA_ERROR_STATUS, WHEA_ERROR_STATUS, PWHEA_ERROR_STATUS union pointer [WHEA Drivers and Applications], whea.whea_error_status, _WHEA_ERROR_STATUS, whearef_3dc93951-2c79-4b1e-b5b0-53ede31c6f37.xml, WHEA_ERROR_STATUS union [WHEA Drivers and Applications], *PWHEA_ERROR_STATUS, ntddk/WHEA_ERROR_STATUS
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
req.typenames : WHEA_ERROR_STATUS, *PWHEA_ERROR_STATUS
---

# _WHEA_ERROR_STATUS structure
The WHEA_ERROR_STATUS union describes generic error codes that are abstracted from the data contained in implementation-specific error registers.

## Syntax
````
typedef union _WHEA_ERROR_STATUS {
  ULONGLONG ErrorStatus;
  struct {
    ULONGLONG Reserved1  :8;
    ULONGLONG ErrorType  :8;
    ULONGLONG Address  :1;
    ULONGLONG Control  :1;
    ULONGLONG Data  :1;
    ULONGLONG Responder  :1;
    ULONGLONG Requester  :1;
    ULONGLONG FirstError  :1;
    ULONGLONG Overflow  :1;
    ULONGLONG Reserved2  :41;
  };
} WHEA_ERROR_STATUS, *PWHEA_ERROR_STATUS;
````

## Members


`DUMMYSTRUCTNAME`



`ErrorStatus`

A ULONGLONG representation of the contents of the WHEA_ERROR_STATUS union.

## Remarks
The WHEA_ERROR_STATUS union provides the capability to abstract information from implementation-specific error registers into generic error codes so that the operating system can process the errors without an intimate knowledge of the underlying platform. This union is derived from the Error Status section of the <a href="http://go.microsoft.com/fwlink/p/?linkid=26730">Intel Itanium Processor Family System Abstraction Layer Specification</a>.

A WHEA_ERROR_STATUS union is contained within the <a href="..\ntddk\ns-ntddk-_whea_memory_error_section.md">WHEA_MEMORY_ERROR_SECTION</a>, <a href="..\ntddk\ns-ntddk-_whea_pcixbus_error_section.md">WHEA_PCIXBUS_ERROR_SECTION</a>, and <a href="..\ntddk\ns-ntddk-_whea_pcixdevice_error_section.md">WHEA_PCIXDEVICE_ERROR_SECTION</a> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\ns-ntddk-_whea_pcixbus_error_section.md">WHEA_PCIXBUS_ERROR_SECTION</a>

<a href="..\ntddk\ns-ntddk-_whea_memory_error_section.md">WHEA_MEMORY_ERROR_SECTION</a>

<a href="..\ntddk\ns-ntddk-_whea_pcixdevice_error_section.md">WHEA_PCIXDEVICE_ERROR_SECTION</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_STATUS union%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
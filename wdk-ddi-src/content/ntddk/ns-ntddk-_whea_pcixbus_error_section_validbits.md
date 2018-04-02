---
UID: NS:ntddk._WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS
title: "_WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS"
author: windows-driver-content
description: The WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PCIXBUS_ERROR_SECTION structure contain valid data.
old-location: whea\whea_pcixbus_error_section_validbits.htm
old-project: whea
ms.assetid: 85f14500-9cf6-42a6-a302-0990b99ddb5f
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, *PWHEA_PCIXBUS_ERROR_VALIDBITS, PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union pointer [WHEA Drivers and Applications], WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union [WHEA Drivers and Applications], WHEA_PCIXBUS_ERROR_VALIDBITS, _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, ntddk/PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, ntddk/WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, whea.whea_pcixbus_error_section_validbits, whearef_a01d7635-52ac-4b47-98f9-b09601dce4ff.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddk.h
api_name:
-	WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS
product:
- Windows
targetos: Windows
req.typenames: WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, *PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS
---

# _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS structure
The WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union describes which members of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560583">WHEA_PCIXBUS_ERROR_SECTION</a> structure contain valid data.

## Syntax
```
typedef struct _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS {
  struct {
    ULONGLONG  : 1  BusAddress;
    ULONGLONG  : 1  BusCommand;
    ULONGLONG  : 1  BusData;
    ULONGLONG  : 1  BusId;
    ULONGLONG  : 1  CompleterId;
    ULONGLONG  : 1  ErrorStatus;
    ULONGLONG  : 1  ErrorType;
    ULONGLONG  : 1  RequesterId;
    ULONGLONG  : 55 Reserved;
    ULONGLONG  : 1  TargetId;
  } DUMMYSTRUCTNAME;
  ULONGLONG ValidBits;
} *PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS, WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS;
```

## Members


`DUMMYSTRUCTNAME`



`ValidBits`

A ULONGLONG representation of the contents of the WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union.

## Remarks
A WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560583">WHEA_PCIXBUS_ERROR_SECTION</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560583">WHEA_PCIXBUS_ERROR_SECTION</a>
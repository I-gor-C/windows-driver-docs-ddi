---
UID: NS:ntddk._WHEA_MEMORY_ERROR_SECTION_VALIDBITS
title: "_WHEA_MEMORY_ERROR_SECTION_VALIDBITS"
author: windows-driver-content
description: The WHEA_MEMORY_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_MEMORY_ERROR_SECTION structure contain valid data.
old-location: whea\whea_memory_error_section_validbits.htm
old-project: whea
ms.assetid: 53ac65ff-56fe-411d-b0d1-174fc875a786
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_MEMORY_ERROR_SECTION_VALIDBITS, *PWHEA_MEMORY_ERROR_VALIDBITS, PWHEA_MEMORY_ERROR_SECTION_VALIDBITS, PWHEA_MEMORY_ERROR_SECTION_VALIDBITS union pointer [WHEA Drivers and Applications], WHEA_MEMORY_ERROR_SECTION_VALIDBITS, WHEA_MEMORY_ERROR_SECTION_VALIDBITS union [WHEA Drivers and Applications], WHEA_MEMORY_ERROR_VALIDBITS, _WHEA_MEMORY_ERROR_SECTION_VALIDBITS, ntddk/PWHEA_MEMORY_ERROR_SECTION_VALIDBITS, ntddk/WHEA_MEMORY_ERROR_SECTION_VALIDBITS, whea.whea_memory_error_section_validbits, whearef_49eab340-c05f-4201-a45d-8602ec121ef3.xml"
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
-	WHEA_MEMORY_ERROR_SECTION_VALIDBITS
product: Windows
targetos: Windows
req.typenames: WHEA_MEMORY_ERROR_SECTION_VALIDBITS, *PWHEA_MEMORY_ERROR_SECTION_VALIDBITS
---

# _WHEA_MEMORY_ERROR_SECTION_VALIDBITS structure
The WHEA_MEMORY_ERROR_SECTION_VALIDBITS union describes which members of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560565">WHEA_MEMORY_ERROR_SECTION</a> structure contain valid data.

## Syntax
```
typedef struct _WHEA_MEMORY_ERROR_SECTION_VALIDBITS {
  struct {
    ULONGLONG  : 1  Bank;
    ULONGLONG  : 1  BitPosition;
    ULONGLONG  : 1  Card;
    ULONGLONG  : 1  Column;
    ULONGLONG  : 1  Device;
    ULONGLONG  : 1  ErrorStatus;
    ULONGLONG  : 1  ErrorType;
    ULONGLONG  : 1  Module;
    ULONGLONG  : 1  Node;
    ULONGLONG  : 1  PhysicalAddress;
    ULONGLONG  : 1  PhysicalAddressMask;
    ULONGLONG  : 1  RequesterId;
    ULONGLONG  : 1  ResponderId;
    ULONGLONG  : 1  Row;
    ULONGLONG  : 1  TargetId;
    ULONGLONG  : 49 Reserved;
  } DUMMYSTRUCTNAME;
  ULONGLONG ValidBits;
} WHEA_MEMORY_ERROR_SECTION_VALIDBITS, *PWHEA_MEMORY_ERROR_SECTION_VALIDBITS;
```

## Members


`DUMMYSTRUCTNAME`



`ValidBits`

A ULONGLONG representation of the contents of the WHEA_MEMORY_ERROR_SECTION_VALIDBITS union.

## Remarks
A WHEA_MEMORY_ERROR_SECTION_VALIDBITS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560565">WHEA_MEMORY_ERROR_SECTION</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560565">WHEA_MEMORY_ERROR_SECTION</a>
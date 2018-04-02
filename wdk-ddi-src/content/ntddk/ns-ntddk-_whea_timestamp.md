---
UID: NS:ntddk._WHEA_TIMESTAMP
title: "_WHEA_TIMESTAMP"
author: windows-driver-content
description: The WHEA_TIMESTAMP union describes the time that an error was reported to the operating system.
old-location: whea\whea_timestamp.htm
old-project: whea
ms.assetid: 70a6555d-1da9-4013-911a-4a9d011b0205
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_TIMESTAMP, PWHEA_TIMESTAMP, PWHEA_TIMESTAMP union pointer [WHEA Drivers and Applications], WHEA_TIMESTAMP, WHEA_TIMESTAMP union [WHEA Drivers and Applications], _WHEA_TIMESTAMP, ntddk/PWHEA_TIMESTAMP, ntddk/WHEA_TIMESTAMP, whea.whea_timestamp, whearef_d0fafe3b-0cea-4adf-a68a-b565e04ae258.xml"
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
-	WHEA_TIMESTAMP
product:
- Windows
targetos: Windows
req.typenames: WHEA_TIMESTAMP, *PWHEA_TIMESTAMP
---

# _WHEA_TIMESTAMP structure
The WHEA_TIMESTAMP union describes the time that an error was reported to the operating system.

## Syntax
```
typedef struct _WHEA_TIMESTAMP {
  struct {
    ULONGLONG  : 8 Century;
    ULONGLONG  : 8 Day;
    ULONGLONG  : 8 Hours;
    ULONGLONG  : 8 Minutes;
    ULONGLONG  : 8 Month;
    ULONGLONG  : 1 Precise;
    ULONGLONG  : 7 Reserved;
    ULONGLONG  : 8 Seconds;
    ULONGLONG  : 8 Year;
  } DUMMYSTRUCTNAME;
  LARGE_INTEGER AsLARGE_INTEGER;
} *PWHEA_TIMESTAMP, WHEA_TIMESTAMP;
```

## Members


`DUMMYSTRUCTNAME`



`AsLARGE_INTEGER`

A LARGE_INTEGER representation of the contents of the WHEA_TIMESTAMP union.

## Remarks
A WHEA_TIMESTAMP union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a>
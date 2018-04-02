---
UID: NS:ntddk._WHEA_GENERIC_ERROR_BLOCKSTATUS
title: "_WHEA_GENERIC_ERROR_BLOCKSTATUS"
author: windows-driver-content
description: The WHEA_GENERIC_ERROR_BLOCKSTATUS union indicates what kind of error data is reported in a generic error status block.
old-location: whea\whea_generic_error_blockstatus.htm
old-project: whea
ms.assetid: 38c8422d-7307-4acd-81f0-931d2e128cb9
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_GENERIC_ERROR_BLOCKSTATUS, PWHEA_GENERIC_ERROR_BLOCKSTATUS, PWHEA_GENERIC_ERROR_BLOCKSTATUS union pointer [WHEA Drivers and Applications], WHEA_GENERIC_ERROR_BLOCKSTATUS, WHEA_GENERIC_ERROR_BLOCKSTATUS union [WHEA Drivers and Applications], _WHEA_GENERIC_ERROR_BLOCKSTATUS, ntddk/PWHEA_GENERIC_ERROR_BLOCKSTATUS, ntddk/WHEA_GENERIC_ERROR_BLOCKSTATUS, whea.whea_generic_error_blockstatus, whearef_2137a60a-daff-4a33-a516-c9ae87e2f11c.xml"
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
-	WHEA_GENERIC_ERROR_BLOCKSTATUS
product:
- Windows
targetos: Windows
req.typenames: WHEA_GENERIC_ERROR_BLOCKSTATUS, *PWHEA_GENERIC_ERROR_BLOCKSTATUS
---

# _WHEA_GENERIC_ERROR_BLOCKSTATUS structure
The WHEA_GENERIC_ERROR_BLOCKSTATUS union indicates what kind of error data is reported in a generic error status block.

## Syntax
```
typedef struct _WHEA_GENERIC_ERROR_BLOCKSTATUS {
  struct {
    ULONG  : 1  CorrectableError;
    ULONG  : 10 ErrorDataEntryCount;
    ULONG  : 1  MultipleCorrectableErrors;
    ULONG  : 1  MultipleUncorrectableErrors;
    ULONG  : 18 Reserved;
    ULONG  : 1  UncorrectableError;
  } DUMMYSTRUCTNAME;
  ULONG  AsULONG;
} *PWHEA_GENERIC_ERROR_BLOCKSTATUS, WHEA_GENERIC_ERROR_BLOCKSTATUS;
```

## Members


`DUMMYSTRUCTNAME`



`AsULONG`

A ULONG representation of the contents of the WHEA_GENERIC_ERROR_BLOCKSTATUS union.

## Remarks
A WHEA_GENERIC_ERROR_BLOCKSTATUS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560524">WHEA_GENERIC_ERROR</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560524">WHEA_GENERIC_ERROR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560529">WHEA_GENERIC_ERROR_DATA_ENTRY</a>
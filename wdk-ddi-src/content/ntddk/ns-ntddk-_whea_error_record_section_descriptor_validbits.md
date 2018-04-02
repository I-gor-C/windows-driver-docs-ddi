---
UID: NS:ntddk._WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS
title: "_WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS"
author: windows-driver-content
description: The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union describes which members of a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure contain valid data.
old-location: whea\whea_error_record_section_descriptor_validbits.htm
old-project: whea
ms.assetid: 7d1f192b-75fe-4ee0-b162-401230299562
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union pointer [WHEA Drivers and Applications], WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union [WHEA Drivers and Applications], _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, ntddk/PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, ntddk/WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, whea.whea_error_record_section_descriptor_validbits, whearef_0e13e9d6-57cb-44bd-825e-d9cab5c138c8.xml"
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
-	WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS
product:
- Windows
targetos: Windows
req.typenames: WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS
---

# _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS structure
The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union describes which members of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure contain valid data.

## Syntax
```
typedef struct _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS {
  struct {
    UCHAR  : 1 FRUId;
    UCHAR  : 1 FRUText;
    UCHAR  : 6 Reserved;
  } DUMMYSTRUCTNAME;
  UCHAR  AsUCHAR;
} WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS;
```

## Members


`DUMMYSTRUCTNAME`



`AsUCHAR`

A UCHAR representation of the contents of the WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union.

## Remarks
A WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
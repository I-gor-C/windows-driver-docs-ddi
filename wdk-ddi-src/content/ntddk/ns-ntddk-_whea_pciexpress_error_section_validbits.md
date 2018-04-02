---
UID: NS:ntddk._WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS
title: "_WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS"
author: windows-driver-content
description: The WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PCIEXPRESS_ERROR_SECTION structure contain valid data.
old-location: whea\whea_pciexpress_error_section_validbits.htm
old-project: whea
ms.assetid: 1c4c3e9c-32a2-405a-b27d-98f8da715626
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, *PWHEA_PCIEXPRESS_ERROR_VALIDBITS, PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union pointer [WHEA Drivers and Applications], WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union [WHEA Drivers and Applications], WHEA_PCIEXPRESS_ERROR_VALIDBITS, _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, ntddk/PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, ntddk/WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, whea.whea_pciexpress_error_section_validbits, whearef_9b6e3f92-4939-401a-9da2-e2ece44b1e98.xml"
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
-	WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS
product: Windows
targetos: Windows
req.typenames: WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, *PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS
---

# _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS structure
The WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union describes which members of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560576">WHEA_PCIEXPRESS_ERROR_SECTION</a> structure contain valid data.

## Syntax
```
typedef struct _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS {
  struct {
    ULONGLONG  : 1  AerInfo;
    ULONGLONG  : 1  BridgeControlStatus;
    ULONGLONG  : 1  CommandStatus;
    ULONGLONG  : 1  DeviceId;
    ULONGLONG  : 1  DeviceSerialNumber;
    ULONGLONG  : 1  ExpressCapability;
    ULONGLONG  : 1  PortType;
    ULONGLONG  : 56 Reserved;
    ULONGLONG  : 1  Version;
  } DUMMYSTRUCTNAME;
  ULONGLONG ValidBits;
} WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS, *PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS;
```

## Members


`DUMMYSTRUCTNAME`



`ValidBits`

A ULONGLONG representation of the contents of the WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union.

## Remarks
A WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560576">WHEA_PCIEXPRESS_ERROR_SECTION</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560576">WHEA_PCIEXPRESS_ERROR_SECTION</a>
---
UID: NS:ntddk._WHEA_PERSISTENCE_INFO
title: "_WHEA_PERSISTENCE_INFO"
author: windows-driver-content
description: The WHEA_PERSISTENCE_INFO union describes data that is used by the error record persistence interface for storing an error record.
old-location: whea\whea_persistence_info.htm
old-project: whea
ms.assetid: ab429d1b-0b4d-4897-b5f0-73113d16758e
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_PERSISTENCE_INFO, PWHEA_PERSISTENCE_INFO, PWHEA_PERSISTENCE_INFO union pointer [WHEA Drivers and Applications], WHEA_PERSISTENCE_INFO, WHEA_PERSISTENCE_INFO union [WHEA Drivers and Applications], _WHEA_PERSISTENCE_INFO, ntddk/PWHEA_PERSISTENCE_INFO, ntddk/WHEA_PERSISTENCE_INFO, whea.whea_persistence_info, whearef_0c5f7bbf-fc55-4667-b97a-9b28ec014bb5.xml"
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
-	WHEA_PERSISTENCE_INFO
product: Windows
targetos: Windows
req.typenames: WHEA_PERSISTENCE_INFO, *PWHEA_PERSISTENCE_INFO
---

# _WHEA_PERSISTENCE_INFO structure
The WHEA_PERSISTENCE_INFO union describes data that is used by the error record persistence interface for storing an error record.

## Syntax
````
typedef union _WHEA_PERSISTENCE_INFO {
  struct {
    ULONGLONG Signature  :16;
    ULONGLONG Length  :24;
    ULONGLONG Identifier  :16;
    ULONGLONG Attributes  :2;
    ULONGLONG DoNotLog  :1;
    ULONGLONG Reserved  :5;
  };
  ULONGLONG AsULONGLONG;
} WHEA_PERSISTENCE_INFO, *PWHEA_PERSISTENCE_INFO;
````

## Members


`DUMMYSTRUCTNAME`



`AsULONGLONG`

A ULONGLONG representation of the contents of the WHEA_PERSISTENCE_INFO union.

## Remarks
A WHEA_PERSISTENCE_INFO union is contained within the <a href="..\ntddk\ns-ntddk-_whea_error_record_header.md">WHEA_ERROR_RECORD_HEADER</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\ns-ntddk-_whea_error_record_header.md">WHEA_ERROR_RECORD_HEADER</a>
---
UID: NS:ntddk._WHEA_REVISION
title: "_WHEA_REVISION"
author: windows-driver-content
description: The WHEA_REVISION union describes the revision of the error record data structures.
old-location: whea\whea_revision.htm
old-project: whea
ms.assetid: 4258f223-353a-4b6e-a93c-5742e5c1668b
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_REVISION, PWHEA_REVISION, PWHEA_REVISION union pointer [WHEA Drivers and Applications], WHEA_REVISION, WHEA_REVISION union [WHEA Drivers and Applications], _WHEA_REVISION, ntddk/PWHEA_REVISION, ntddk/WHEA_REVISION, whea.whea_revision, whearef_0572aecb-765a-4118-8df0-7b34922e79d9.xml"
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
-	WHEA_REVISION
product: Windows
targetos: Windows
req.typenames: WHEA_REVISION, *PWHEA_REVISION
---

# _WHEA_REVISION structure
The WHEA_REVISION union describes the revision of the error record data structures.

## Syntax
```
typedef struct _WHEA_REVISION {
  struct {
    UCHAR MajorRevision;
    UCHAR MinorRevision;
  } DUMMYSTRUCTNAME;
  USHORT AsUSHORT;
} *PWHEA_REVISION, WHEA_REVISION;
```

## Members


`DUMMYSTRUCTNAME`



`AsUSHORT`

A USHORT representation of the contents of the WHEA_REVISION union.

## Remarks
A WHEA_REVISION union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a> and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
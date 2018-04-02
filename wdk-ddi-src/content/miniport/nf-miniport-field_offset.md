---
UID: NF:miniport.FIELD_OFFSET
title: FIELD_OFFSET macro
author: windows-driver-content
description: The FIELD_OFFSET macro returns the byte offset of a named field in a known structure type.
old-location: kernel\field_offset.htm
old-project: kernel
ms.assetid: c792d021-3c64-4341-878c-08a7e163447c
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: FIELD_OFFSET, FIELD_OFFSET function [Kernel-Mode Driver Architecture], k106_d6f0b450-e99c-4dd7-94c5-f428e4b1d642.xml, kernel.field_offset, ntdef/FIELD_OFFSET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: miniport.h
req.include-header: Wdm.h, Ntddk.h, Miniport.h, Minitape.h, Scsi.h, Storport.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
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
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntdef.h
api_name:
-	FIELD_OFFSET
product: Windows
targetos: Windows
req.typenames: MEMORY_CACHING_TYPE
---


# FIELD_OFFSET function
The <b>FIELD_OFFSET</b> macro returns the byte offset of a named field in a known structure type.

## Syntax

```
void FIELD_OFFSET(
   type,
   field
);
```

## Parameters

`type`

TBD

`field`

TBD


## Return Value

None

## Remarks

Used by device driver writers to symbolically determine the offset of a known field in a known structure type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Desktop |
| **Header** | miniport.h (include Wdm.h, Ntddk.h, Miniport.h, Minitape.h, Scsi.h, Storport.h) |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a>
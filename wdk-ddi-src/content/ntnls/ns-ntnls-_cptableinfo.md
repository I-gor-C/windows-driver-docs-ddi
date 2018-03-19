---
UID: NS:ntnls._CPTABLEINFO
title: "_CPTABLEINFO"
author: windows-driver-content
description: Stores the NLS file formats.
old-location: kernel\cptableinfo.htm
old-project: kernel
ms.assetid: 20EE0017-760E-48A1-8658-2A0278843074
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PCPTABLEINFO, CPTABLEINFO, CPTABLEINFO structure [Kernel-Mode Driver Architecture], PCPTABLEINFO, PCPTABLEINFO structure pointer [Kernel-Mode Driver Architecture], _CPTABLEINFO, kernel.cptableinfo, ntnls/CPTABLEINFO, ntnls/PCPTABLEINFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntnls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntnls.h
api_name:
-	CPTABLEINFO
product: Windows
targetos: Windows
req.typenames: CPTABLEINFO, *PCPTABLEINFO
---

# _CPTABLEINFO structure
Stores the NLS file formats.

## Syntax
````
typedef struct _CPTABLEINFO {
  USHORT  CodePage;
  USHORT  MaximumCharacterSize;
  USHORT  DefaultChar;
  USHORT  UniDefaultChar;
  USHORT  TransDefaultChar;
  USHORT  TransUniDefaultChar;
  USHORT  DBCSCodePage;
  UCHAR   LeadByte[MAXIMUM_LEADBYTES];
  PUSHORT MultiByteTable;
  PVOID   WideCharTable;
  PUSHORT DBCSRanges;
  PUSHORT DBCSOffsets;
} CPTABLEINFO, *PCPTABLEINFO;
````

## Members


`CodePage`

Specifies the code page number.

`MaximumCharacterSize`

Specifies the maximum length in bytes of a character.

`DefaultChar`

Specifies the default character (MB).

`UniDefaultChar`

Specifies the default character (Unicode).

`TransDefaultChar`

Specifies the translation of the default character (Unicode).

`TransUniDefaultChar`

Specifies the translation of the Unicode default character (MB).

`DBCSCodePage`

Specifies non-zero for DBCS code pages.

`LeadByte`

Specifies the lead byte ranges.

`MultiByteTable`

Specifies a pointer to a MB translation table.

`WideCharTable`

Specifies a pointer to a WC translation table.

`DBCSRanges`

Specifies a pointer to DBCS ranges.

`DBCSOffsets`

Specifies a pointer to DBCS offsets.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntnls.h |
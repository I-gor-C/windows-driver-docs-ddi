---
UID: NF:ntifs.FsRtlTestAnsiCharacter
title: FsRtlTestAnsiCharacter macro
author: windows-driver-content
description: The FsRtlTestAnsiCharacter macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria.
old-location: ifsk\fsrtltestansicharacter.htm
old-project: ifsk
ms.assetid: b667f0c9-7746-432e-ae58-3fe5b48309e0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FsRtlTestAnsiCharacter, FsRtlTestAnsiCharacter function [Installable File System Drivers], fsrtlref_7ef89c09-f42e-433a-90bf-59452fd1b7c4.xml, ifsk.fsrtltestansicharacter, ntifs/FsRtlTestAnsiCharacter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
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
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	FsRtlTestAnsiCharacter
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# FsRtlTestAnsiCharacter function
The<b> FsRtlTestAnsiCharacter</b> macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria.

## Syntax

```
void FsRtlTestAnsiCharacter(
   C,
   DEFAULT_RET,
   WILD_OK,
   FLAGS
);
```

## Parameters

`C`

TBD

`DEFAULT_RET`

TBD

`WILD_OK`

TBD

`FLAGS`

TBD


## Return Value

None

## Remarks

For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntifs.h (include Ntifs.h) |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546731">FsRtlIsAnsiCharacterLegal</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546735">FsRtlIsAnsiCharacterLegalFat</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546761">FsRtlIsAnsiCharacterLegalHpfs</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546768">FsRtlIsAnsiCharacterLegalNtfs</a>
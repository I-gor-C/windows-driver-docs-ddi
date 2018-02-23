---
UID: NF:ntifs.FsRtlTestAnsiCharacter
title: FsRtlTestAnsiCharacter macro
author: windows-driver-content
description: The FsRtlTestAnsiCharacter macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria.
old-location: ifsk\fsrtltestansicharacter.htm
old-project: ifsk
ms.assetid: b667f0c9-7746-432e-ae58-3fe5b48309e0
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ifsk.fsrtltestansicharacter, FsRtlTestAnsiCharacter, fsrtlref_7ef89c09-f42e-433a-90bf-59452fd1b7c4.xml, FsRtlTestAnsiCharacter function [Installable File System Drivers], ntifs/FsRtlTestAnsiCharacter
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
req.lib: ntifs.h
req.dll: 
req.irql: Any level
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntifs.h
apiname:
-	FsRtlTestAnsiCharacter
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# FsRtlTestAnsiCharacter function
The<b> FsRtlTestAnsiCharacter</b> macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria.

## Syntax

````
BOOLEAN FsRtlTestAnsiCharacter(
   PSCHAR  *Character,
   BOOLEAN DefaultReturnValue,
   BOOLEAN WildCardsPermissible,
   UCHAR   Flags
);
````

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
| **Library** | ntifs.h |
| **IRQL** | Any level |

## See Also

<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegal.md">FsRtlIsAnsiCharacterLegal</a>



<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalfat.md">FsRtlIsAnsiCharacterLegalFat</a>



<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalntfs.md">FsRtlIsAnsiCharacterLegalNtfs</a>



<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalhpfs.md">FsRtlIsAnsiCharacterLegalHpfs</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlTestAnsiCharacter function%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
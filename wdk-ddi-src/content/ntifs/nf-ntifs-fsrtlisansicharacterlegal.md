---
UID: NF:ntifs.FsRtlIsAnsiCharacterLegal
title: FsRtlIsAnsiCharacterLegal macro
author: windows-driver-content
description: The FsRtlIsAnsiCharacterLegal macro determines whether a character is a legal ANSI character.
old-location: ifsk\fsrtlisansicharacterlegal.htm
old-project: ifsk
ms.assetid: e270e4a9-90dc-4e9b-abdf-079c331ad71c
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: FsRtlIsAnsiCharacterLegal, FsRtlIsAnsiCharacterLegal function [Installable File System Drivers], fsrtlref_dad0349c-b705-4a0a-a1ea-359517e65eae.xml, ifsk.fsrtlisansicharacterlegal, ntifs/FsRtlIsAnsiCharacterLegal
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
-	FsRtlIsAnsiCharacterLegal
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# FsRtlIsAnsiCharacterLegal function
The <b>FsRtlIsAnsiCharacterLegal</b> macro determines whether a character is a legal ANSI character.

## Syntax

````
BOOLEAN FsRtlIsAnsiCharacterLegal(
   SCHAR Character,
   UCHAR Flags
);
````

## Parameters

`C`

TBD

`FLAGS`

TBD


## Return Value

None

## Remarks

To be a legal ANSI character, a character must be present in the ANSI legal character array and must satisfy the input flag settings. 

For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntifs.h (include Ntifs.h) |
| **IRQL** | Any level |

## See Also

<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalntfs.md">FsRtlIsAnsiCharacterLegalNtfs</a>



<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalhpfs.md">FsRtlIsAnsiCharacterLegalHpfs</a>



<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalfat.md">FsRtlIsAnsiCharacterLegalFat</a>
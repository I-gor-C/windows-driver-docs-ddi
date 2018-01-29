---
UID : NF:ntifs.FsRtlIsAnsiCharacterLegal
title : FsRtlIsAnsiCharacterLegal macro
author : windows-driver-content
description : The FsRtlIsAnsiCharacterLegal macro determines whether a character is a legal ANSI character.
old-location : ifsk\fsrtlisansicharacterlegal.htm
old-project : ifsk
ms.assetid : e270e4a9-90dc-4e9b-abdf-079c331ad71c
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ntifs/FsRtlIsAnsiCharacterLegal, ifsk.fsrtlisansicharacterlegal, fsrtlref_dad0349c-b705-4a0a-a1ea-359517e65eae.xml, FsRtlIsAnsiCharacterLegal function [Installable File System Drivers], FsRtlIsAnsiCharacterLegal
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : ntifs.h
req.dll : 
req.irql : Any level
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
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
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** | Any level |
| **DDI compliance rules** |  |

## See Also

<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalhpfs.md">FsRtlIsAnsiCharacterLegalHpfs</a>

<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalntfs.md">FsRtlIsAnsiCharacterLegalNtfs</a>

<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegalfat.md">FsRtlIsAnsiCharacterLegalFat</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIsAnsiCharacterLegal function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
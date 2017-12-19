---
UID: NF.ntifs.FsRtlIsAnsiCharacterLegalFat
title: FsRtlIsAnsiCharacterLegalFat macro
author: windows-driver-content
description: The FsRtlIsAnsiCharacterLegalFat macro determines whether an ANSI character is legal for FAT file names.
old-location: ifsk\fsrtlisansicharacterlegalfat.htm
old-project: ifsk
ms.assetid: 4bbd50a8-1f1f-45d9-9b63-6c1576fe7b98
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlIsAnsiCharacterLegalFat
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
req.alt-api: FsRtlIsAnsiCharacterLegalFat
req.alt-loc: ntifs.h
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
---

# FsRtlIsAnsiCharacterLegalFat macro



## -description
The <b>FsRtlIsAnsiCharacterLegalFat</b> macro determines whether an ANSI character is legal for FAT file names.



## -syntax

````
BOOLEAN FsRtlIsAnsiCharacterLegalFat(
   PSCHAR  *Character,
   BOOLEAN WildCardsPermissible
);
````


## -parameters

### -param Character 

Pointer to the character to be tested.


### -param WildCardsPermissible 

Set to <b>TRUE</b> if wildcard characters are to be considered legal, <b>FALSE</b> otherwise.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtlisansicharacterlegal">FsRtlIsAnsiCharacterLegal</a>
</dt>
<dt>
<a href="ifsk.fsrtlisansicharacterlegalhpfs">FsRtlIsAnsiCharacterLegalHpfs</a>
</dt>
<dt>
<a href="ifsk.fsrtlisansicharacterlegalntfs">FsRtlIsAnsiCharacterLegalNtfs</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIsAnsiCharacterLegalFat function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


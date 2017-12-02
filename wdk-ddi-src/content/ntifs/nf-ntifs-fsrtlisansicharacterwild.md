---
UID: NF.ntifs.FsRtlIsAnsiCharacterWild
title: FsRtlIsAnsiCharacterWild
author: windows-driver-content
description: The FsRtlIsAnsiCharacterWild macro determines whether an ANSI character is a wildcard character.
old-location: ifsk\fsrtlisansicharacterwild.htm
old-project: ifsk
ms.assetid: badbc73a-44aa-4917-83a8-2ebd9f9ec576
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlIsAnsiCharacterWild
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIsAnsiCharacterWild
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
req.iface: 
---

# FsRtlIsAnsiCharacterWild function



## -description
<p>The <b>FsRtlIsAnsiCharacterWild</b> macro determines whether an ANSI character is a wildcard character.</p>


## -syntax

````
BOOLEAN FsRtlIsAnsiCharacterWild(
   PSCHAR *Character
);
````


## -parameters
<dl>

### -param Character 

<dd>
<p>Pointer to the character to be tested.</p>
</dd>
</dl>

## -returns
<p><b>FsRtlIsAnsiCharacterWild</b> returns <b>TRUE</b> if the character is a wildcard character, <b>FALSE</b> otherwise.</p>

## -remarks
<p>For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlisansicharacterlegal.md">FsRtlIsAnsiCharacterLegal</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlisunicodecharacterwild.md">FsRtlIsUnicodeCharacterWild</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIsAnsiCharacterWild function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

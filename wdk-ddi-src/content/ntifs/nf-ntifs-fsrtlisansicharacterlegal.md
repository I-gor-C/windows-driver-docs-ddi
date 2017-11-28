---
UID: NF.ntifs.FsRtlIsAnsiCharacterLegal
title: FsRtlIsAnsiCharacterLegal
author: windows-driver-content
description: The FsRtlIsAnsiCharacterLegal macro determines whether a character is a legal ANSI character.
old-location: ifsk\fsrtlisansicharacterlegal.htm
old-project: ifsk
ms.assetid: e270e4a9-90dc-4e9b-abdf-079c331ad71c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlIsAnsiCharacterLegal
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
req.alt-api: FsRtlIsAnsiCharacterLegal
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

# FsRtlIsAnsiCharacterLegal function



## -description
<p>The <b>FsRtlIsAnsiCharacterLegal</b> macro determines whether a character is a legal ANSI character.</p>


## -syntax

````
BOOLEAN FsRtlIsAnsiCharacterLegal(
   SCHAR Character,
   UCHAR Flags
);
````


## -parameters
<dl>

### -param <i>Character</i> 

<dd>
<p>The character to be tested.</p>
</dd>

### -param <i>Flags</i> 

<dd>
<p>Combination of one or more of the following flag values:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FSRTL_FAT_LEGAL</p>
</td>
<td>
<p>Valid characters for FAT file names are legal.</p>
</td>
</tr>
<tr>
<td>
<p>FSRTL_HPFS_LEGAL</p>
</td>
<td>
<p>Valid characters for high-performance file system (HPFS) file names are legal.</p>
</td>
</tr>
<tr>
<td>
<p>FSRTL_NTFS_LEGAL</p>
</td>
<td>
<p>Valid characters for NTFS file names are legal.</p>
</td>
</tr>
<tr>
<td>
<p>FSRTL_WILD_CHARACTER</p>
</td>
<td>
<p>Wildcard characters are legal.</p>
</td>
</tr>
<tr>
<td>
<p>FSRTL_OLE_LEGAL</p>
</td>
<td>
<p>Valid characters for NTFS stream names are legal. </p>
</td>
</tr>
<tr>
<td>
<p>FSRTL_NTFS_STREAM_LEGAL</p>
</td>
<td>
<p>FSRTL_NTFS_LEGAL | FSRTL_OLE_LEGAL</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>FsRtlIsAnsiCharacterLegal</b> returns <b>TRUE</b> if the character is a legal ANSI character, <b>FALSE</b> otherwise.</p>

## -remarks
<p>To be a legal ANSI character, a character must be present in the ANSI legal character array and must satisfy the input flag settings. </p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

<p>To be a legal ANSI character, a character must be present in the ANSI legal character array and must satisfy the input flag settings. </p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546735">FsRtlIsAnsiCharacterLegalFat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546761">FsRtlIsAnsiCharacterLegalHpfs</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546768">FsRtlIsAnsiCharacterLegalNtfs</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIsAnsiCharacterLegal function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

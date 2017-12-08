---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlIsDbcsInExpression~r1
title: FsRtlIsDbcsInExpression function
author: windows-driver-content
description: The FsRtlIsDbcsInExpression routine determines whether an ANSI or double-byte character set (DBCS) string matches the specified pattern.
old-location: ifsk\fsrtlisdbcsinexpression.htm
old-project: ifsk
ms.assetid: 87292b33-4b82-4ac5-b71b-523391e5fea2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlIsDbcsInExpression
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIsDbcsInExpression
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
---

# FsRtlIsDbcsInExpression function



## -description
The <b>FsRtlIsDbcsInExpression</b> routine determines whether an ANSI or double-byte character set (DBCS) string matches the specified pattern. 


## -syntax

````
BOOLEAN FsRtlIsDbcsInExpression(
  _In_ PANSI_STRING Expression,
  _In_ PANSI_STRING Name
);
````


## -parameters

### -param Expression [in]

A pointer to the pattern string. Can contain wildcard characters. 

### -param Name [in]

A pointer to the string to be compared against the pattern. Cannot contain wildcard characters. 

## -returns
<b>FsRtlIsDbcsInExpression</b> returns <b>TRUE</b> if the string matches the pattern, <b>FALSE</b> otherwise.

## -remarks
The following wildcard characters can be used in the pattern string.

* (asterisk)

Matches zero or more characters.

? (question mark)

Matches a single character.

ANSI_DOS_DOT

Matches either a period or zero characters beyond the name string.

ANSI_DOS_QM

Matches any single character or, upon encountering a period or end of name string, advances the expression to the end of the set of contiguous ANSI_DOS_QMs.

ANSI_DOS_STAR

Matches zero or more characters until encountering and matching the final . in the name.

Pattern matching is case sensitive. To perform a case-insensitive match, the caller must use a routine such as <a href="kernel.rtlupperstring">RtlUpperString</a> to convert the pattern and input strings to uppercase before calling <b>FsRtlIsDbcsInExpression</b>.

For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ansi_string">ANSI_STRING</a>
</dt>
<dt>
<a href="ifsk.fsrtlisnameinexpression">FsRtlIsNameInExpression</a>
</dt>
<dt>
<a href="kernel.rtlupperstring">RtlUpperString</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIsDbcsInExpression routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

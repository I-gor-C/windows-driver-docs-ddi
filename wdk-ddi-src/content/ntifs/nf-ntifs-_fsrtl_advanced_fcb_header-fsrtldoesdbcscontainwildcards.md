---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlDoesDbcsContainWildCards
title: FsRtlDoesDbcsContainWildCards function
author: windows-driver-content
description: The FsRtlDoesDbcsContainWildCards routine determines whether an ANSI or double-byte character set (DBCS) string contains wildcard characters.
old-location: ifsk\fsrtldoesdbcscontainwildcards.htm
old-project: ifsk
ms.assetid: 4a33014a-c980-4186-b7b2-68fda22fa152
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlDoesDbcsContainWildCards
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlDoesDbcsContainWildCards
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

# FsRtlDoesDbcsContainWildCards function



## -description
The <b>FsRtlDoesDbcsContainWildCards</b> routine determines whether an ANSI or double-byte character set (DBCS) string contains wildcard characters. 


## -syntax

````
BOOLEAN FsRtlDoesDbcsContainWildCards(
  _In_ PANSI_STRING Name
);
````


## -parameters

### -param Name [in]

A pointer to the string to be checked.

## -returns
The <b>FsRtlDoesDbcsContainWildCards</b> routine returns <b>TRUE</b> if one or more wildcard characters were found, <b>FALSE</b> otherwise.

## -remarks
The following are wildcard characters: *, ?, ANSI_DOS_STAR, ANSI_DOS_DOT, and ANSI_DOS_QM.

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
Version
</th>
<td width="70%">
This routine is available on Microsoft Windows 2000 and later versions of Windows operating systems. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlDoesDbcsContainWildCards routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

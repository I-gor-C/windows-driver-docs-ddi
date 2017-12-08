---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlDoesNameContainWildCards
title: FsRtlDoesNameContainWildCards function
author: windows-driver-content
description: The FsRtlDoesNameContainWildCards routine determines whether a Unicode string contains wildcard characters.
old-location: ifsk\fsrtldoesnamecontainwildcards.htm
old-project: ifsk
ms.assetid: a2bcf1c0-a6c7-4bf3-bce6-9a661f2ab2e1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlDoesNameContainWildCards
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
req.alt-api: FsRtlDoesNameContainWildCards
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
req.irql: PASSIVE_LEVEL
---

# FsRtlDoesNameContainWildCards function



## -description
The <b>FsRtlDoesNameContainWildCards</b> routine determines whether a Unicode string contains wildcard characters. 


## -syntax

````
BOOLEAN FsRtlDoesNameContainWildCards(
  _In_ PUNICODE_STRING Name
);
````


## -parameters

### -param Name [in]

A pointer to the string to be checked.

## -returns
<b>FsRtlDoesNameContainWildCards</b> returns <b>TRUE</b> if one or more wildcard characters were found, <b>FALSE</b> otherwise.

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
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlDoesNameContainWildCards routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

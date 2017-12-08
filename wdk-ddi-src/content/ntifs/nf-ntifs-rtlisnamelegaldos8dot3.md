---
UID: NF.ntifs.RtlIsNameLegalDOS8Dot3
title: RtlIsNameLegalDOS8Dot3 function
author: windows-driver-content
description: The RtlIsNameLegalDOS8Dot3 routine determines whether a given name represents a valid short (8.3) file name.
old-location: ifsk\rtlisnamelegaldos8dot3.htm
old-project: ifsk
ms.assetid: 27aa6bd1-c4e2-427e-a9e4-383d66fe2d61
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlIsNameLegalDOS8Dot3
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
req.alt-api: RtlIsNameLegalDOS8Dot3
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
req.irql: See Remarks section.
---

# RtlIsNameLegalDOS8Dot3 function



## -description
The <b>RtlIsNameLegalDOS8Dot3</b> routine determines whether a given name represents a valid short (8.3) file name. 


## -syntax

````
BOOLEAN RtlIsNameLegalDOS8Dot3(
  _In_      PCUNICODE_STRING Name,
  _Inout_   POEM_STRING      OemName,
  _Out_opt_ PBOOLEAN         NameContainsSpaces
);
````


## -parameters

### -param Name [in]

Pointer to a Unicode string containing the file name. 

### -param OemName [in, out]

Pointer to an optional caller-allocated buffer that receives a counted OEM string corresponding to the Unicode string at <i>Name</i>. 

### -param NameContainsSpaces [out, optional]

Pointer to an optional BOOLEAN value that receives <b>TRUE</b> if the string at <i>Name</i> contains embedded spaces, <b>FALSE</b> otherwise. This value is valid only if <b>RtlIsNameLegalDOS8Dot3</b> returns <b>TRUE</b>. 

## -returns
<b>RtlIsNameLegalDOS8Dot3</b> returns <b>TRUE</b> if the string at <i>Name</i> is a legal short (8.3) file name, <b>FALSE</b> otherwise.

## -remarks
<b>RtlIsNameLegalDOS8Dot3</b> translates the Unicode string at <i>Name</i> using the OEM code page that was installed as the current system code page at system boot time, and converts the translated string to uppercase. (If the caller supplied a buffer at <i>OemName</i>, this buffer receives the resulting string.) <b>RtlIsNameLegalDOS8Dot3</b> checks that the name is a properly formatted 8.3 name and contains only legal characters.

For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. 

If the block of memory at <i>Name</i> is nonpaged, the caller can be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, callers of <b>RtlIsNameLegalDOS8Dot3</b> must be running at IRQL &lt; DISPATCH_LEVEL. 

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
See Remarks section.
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.oem_string">OEM_STRING</a>
</dt>
<dt>
<a href="ifsk.rtlgenerate8dot3name">RtlGenerate8dot3Name</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlIsNameLegalDOS8Dot3 routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

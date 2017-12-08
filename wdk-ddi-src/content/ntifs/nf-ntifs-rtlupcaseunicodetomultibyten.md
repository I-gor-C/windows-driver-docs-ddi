---
UID: NF.ntifs.RtlUpcaseUnicodeToMultiByteN
title: RtlUpcaseUnicodeToMultiByteN function
author: windows-driver-content
description: The RtlUpcaseUnicodeToMultiByteN routine translates the specified Unicode string into a new uppercase character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set.
old-location: ifsk\rtlupcaseunicodetomultibyten.htm
old-project: ifsk
ms.assetid: a79a5d3b-ed1c-42fa-b491-0ad0b3dfc921
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlUpcaseUnicodeToMultiByteN
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
req.alt-api: RtlUpcaseUnicodeToMultiByteN
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
req.irql: < DISPATCH_LEVEL
---

# RtlUpcaseUnicodeToMultiByteN function



## -description
The <b>RtlUpcaseUnicodeToMultiByteN</b> routine translates the specified Unicode string into a new uppercase character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. 


## -syntax

````
NTSTATUS RtlUpcaseUnicodeToMultiByteN(
  _Out_     PCHAR  MultiByteString,
  _In_      ULONG  MaxBytesInMultiByteString,
  _Out_opt_ PULONG BytesInMultiByteString,
  _In_      PCWCH  UnicodeString,
  _In_      ULONG  BytesInUnicodeString
);
````


## -parameters

### -param MultiByteString [out]

Pointer to a caller-allocated buffer to receive the translated string. 

### -param MaxBytesInMultiByteString [in]

Maximum number of bytes to be written at <i>MultiByteString</i>. If this value causes the translated string to be truncated, <b>RtlUpcaseUnicodeToMultiByteN</b> does not return an error status. 

### -param BytesInMultiByteString [out, optional]

Pointer to a caller-allocated variable that receives the length, in bytes, of the translated string. This parameter can be <b>NULL</b>. 

### -param UnicodeString [in]

Pointer to the Unicode source string to be translated. 

### -param BytesInUnicodeString [in]

Size, in bytes, of the string at <i>UnicodeString</i>. 

## -returns
<b>RtlUpcaseUnicodeToMultiByteN</b> returns STATUS_SUCCESS. 

## -remarks
<b>RtlUpcaseUnicodeToMultiByteN</b> translates the given Unicode string using the current system ANSI code page installed at system boot time and converts the translated string to uppercase. 

This routine does not modify the source string. It returns a NULL-terminated ANSI string if the given <i>BytesInUnicodeString</i> included a NULL terminator and if the given <i>MaxBytesInMultiByteString</i> did not cause truncation.

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
&lt; DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.rtlmultibytetounicoden">RtlMultiByteToUnicodeN</a>
</dt>
<dt>
<a href="ifsk.rtlunicodetomultibyten">RtlUnicodeToMultiByteN</a>
</dt>
<dt>
<a href="ifsk.rtlunicodetomultibytesize">RtlUnicodeToMultiByteSize</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlUpcaseUnicodeToMultiByteN routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
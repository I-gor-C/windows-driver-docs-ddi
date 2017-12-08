---
UID: NF.ntifs.RtlUnicodeToOemN
title: RtlUnicodeToOemN function
author: windows-driver-content
description: The RtlUnicodeToOemN routine translates a given Unicode string to an OEM string, using the current system OEM code page.
old-location: ifsk\rtlunicodetooemn.htm
old-project: ifsk
ms.assetid: bb9ec3d9-89cd-4c56-8020-f8f97c2ce69b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlUnicodeToOemN
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
req.alt-api: RtlUnicodeToOemN
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

# RtlUnicodeToOemN function



## -description
The <b>RtlUnicodeToOemN</b> routine translates a given Unicode string to an OEM string, using the current system OEM code page. 


## -syntax

````
NTSTATUS RtlUnicodeToOemN(
  _Out_     PCHAR  OemString,
  _In_      ULONG  MaxBytesInOemString,
  _Out_opt_ PULONG BytesInOemString,
  _In_      PCWCH  UnicodeString,
  _In_      ULONG  BytesInUnicodeString
);
````


## -parameters

### -param OemString [out]

Pointer to a caller-allocated buffer to receive the translated string. 

### -param MaxBytesInOemString [in]

Maximum number of bytes to be written to <i>OemString</i>. 

### -param BytesInOemString [out, optional]

Pointer to a caller-allocated variable that receives the number of bytes in the translated string. This parameter can be <b>NULL</b>. 

### -param UnicodeString [in]

Pointer to the Unicode source string to be translated. 

### -param BytesInUnicodeString [in]

Size, in bytes, of the string at <i>UnicodeString</i>. 

## -returns
<b>RtlUnicodeToOemN</b> returns STATUS_SUCCESS if the full string at <i>UnicodeString</i> was translated and returned at <i>OemString</i>. 

## -remarks
For the return value STATUS_BUFFER_OVERFLOW, the truncated string at <i>OemString</i> was translated without error. 

For the return value STATUS_SUCCESS, the value at <i>BytesInOemString</i>, if any, indicates the length of the returned string, rather than the given <i>MaxBytesInOemString</i>. 

<b>RtlUnicodeToOemN</b> does not modify the source string. It returns a null-terminated OEM string if the given <i>BytesInUnicodeString</i> included a NULL terminator and if the given <i>MaxBytesInOemString</i> did not cause truncation. 

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
<a href="ifsk.rtloemtounicoden">RtlOemToUnicodeN</a>
</dt>
<dt>
<a href="ifsk.rtlunicodestringtocountedoemstring">RtlUnicodeStringToCountedOemString</a>
</dt>
<dt>
<a href="ifsk.rtlunicodestringtooemstring">RtlUnicodeStringToOemString</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlUnicodeToOemN routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

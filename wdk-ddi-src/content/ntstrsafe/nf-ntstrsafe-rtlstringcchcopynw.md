---
UID: NF.ntstrsafe.RtlStringCchCopyNW
title: RtlStringCchCopyNW
author: windows-driver-content
description: The RtlStringCchCopyNW and RtlStringCchCopyNA functions copy a character-counted string to a buffer while limiting the size of the copied string.
old-location: kernel\rtlstringcchcopyn.htm
old-project: kernel
ms.assetid: 86ec1a98-d70f-437c-9c8b-005bf78375ba
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlStringCchCopyNW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntstrsafe.h
req.include-header: Ntstrsafe.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP with Service Pack 1 (SP1) and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlStringCchCopyN,RtlStringCchCopyNW,RtlStringCchCopyNW
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: RtlStringCchCopyNW (Unicode) and RtlStringCchCopyNW (ANSI)
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntstrsafe.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# RtlStringCchCopyNW function



## -description
<p>The <b>RtlStringCchCopyNW</b> and <b>RtlStringCchCopyNA</b> functions copy a character-counted string to a buffer while limiting the size of the copied string.</p>


## -syntax

````
NTSTATUS RtlStringCchCopyN(
  _Out_ LPTSTR  pszDest,
  _In_  size_t  cchDest,
  _In_  LPCTSTR pszSrc,
  _In_  size_t  cchSrc
);
````


## -parameters
<dl>

### -param <i>pszDest</i> [out]

<dd>
<p>A pointer to a caller-supplied buffer that receives the copied string. The string at <i>pszSrc</i>, up to <i>cchSrc</i> characters, is copied to the buffer at <i>pszDest</i> and terminated with a null character.</p>
</dd>

### -param <i>cchDest</i> [in]

<dd>
<p>The size of the destination buffer, in characters. The maximum number of characters allowed is NTSTRSAFE_MAX_CCH.</p>
</dd>

### -param <i>pszSrc</i> [in]

<dd>
<p>A pointer to a caller-supplied, null-terminated string. </p>
</dd>

### -param <i>cchSrc</i> [in]

<dd>
<p>The maximum number of characters to copy from <i>pszSrc</i> to the buffer that is supplied by <i>pszDest</i>.</p>
</dd>
</dl>

## -returns
<p>The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means source data was present, the string was copied without truncation, and the resultant destination buffer is null-terminated.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This <i>warning</i> status means the copy operation did not complete due to insufficient space in the destination buffer. The destination buffer contains a truncated version of the copied string.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.</p>

<p>The function returns the STATUS_INVALID_PARAMETER value when:</p>

<p> </p>

## -remarks
<p><b>RtlStringCchCopyNW</b> and <b>RtlStringCchCopyNA</b> should be used instead of <b>strncpy</b>. </p>

<p>The functions copy a given number of characters from a source string. <b>RtlStringCchCopyNW</b> and <b>RtlStringCchCopyNA</b> receive the size, in characters, of the destination buffer to ensure that the functions do not write past the end of the buffer.</p>

<p>Note that these functions behave differently from <b>strncpy</b> in one respect. If <i>cchSrc</i> is larger than the number of characters in <i>pszSrc</i>, <b>RtlStringCchCopyNW</b> and <b>RtlStringCchCopyNA</b>—unlike <b>strncpy</b>—do not continue to pad <i>pszDest</i> with null characters until <i>cchSrc</i> characters have been copied.</p>

<p>Use <b>RtlStringCchCopyNW</b> to handle Unicode strings and <b>RtlStringCchCopyNA</b> to handle ANSI strings. The form you use depends on your data, as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCchCopyNW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCchCopyNA</b></p>

<p>If <i>pszSrc</i> and <i>pszDest</i> point to overlapping strings, the behavior of the function is undefined.</p>

<p>Neither <i>pszSrc</i> nor <i>pszDest</i> can be <b>NULL</b>. If you need to handle <b>NULL</b> string pointer values, use <a href="kernel.rtlstringcchcopynex">RtlStringCchCopyNEx</a>.</p>

<p>For more information about the safe string functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565508">Using Safe String Functions</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP with Service Pack 1 (SP1) and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntstrsafe.h (include Ntstrsafe.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntstrsafe.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Unicode and ANSI names</p>
</th>
<td width="70%">
<p><b>RtlStringCchCopyNW</b> (Unicode) and <b>RtlStringCchCopyNW</b> (ANSI)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlstringcbcopyn">RtlStringCbCopyN</a>
</dt>
<dt>
<a href="kernel.rtlstringcchcopy">RtlStringCchCopy</a>
</dt>
<dt>
<a href="kernel.rtlstringcchcopynex">RtlStringCchCopyNEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCchCopyN function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ntstrsafe.RtlStringCbCatA
title: RtlStringCbCatA
author: windows-driver-content
description: The RtlStringCbCatW and RtlStringCbCatA functions concatenate two byte-counted strings.
old-location: kernel\rtlstringcbcat.htm
old-project: kernel
ms.assetid: 1034384f-6295-42ca-bf78-47c383417500
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlStringCbCatA
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
req.alt-api: RtlStringCbCat,RtlStringCbCatA,RtlStringCbCatW
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: RtlStringCbCatW (Unicode) and RtlStringCbCatA (ANSI)
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

# RtlStringCbCatA function



## -description
<p>The <b>RtlStringCbCatW</b> and <b>RtlStringCbCatA</b> functions concatenate two byte-counted strings.</p>


## -syntax

````
NTSTATUS RtlStringCbCat(
  _Inout_ LPTSTR  pszDest,
  _In_    size_t  cbDest,
  _In_    LPCTSTR pszSrc
);
````


## -parameters
<dl>

### -param <i>pszDest</i> [in, out]

<dd>
<p>A pointer to a buffer which, on input, contains a null-terminated string to which <i>pszSrc</i> will be concatenated. On output, this is the destination buffer that contains the entire resultant string. The string at <i>pszSrc</i> is added to the end of the string at <i>pszDest</i> and terminated with a null character. </p>
</dd>

### -param <i>cbDest</i> [in]

<dd>
<p>The size of the destination buffer, in bytes. The destination buffer must be large enough to include the concatenated strings and the terminating null character. </p>
<p>For Unicode strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(WCHAR).</p>
<p>For ANSI strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(char).</p>
</dd>

### -param <i>pszSrc</i> [in]

<dd>
<p>A pointer to a null-terminated string. This string will be concatenated to the end of the string that is contained in the buffer at <i>pszDest</i>.</p>
</dd>
</dl>

## -returns
<p>The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means source data was present, the strings were concatenated without truncation, and the resultant destination buffer is null-terminated.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This <i>warning</i> status means the concatenation operation did not complete due to insufficient buffer space. The destination buffer contains a truncated, null-terminated version of the intended result.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.</p>

<p>The STATUS_INVALID_PARAMETER return value means that one of the following occurred:</p>

<p> </p>

## -remarks
<p><b>RtlStringCbCatW</b> and <b>RtlStringCbCatA</b> should be used instead of the following functions:</p>

<p><b>strcat</b></p>

<p><b>wcscat</b></p>

<p>Because <b>RtlStringCbCatW</b> and <b>RtlStringCbCatA </b>receive the size of the destination buffer as input, they will not write past the end of the buffer. </p>

<p>Use <b>RtlStringCbCatW</b> to handle Unicode strings and <b>RtlStringCbCatA</b> to handle ANSI strings. The form to use is determined by your data as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCbCatW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCbCatA</b></p>

<p>If <i>pszSrc</i> and <i>pszDest</i> point to strings that overlap, the behavior of the functions is undefined.</p>

<p>Neither <i>pszSrc</i> nor <i>pszDest</i> can be <b>NULL</b>. If you need to handle <b>NULL</b> string pointer values, use <a href="kernel.rtlstringcbcatnex">RtlStringCbCatNEx</a>.</p>

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
<p><b>RtlStringCbCatW</b> (Unicode) and <b>RtlStringCbCatA</b> (ANSI)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlstringcbcatex">RtlStringCbCatEx</a>
</dt>
<dt>
<a href="kernel.rtlstringcchcatex">RtlStringCchCatEx</a>
</dt>
<dt>
<a href="kernel.rtlstringcbcatnex">RtlStringCbCatNEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCbCat function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ntstrsafe.RtlStringCchCopyNExA
title: RtlStringCchCopyNExA
author: windows-driver-content
description: The RtlStringCchCopyNExW and RtlStringCchCopyNExA functions copy a character-counted string to a buffer while limiting the size of the copied string.
old-location: kernel\rtlstringcchcopynex.htm
old-project: kernel
ms.assetid: c53672b7-fbe7-45f7-b3ff-30cfeefa7d52
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlStringCchCopyNExA
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
req.alt-api: RtlStringCchCopyNEx,RtlStringCchCopyNExA,RtlStringCchCopyNExW
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: RtlStringCchCopyNExW (Unicode) and RtlStringCchCopyNExA (ANSI)
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

# RtlStringCchCopyNExA function



## -description
<p>The <b>RtlStringCchCopyNExW</b> and <b>RtlStringCchCopyNExA</b> functions copy a character-counted string to a buffer while limiting the size of the copied string.</p>


## -syntax

````
NTSTATUS RtlStringCchCopyNEx(
  _Out_opt_ LPTSTR  pszDest,
  _In_      size_t  cchDest ,
  _In_opt_  LPCTSTR pszSrc,
  _In_      size_t  cchSrc,
  _Out_opt_ LPTSTR  *ppszDestEnd,
  _Out_opt_ size_t  *pcchRemaining,
  _In_      DWORD   dwFlags
);
````


## -parameters
<dl>

### -param <i>pszDest</i> [out, optional]

<dd>
<p>A pointer to a caller-supplied buffer that receives the copied string. The string at <i>pszSrc</i> is copied to the buffer at <i>pszDest</i> and terminated with a null character. The <i>pszDest</i> pointer can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.</p>
</dd>

### -param <i>cchDest </i> [in]

<dd>
<p>The size, in characters, of the destination buffer. The maximum number of characters allowed is NTSTRSAFE_MAX_CCH. If <i>pszDest</i> is <b>NULL</b>, <i>cchDest</i> must be zero.</p>
</dd>

### -param <i>pszSrc</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied, null-terminated string. </p>
</dd>

### -param <i>cchSrc</i> [in]

<dd>
<p>The maximum number of characters to copy from <i>pszSrc</i> to the buffer that is supplied by <i>pszDest</i>.</p>
</dd>

### -param <i>ppszDestEnd</i> [out, optional]

<dd>
<p>If the caller supplies a non-<b>NULL</b> address pointer then, after the copy operation completes, the function loads that address with a pointer to the destination buffer's resulting null string terminator. </p>
</dd>

### -param <i>pcchRemaining</i> [out, optional]

<dd>
<p>If the caller supplies a non-<b>NULL</b> address pointer, the function loads the address with the number of unused characters that are in the buffer pointed to by <i>pszDest</i>, including the terminating null character.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>One or more flags and, optionally, a fill byte. The flags are defined as follows:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STRSAFE_FILL_BEHIND_NULL"></a><a id="strsafe_fill_behind_null"></a><dl>

### -param <b>STRSAFE_FILL_BEHIND_NULL</b>

</dl>
</td>
<td width="60%">
<p>If set and the function succeeds, the low byte of <i>dwFlags</i> is used to fill the portion of the destination buffer that follows the terminating null character. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="STRSAFE_IGNORE_NULLS"></a><a id="strsafe_ignore_nulls"></a><dl>

### -param <b>STRSAFE_IGNORE_NULLS</b>

</dl>
</td>
<td width="60%">
<p>If set, either <i>pszDest </i>or<i> pszSrc</i>, or both, can be <b>NULL</b>. <b>NULL</b> <i>pszSrc</i> pointers are treated like empty strings (TEXT("")), which can be copied. <b>NULL</b> <i>pszDest</i> pointers cannot receive nonempty strings.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STRSAFE_FILL_ON_FAILURE"></a><a id="strsafe_fill_on_failure"></a><dl>

### -param <b>STRSAFE_FILL_ON_FAILURE</b>

</dl>
</td>
<td width="60%">
<p>If set and the function fails, the low byte of <i>dwFlags</i> is used to fill the entire destination buffer, and the buffer is null-terminated. This operation overwrites any preexisting buffer contents.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STRSAFE_NULL_ON_FAILURE"></a><a id="strsafe_null_on_failure"></a><dl>

### -param <b>STRSAFE_NULL_ON_FAILURE</b>

</dl>
</td>
<td width="60%">
<p>If set and the function fails, the destination buffer is set to an empty string (TEXT("")). This operation overwrites any preexisting buffer contents.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STRSAFE_NO_TRUNCATION"></a><a id="strsafe_no_truncation"></a><dl>

### -param <b>STRSAFE_NO_TRUNCATION</b>

</dl>
</td>
<td width="60%">
<p>If set and the function returns STATUS_BUFFER_OVERFLOW, the contents of the destination buffer are not modified.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means source data was present, the string was copied without truncation, and the resultant destination buffer is null-terminated.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This <i>warning</i> status means the copy operation did not complete due to insufficient space in the destination buffer. If STRSAFE_NO_TRUNCATION is set in <i>dwFlags</i>, the destination buffer is not modified. If the flag is not set, the destination buffer contains a truncated version of the created string.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.</p>

<p>The function returns the STATUS_INVALID_PARAMETER value when:</p>

<p> </p>

## -remarks
<p><b>RtlStringCchCopyNExW</b> and <b>RtlStringCchCopyNExA</b> should be used instead of <b>strncpy</b>. </p>

<p>The functions copy a given number of characters from a source string. The size, in characters, of the destination buffer is provided to <b>RtlStringCchCopyNExW</b> and <b>RtlStringCchCopyNExA</b> to ensure that they do not write past the end of the buffer.</p>

<p>Note that these functions behave differently from <b>strncpy</b> in one respect. If <i>cchSrc</i> is larger than the number of characters in <i>pszSrc</i>, <b>RtlStringCchCopyNExW</b> and <b>RtlStringCchCopyNExA</b>—unlike <b>strncpy</b>—do not continue to pad <i>pszDest</i> with null characters until <i>cchSrc</i> characters have been copied.</p>

<p><b>RtlStringCchCopyNExW</b> and <b>RtlStringCchCopyNExA</b> add to the functionality of <a href="kernel.rtlstringcchcopyn">RtlStringCchCopyN</a> by returning a pointer to the end of the destination string, as well as the number of characters left unused in that string. Flags can be passed to the function for additional control.</p>

<p>Use <b>RtlStringCchCopyNExW</b> to handle Unicode strings and <b>RtlStringCchCopyNExA</b> to handle ANSI strings. The form you  use depends on your data, as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCchCopyNExW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCchCopyNExA</b></p>

<p>If <i>pszSrc</i> and <i>pszDest</i> point to overlapping strings, the behavior of the function is undefined.</p>

<p>Neither <i>pszSrc</i> nor <i>pszDest</i> can be <b>NULL</b> unless the STRSAFE_IGNORE_NULLS flag is set, in which case either or both can be <b>NULL</b>. If <i>pszDest</i> is <b>NULL</b>, <i>pszSrc</i> must either be <b>NULL</b> or point to an empty string.</p>

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
<p><b>RtlStringCchCopyNExW</b> (Unicode) and <b>RtlStringCchCopyNExA</b> (ANSI)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlstringcchcopyn">RtlStringCchCopyN</a>
</dt>
<dt>
<a href="kernel.rtlstringcbcopynex">RtlStringCbCopyNEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCchCopyNEx function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

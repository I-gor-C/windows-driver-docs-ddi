---
UID: NF.ntstrsafe.RtlStringCchCopyA
title: RtlStringCchCopyA
author: windows-driver-content
description: The RtlStringCchCopyW and RtlStringCchCopyA functions copy a null-terminated source string into a destination buffer of specified length.
old-location: kernel\rtlstringcchcopy.htm
old-project: kernel
ms.assetid: d5c6d7d2-fe14-49d5-9e81-3a425a4cf1b3
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlStringCchCopyA
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
req.alt-api: RtlStringCchCopy,RtlStringCchCopyA,RtlStringCchCopyW
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: RtlStringCchCopyW (Unicode) and RtlStringCchCopyA (ANSI)
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

# RtlStringCchCopyA function



## -description
<p>The <b>RtlStringCchCopyW</b> and <b>RtlStringCchCopyA</b> functions copy a null-terminated source string into a destination buffer of specified length. </p>


## -syntax

````
NTSTATUS RtlStringCchCopy(
  _Out_ LPTSTR  pszDest,
  _In_  size_t  cchDest,
  _In_  LPCTSTR pszSrc
);
````


## -parameters
<dl>

### -param <i>pszDest</i> [out]

<dd>
<p>A pointer to a caller-supplied buffer that receives the copied string. The string at <i>pszSrc</i> is copied to the buffer at <i>pszDest</i> and terminated with a null character.</p>
</dd>

### -param <i>cchDest</i> [in]

<dd>
<p>The size, in characters, of the destination buffer. The maximum number of characters allowed is NTSTRSAFE_MAX_CCH. </p>
</dd>

### -param <i>pszSrc</i> [in]

<dd>
<p>A pointer to a caller-supplied, null-terminated string.</p>
</dd>
</dl>

## -returns
<p>The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means source data was present, the string was copied without truncation, and the resultant destination buffer is null-terminated.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This <i>warning</i> status means the copy operation did not complete due to insufficient buffer space. The destination buffer contains a truncated, null-terminated version of the intended result.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.</p>

<p>The function returns the STATUS_INVALID_PARAMETER value when:</p>

<p> </p>

## -remarks
<p><b>RtlStringCchCopyW</b> and <b>RtlStringCchCopyA</b> should be used instead of the following functions: </p>

<p><b>strcpy</b></p>

<p><b>wcscpy</b></p>

<p>These functions are not replacements for <b>strncpy</b>. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562846">RtlStringCchCopyN</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562849">RtlStringCchCopyNEx</a> to replace <b>strncpy</b>.</p>

<p>The size, in characters, of the destination buffer is provided to <b>RtlStringCchCopyW</b> and <b>RtlStringCchCopyA</b> to ensure that they do not write past the end of the buffer.</p>

<p>Use <b>RtlStringCchCopyW</b> to handle Unicode strings and <b>RtlStringCchCopyA</b> to handle ANSI strings. The form you use depends your data, as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCchCopyW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCchCopyA</b></p>

<p> </p>

<p>If <i>pszSrc</i> and <i>pszDest</i> point to overlapping strings, the behavior of the function is undefined.</p>

<p>Neither <i>pszSrc</i> nor <i>pszDest</i> can be <b>NULL</b>. If you need to handle <b>NULL</b> string pointer values, use <a href="kernel.rtlstringcchcopyex">RtlStringCchCopyEx</a>.</p>

<p>For more information about the safe string functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565508">Using Safe String Functions</a>.</p>

<p><b>RtlStringCchCopyW</b> and <b>RtlStringCchCopyA</b> should be used instead of the following functions: </p>

<p><b>strcpy</b></p>

<p><b>wcscpy</b></p>

<p>These functions are not replacements for <b>strncpy</b>. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562846">RtlStringCchCopyN</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562849">RtlStringCchCopyNEx</a> to replace <b>strncpy</b>.</p>

<p>The size, in characters, of the destination buffer is provided to <b>RtlStringCchCopyW</b> and <b>RtlStringCchCopyA</b> to ensure that they do not write past the end of the buffer.</p>

<p>Use <b>RtlStringCchCopyW</b> to handle Unicode strings and <b>RtlStringCchCopyA</b> to handle ANSI strings. The form you use depends your data, as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCchCopyW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCchCopyA</b></p>

<p> </p>

<p>If <i>pszSrc</i> and <i>pszDest</i> point to overlapping strings, the behavior of the function is undefined.</p>

<p>Neither <i>pszSrc</i> nor <i>pszDest</i> can be <b>NULL</b>. If you need to handle <b>NULL</b> string pointer values, use <a href="kernel.rtlstringcchcopyex">RtlStringCchCopyEx</a>.</p>

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
<p><b>RtlStringCchCopyW</b> (Unicode) and <b>RtlStringCchCopyA</b> (ANSI)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562805">RtlStringCbCopy</a>
</dt>
<dt>
<a href="kernel.rtlstringcchcopyex">RtlStringCchCopyEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCchCopy function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

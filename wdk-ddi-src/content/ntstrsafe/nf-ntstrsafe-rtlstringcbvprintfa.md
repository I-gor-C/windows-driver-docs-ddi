---
UID: NF.ntstrsafe.RtlStringCbVPrintfA
title: RtlStringCbVPrintfA
author: windows-driver-content
description: The RtlStringCbVPrintfW and RtlStringCbVPrintfA functions create a byte-counted text string, with formatting that is based on supplied formatting information.
old-location: kernel\rtlstringcbvprintf.htm
old-project: kernel
ms.assetid: 9dfd1894-c9b5-43c2-8377-c28577898754
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlStringCbVPrintfA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntstrsafe.h
req.include-header: Ntstrsafe.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows XP with Service Pack 1 (SP1).
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlStringCbVPrintf,RtlStringCbVPrintfA,RtlStringCbVPrintfW
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: RtlStringCbVPrintfW (Unicode) and RtlStringCbVPrintfA (ANSI)
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

# RtlStringCbVPrintfA function



## -description
<p>The <b>RtlStringCbVPrintfW</b> and <b>RtlStringCbVPrintfA</b> functions create a byte-counted text string, with formatting that is based on supplied formatting information.</p>


## -syntax

````
NTSTATUS RtlStringCbVPrintf(
  _Out_ LPTSTR  pszDest,
  _In_  size_t  cbDest,
  _In_  LPCTSTR pszFormat,
  _In_  va_list argList
);
````


## -parameters
<dl>

### -param <i>pszDest</i> [out]

<dd>
<p>A pointer to a caller-supplied buffer that receives a formatted, null-terminated string. The function creates this string from both the formatting string that is supplied by <i>pszFormat</i> and the arguments supplied by <i>argList</i>.</p>
</dd>

### -param <i>cbDest</i> [in]

<dd>
<p>The size of the destination buffer, in bytes. The buffer must be large enough to contain the formatted string plus the terminating null character.</p>
<p>For Unicode strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(WCHAR). </p>
<p>For ANSI strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(char). </p>
</dd>

### -param <i>pszFormat</i> [in]

<dd>
<p>A pointer to a null-terminated text string that contains <b>printf</b>-styled <a href="http://msdn.microsoft.com/en-us/library/56e442dc.aspx">formatting directives</a>.</p>
</dd>

### -param <i>argList</i> [in]

<dd>
<p>A <b>va_list</b>-typed argument list. Arguments contained in the argument list will be interpreted by using the formatting string that is supplied by <i>pszFormat</i>.</p>
</dd>
</dl>

## -returns
<p>The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means source data was present, the output string was created without truncation, and the resultant destination buffer is null-terminated.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This <i>warning</i> status means the operation did not complete due to insufficient space in the destination buffer. The destination buffer contains a truncated version of the created string.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.</p>

<p>The function returns the STATUS_INVALID_PARAMETER value when:</p>

<p> </p>

## -remarks
<p><b>RtlStringCbVPrintfW</b> and <b>RtlStringCbVPrintfA</b> should be used instead of the following functions: </p>

<p><b>vsprintf</b></p>

<p><b>vswprintf</b></p>

<p>_<b>vsnprintf</b></p>

<p>_<b>vsnwprintf</b></p>

<p>All of these functions accept a format string, along with a set of arguments in a <b>va_list</b>-typed argument list, and return a formatted string. The size, in bytes, of the destination buffer is provided to <b>RtlStringCbVPrintfW</b> and <b>RtlStringCbVPrintfA</b> to ensure that they do not write past the end of the buffer.</p>

<p>For more information about <b>va_list</b>-typed argument lists, see the Microsoft Windows SDK documentation.</p>

<p>Use <b>RtlStringCbVPrintfW</b> to handle Unicode strings and <b>RtlStringCbVPrintfA</b> to handle ANSI strings. The form you use depends on your data, as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCbVPrintfW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCbVPrintfA</b></p>

<p>If <i>pszDest</i> and <i>pszFormat </i>point to overlapping strings or if any argument strings overlap, the behavior of the function is undefined..</p>

<p>Neither <i>pszFormat</i> nor <i>pszDest</i> should be <b>NULL</b>. If you need to handle <b>NULL</b> string pointer values, use <a href="kernel.rtlstringcbvprintfex">RtlStringCbVPrintfEx</a>.</p>

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
<p>Available starting with Windows XP with Service Pack 1 (SP1).</p>
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
<p><b>RtlStringCbVPrintfW</b> (Unicode) and <b>RtlStringCbVPrintfA</b> (ANSI)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlstringcbvprintfex">RtlStringCbVPrintfEx</a>
</dt>
<dt>
<a href="kernel.rtlstringcbprintf">RtlStringCbPrintf</a>
</dt>
<dt>
<a href="kernel.rtlstringcchvprintf">RtlStringCchVPrintf</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCbVPrintf function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

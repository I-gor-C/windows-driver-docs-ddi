---
UID: NF.ntstrsafe.RtlUnicodeStringVPrintfEx
title: RtlUnicodeStringVPrintfEx
author: windows-driver-content
description: The RtlUnicodeStringVPrintfEx function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure.
old-location: kernel\rtlunicodestringvprintfex.htm
old-project: kernel
ms.assetid: da14f93d-c3db-4c54-8378-7492b79a5e18
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlUnicodeStringVPrintfEx
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
req.alt-api: RtlUnicodeStringVPrintfEx
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: 
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

# RtlUnicodeStringVPrintfEx function



## -description
<p>The <b>RtlUnicodeStringVPrintfEx</b> function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure.</p>


## -syntax

````
NTSTATUS RtlUnicodeStringVPrintfEx(
  _Out_     PUNICODE_STRING  DestinationString,
  _Out_opt_ PUNICODE_STRING  RemainingString,
  _In_      DWORD            dwFlags,
  _In_      NTSTRSAFE_PCWSTR pszFormat,
  _In_      va_list          argList
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [out]

<dd>
<p>Optional. A pointer to a <b>UNICODE_STRING</b> structure that receives a formatted string. <b>RtlUnicodeStringVPrintfEx</b> creates this string from the formatting string that <i>pszFormat</i> supplies and the function's argument list. The maximum number of characters in the string is NTSTRSAFE_UNICODE_STRING_MAX_CCH. <i>DestinationString</i> can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.</p>
</dd>

### -param <i>RemainingString</i> [out, optional]

<dd>
<p>Optional. If the caller supplies a non-<b>NULL</b> pointer to a <b>UNICODE_STRING</b> structure, <b>RtlUnicodeStringVPrintfE</b> sets this structure's <b>Buffer</b> member to the end of the formatted string, sets the structure's <b>Length</b> member to zero, and sets the structure's <b>MaximumLength</b> member to the number of bytes that are remaining in the destination buffer. <i>RemainingString</i> can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>One or more flags and, optionally, a fill byte. The flags are defined as follows:</p>
<p></p>
<dl>

### -param <a id="STRSAFE_FILL_BEHIND"></a><a id="strsafe_fill_behind"></a>STRSAFE_FILL_BEHIND

<dd>
<p>If this flag is set and the function succeeds, the low byte of <i>dwFlags</i> is used to fill the portion of the destination buffer that follows the last character in the string.</p>
</dd>

### -param <a id="STRSAFE_IGNORE_NULLS_"></a><a id="strsafe_ignore_nulls_"></a>STRSAFE_IGNORE_NULLS 

<dd>
<p>If this flag is set, the source or destination pointer, or both, can be <b>NULL</b>. <b>RtlUnicodeStringVPrintfEx</b> treats <b>NULL</b> source buffer pointers like empty strings (TEXT("")), which can be copied. <b>NULL</b> destination buffer pointers cannot receive nonempty strings.</p>
</dd>

### -param <a id="STRSAFE_FILL_ON_FAILURE_"></a><a id="strsafe_fill_on_failure_"></a>STRSAFE_FILL_ON_FAILURE 

<dd>
<p>If this flag is set and the function fails, the low byte of <i>dwFlags</i> is used to fill the entire destination buffer. This operation overwrites any preexisting buffer contents.</p>
</dd>

### -param <a id="STRSAFE_NULL_ON_FAILURE_"></a><a id="strsafe_null_on_failure_"></a>STRSAFE_NULL_ON_FAILURE 

<dd>
<p>If this flag is set and the function fails, the destination buffer is set to an empty string (TEXT("")). This operation overwrites any preexisting buffer contents.</p>
</dd>

### -param <a id="STRSAFE_NO_TRUNCATION_"></a><a id="strsafe_no_truncation_"></a>STRSAFE_NO_TRUNCATION 

<dd>
<p>If this flag is set and the function returns STATUS_BUFFER_OVERFLOW, the contents of the destination buffer are not modified.</p>
</dd>

### -param <a id="STRSAFE_ZERO_LENGTH_ON_FAILURE"></a><a id="strsafe_zero_length_on_failure"></a>STRSAFE_ZERO_LENGTH_ON_FAILURE

<dd>
<p>If this flag is set and the function returns STATUS_BUFFER_OVERFLOW, the destination string length is set to zero bytes.</p>
</dd>
</dl>
</dd>

### -param <i>pszFormat</i> [in]

<dd>
<p>A pointer to a nul-terminated text string that contains <b>printf</b>-styled formatting directives. This pointer can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.</p>
</dd>

### -param <i>argList</i> [in]

<dd>
<p>A <b>va_list</b>-typed argument list. Arguments in this argument list will be interpreted by the using formatting string that <i>pszFormat</i> supplies.</p>
</dd>
</dl>

## -returns
<p><b>RtlUnicodeStringVPrintfEx</b> returns one of the following NTSTATUS values. </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means source data was present, and the strings were concatenated without truncation.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This <i>warning</i> status means the copy operation did not complete due to insufficient space in the destination buffer. If STRSAFE_NO_TRUNCATION is set in <i>dwFlags</i>, the destination buffer is not modified. If the flag is not set, the destination buffer contains a truncated version of the copied string.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.</p>

<p> </p>

<p><b>RtlUnicodeStringVPrintfEx</b> returns the STATUS_INVALID_PARAMETER value when one of the following occurs:</p>

<p>For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p>

## -remarks
<p>The <b>RtlUnicodeStringVPrintfEx</b> function uses the destination buffer's size to ensure that the string formatting operation does not write past the end of the buffer. By default, the function does <u>not</u> terminate the resultant string with a null character value (that is, with zero). As an option, the caller can use the STRSAFE_FILL_BEHIND flag and a fill byte value of zero to null-terminate a resultant string that does not occupy the entire destination buffer.</p>

<p><b>RtlUnicodeStringVPrintfEx</b> adds to the functionality of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562983">RtlUnicodeStringVPrintf</a> function by returning a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that identifies the end of the destination string and the number of bytes that are left unused in that string. You can pass flags to <b>RtlUnicodeStringVPrintfEx</b> for additional control.</p>

<p>If the format string and the destination string overlap, the behavior of the function is undefined.</p>

<p>The <i>pszFormat</i> and <i>DestinationString</i> pointers cannot be <b>NULL</b> unless the STRSAFE_IGNORE_NULLS flag is set in <i>dwFlags</i>. If STRSAFE_IGNORE_NULLS is set, one or both of these pointers can be <b>NULL</b>. If the <i>DestinationString</i> pointer is <b>NULL</b>, the <i>pszFormat</i> pointer must be <b>NULL</b> or point to an empty string.</p>

<p>For more information about <b>va_list</b>-typed argument lists, see the Microsoft Windows SDK documentation.</p>

<p>For more information about the safe string functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565508">Using Safe String Functions</a>.</p>

<p>The <b>RtlUnicodeStringVPrintfEx</b> function uses the destination buffer's size to ensure that the string formatting operation does not write past the end of the buffer. By default, the function does <u>not</u> terminate the resultant string with a null character value (that is, with zero). As an option, the caller can use the STRSAFE_FILL_BEHIND flag and a fill byte value of zero to null-terminate a resultant string that does not occupy the entire destination buffer.</p>

<p><b>RtlUnicodeStringVPrintfEx</b> adds to the functionality of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562983">RtlUnicodeStringVPrintf</a> function by returning a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that identifies the end of the destination string and the number of bytes that are left unused in that string. You can pass flags to <b>RtlUnicodeStringVPrintfEx</b> for additional control.</p>

<p>If the format string and the destination string overlap, the behavior of the function is undefined.</p>

<p>The <i>pszFormat</i> and <i>DestinationString</i> pointers cannot be <b>NULL</b> unless the STRSAFE_IGNORE_NULLS flag is set in <i>dwFlags</i>. If STRSAFE_IGNORE_NULLS is set, one or both of these pointers can be <b>NULL</b>. If the <i>DestinationString</i> pointer is <b>NULL</b>, the <i>pszFormat</i> pointer must be <b>NULL</b> or point to an empty string.</p>

<p>For more information about <b>va_list</b>-typed argument lists, see the Microsoft Windows SDK documentation.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562961">RtlUnicodeStringPrintf</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562964">RtlUnicodeStringPrintfEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562983">RtlUnicodeStringVPrintf</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlUnicodeStringVPrintfEx function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

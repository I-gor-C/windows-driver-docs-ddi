---
UID: NF.ntstrsafe.RtlUnicodeStringInitEx
title: RtlUnicodeStringInitEx
author: windows-driver-content
description: The RtlUnicodeStringInitEx function initializes a UNICODE_STRING structure.
old-location: kernel\rtlunicodestringinitex.htm
old-project: kernel
ms.assetid: d57fee0b-2dd3-4fad-bc7e-d413c08e2441
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUnicodeStringInitEx
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
req.alt-api: RtlUnicodeStringInitEx
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

# RtlUnicodeStringInitEx function



## -description
<p>The <b>RtlUnicodeStringInitEx</b> function initializes a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure.</p>


## -syntax

````
NTSTATUS RtlUnicodeStringInitEx(
  _Out_    PUNICODE_STRING  DestinationString,
  _In_opt_ NTSTRSAFE_PCWSTR pszSrc,
  _In_     DWORD            dwFlags
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [out]

<dd>
<p>Optional. A pointer to a <b>UNICODE_STRING</b> structure to be initialized. The <i>pszSrc</i> pointer is copied into the <i>DestinationString</i> parameter's <b>UNICODE_STRING</b> structure. The maximum number of characters in the string that <i>pszSrc</i> points to is NTSTRSAFE_UNICODE_STRING_MAX_CCH. <i>DestinationString</i> can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.</p>
</dd>

### -param <i>pszSrc</i> [in, optional]

<dd>
<p>Optional. A pointer to a null-terminated string constant. This string pointer will be copied to the <b>Buffer</b> member of the <b>UNICODE_STRING</b> structure pointed to by the <i>DestinationString</i> parameter. This string pointer can be <b>NULL</b>.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>The following flag is defined: </p>
<p></p>
<dl>

### -param <a id="STRSAFE_IGNORE_NULLS_"></a><a id="strsafe_ignore_nulls_"></a>STRSAFE_IGNORE_NULLS 

<dd>
<p>If this flag is set, the source pointer can be <b>NULL</b>. <b>RtlUnicodeStringInitEx</b> treats <b>NULL</b> source buffer pointers like empty strings (TEXT("")), which can be copied.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>RtlUnicodeStringInitEx</b> returns one of the following NTSTATUS values. </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This <i>success</i> status means that source data was present, the string was copied without truncation, and the resultant destination buffer is null-terminated.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This <i>error</i> status means that the function received an invalid input parameter. For more information, see the following list.</p>

<p> </p>

<p><b>RtlUnicodeStringInitEx</b> returns the STATUS_INVALID_PARAMETER value when one of the following occurs:</p>

<p>For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p>

## -remarks
<p>The <b>RtlUnicodeStringInitEx</b> function does the following:</p>

<p>Sets the <b>Length</b> member of the <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure to the length, in bytes, of the string that the <i>pszSrc</i> parameter points to. </p>

<p>Sets the <b>MaximumLength</b> member of the <b>UNICODE_STRING</b> structure to the length, in bytes, of the string that the <i>pszSrc</i> parameter points to plus 2 bytes. </p>

<p>Sets the <b>Buffer</b> member of the <b>UNICODE_STRING</b> structure to the address that the <i>pszSrc</i> parameter specifies.</p>

<p>The <i>DestinationString</i> pointer cannot be <b>NULL</b> unless the STRSAFE_IGNORE_NULLS flag is set.</p>

<p>For more information about the safe string functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565508">Using Safe String Functions</a>. </p>

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
<a href="..\ntstrsafe\nf-ntstrsafe-rtlunicodestringinit.md">RtlUnicodeStringInit</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlUnicodeStringInitEx function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

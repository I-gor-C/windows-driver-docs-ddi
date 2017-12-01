---
UID: NF.wdm.RtlUnicodeStringToInteger
title: RtlUnicodeStringToInteger
author: windows-driver-content
description: The RtlUnicodeStringToInteger routine converts a Unicode string representation of a number to the equivalent integer value.
old-location: kernel\rtlunicodestringtointeger.htm
old-project: kernel
ms.assetid: d9357864-d49b-44fe-b884-64c6da609789
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUnicodeStringToInteger
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlUnicodeStringToInteger
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RtlUnicodeStringToInteger function



## -description
<p>The <b>RtlUnicodeStringToInteger</b> routine converts a Unicode string representation of a number to the equivalent integer value.</p>


## -syntax

````
NTSTATUS RtlUnicodeStringToInteger(
  _In_     PCUNICODE_STRING String,
  _In_opt_ ULONG            Base,
  _Out_    PULONG           Value
);
````


## -parameters
<dl>

### -param <i>String</i> [in]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the number representation to convert to the equivalent integer value.</p>
</dd>

### -param <i>Base</i> [in, optional]

<dd>
<p>A numeric value that indicates the base (or radix) of the number that the Unicode string represents. This parameter value is optional and can be set to zero.</p>
<p>If <i>Base</i> is zero, <b>RtlUnicodeStringToInteger</b> checks the prefix of the Unicode string to determine the base of the number:</p>
<ul>
<li>
<p>If the prefix is "0x", <b>RtlUnicodeStringToInteger</b> interprets the number in the string as a hexadecimal integer.</p>
</li>
<li>
<p>If the prefix is "0o", <b>RtlUnicodeStringToInteger</b> interprets the number in the string as an octal integer.</p>
</li>
<li>
<p>If the prefix is "0b", <b>RtlUnicodeStringToInteger</b> interprets the number in the string as a binary integer.</p>
</li>
</ul>
<p>If the Unicode string does not contain any of these prefixes, <b>RtlUnicodeStringToInteger</b> treats the string as a base-10 integer.</p>
</dd>

### -param <i>Value</i> [out]

<dd>
<p>A pointer to a ULONG variable to which <b>RtlUnicodeStringToInteger</b> writes the integer value that results from conversion of the Unicode string.</p>
</dd>
</dl>

## -returns
<p>If the conversion is successful, the <b>RtlUnicodeStringToInteger</b> routine returns STATUS_SUCCESS and sets *<i>Value</i> to the integer value represented by the number in the Unicode string. If the string is not empty, but does not start with a valid number representation, the routine returns STATUS_SUCCESS and sets *<i>Value</i> to zero. If the string is empty, the routine fails and returns STATUS_INVALID_PARAMETER.</p>

## -remarks
<p>This routine skips any white space at the start of the input string to find the start of the number.</p>

<p>If the first non-white space character in the string is a hyphen (-), the integer value written to *<i>Value</i> is negative; otherwise, if the first character is a "+" or there is no sign character, the integer value written to *<i>Value</i> is positive.</p>

<p> If the string does not contain a valid number, or if the first digit in the string is preceded by a non-white space character other than '+' or '-', the routine sets the output value to zero and returns STATUS_SUCCESS.</p>

<p>A substring that contains one or more valid digits is terminated by any character that is not a valid digit. For example, if <i>Base</i> = 2, valid digits are '0' and '1'. If <i>Base</i> = 8, valid digits are '0' to '7'. If <i>Base</i> = 10, valid digits are '0' to '9'. If <i>Base</i> = 16, valid digits are '0' to '9', 'a' to 'f', and 'A' to 'F'.</p>

<p>The following table contains examples of output values that result from various combinations of input strings and <i>Base</i> parameter values.</p>

<p>A related routine, <a href="..\wdm\nf-wdm-rtlintegertounicodestring.md">RtlIntegerToUnicodeString</a>, converts an integer value to the equivalent Unicode string representation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
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
<a href="..\wdm\nf-wdm-rtlintegertounicodestring.md">RtlIntegerToUnicodeString</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlUnicodeStringToInteger routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

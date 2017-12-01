---
UID: NF.wdm.RtlIntegerToUnicodeString
title: RtlIntegerToUnicodeString
author: windows-driver-content
description: The RtlIntegerToUnicodeString routine converts an unsigned integer value to a null-terminated string of one or more Unicode characters in the specified base.
old-location: kernel\rtlintegertounicodestring.htm
old-project: kernel
ms.assetid: d9c82a97-a8fb-4c23-aa9c-23711d98fd8b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlIntegerToUnicodeString
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
req.alt-api: RtlIntegerToUnicodeString
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

# RtlIntegerToUnicodeString function



## -description
<p>The <b>RtlIntegerToUnicodeString</b> routine converts an unsigned integer value to a null-terminated string of one or more Unicode characters in the specified base.</p>


## -syntax

````
NTSTATUS RtlIntegerToUnicodeString(
  _In_     ULONG           Value,
  _In_opt_ ULONG           Base,
  _Inout_  PUNICODE_STRING String
);
````


## -parameters
<dl>

### -param <i>Value</i> [in]

<dd>
<p>Specifies the ULONG value to convert. </p>
</dd>

### -param <i>Base</i> [in, optional]

<dd>
<p>Specifies the base to use when converting <i>Value</i> to a string. The possible values are:</p>
<table>
<tr>
<th>Value</th>
<th>Base</th>
</tr>
<tr>
<td>
<p>16</p>
</td>
<td>
<p>Hexadecimal</p>
</td>
</tr>
<tr>
<td>
<p>8</p>
</td>
<td>
<p>Octal</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Binary</p>
</td>
</tr>
<tr>
<td>
<p>0 or 10</p>
</td>
<td>
<p>Decimal</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>String</i> [in, out]

<dd>
<p>Pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that receives the string representation of <i>Value</i>. The buffer specified by the <i>Buffer</i>  of <i>String</i> must be large enough to hold the result. </p>
</dd>
</dl>

## -returns
<p><b>RtlIntegerToUnicodeString</b> returns an NTSTATUS value. Possible return values include:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully converted <i>Value</i> to a Unicode string.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p><i>Value</i> is too large to convert, or the <b>UNICODE_STRING</b> structure is too small to hold the result.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified code base is not valid. The only valid values are 0, 2, 8, 10, and 16.</p>

<p> </p>

## -remarks


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
<a href="..\wdm\nf-wdm-rtlunicodestringtointeger.md">RtlUnicodeStringToInteger</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlappendunicodestringtostring.md">RtlAppendUnicodeStringToString</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlIntegerToUnicodeString routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

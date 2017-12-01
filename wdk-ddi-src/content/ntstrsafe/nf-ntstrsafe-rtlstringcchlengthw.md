---
UID: NF.ntstrsafe.RtlStringCchLengthW
title: RtlStringCchLengthW
author: windows-driver-content
description: The RtlStringCchLengthW and RtlStringCchLengthA functions determine the length, in characters, of a supplied string.
old-location: kernel\rtlstringcchlength.htm
old-project: kernel
ms.assetid: 37d9309d-b105-4e56-b236-530ed49ca116
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlStringCchLengthW
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
req.alt-api: RtlStringCchLength,RtlStringCchLengthA,RtlStringCchLengthW
req.alt-loc: Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: RtlStringCchLengthW (Unicode) and RtlStringCchLengthA (ANSI)
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

# RtlStringCchLengthW function



## -description
<p>The <b>RtlStringCchLengthW</b> and <b>RtlStringCchLengthA</b> functions determine the length, in characters, of a supplied string. </p>


## -syntax

````
NTSTATUS RtlStringCchLength(
  _In_      LPCTSTR psz,
  _In_      size_t  cchMax,
  _Out_opt_ size_t  *pcch
);
````


## -parameters
<dl>

### -param <i>psz</i> [in]

<dd>
<p>A pointer to a buffer that contains a null-terminated string, the length of which will be checked. </p>
</dd>

### -param <i>cchMax</i> [in]

<dd>
<p>The maximum number of characters allowed in the buffer pointed to by <i>psz</i>, including the terminating null character. This value cannot exceed NTSTRSAFE_MAX_CCH. </p>
</dd>

### -param <i>pcch</i> [out, optional]

<dd>
<p>If the caller supplies a non-<b>NULL</b> address pointer, the function loads the address with the length, in characters, of the string that is contained in the buffer. The length does not include the string's terminating null character.</p>
</dd>
</dl>

## -returns
<p>The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>This success status means the string at <i>psz</i> was not <b>NULL</b>, and the length of the string (including the terminating null character) is less than or equal to <i>cchMax</i> characters.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This error status means the value in <i>psz</i> is <b>NULL</b>, <i>cchMax</i> is larger than NTSTRSAFE_MAX_CCH, or <i>psz</i> is longer than <i>cchMax</i>.</p>

<p> </p>

## -remarks
<p><b>RtlStringCchLengthW</b> and <b>RtlStringCchLengthA</b> should be used instead of <b>strlen</b>. They are used to ensure that a string is not larger than a given length, in characters. If that condition is met, <b>RtlStringCchLengthW</b> and <b>RtlStringCchLengthA</b> return the current length of the string in characters, not including the terminating null character.</p>

<p>Use <b>RtlStringCchLengthW</b> to handle Unicode strings and <b>RtlStringCchLengthA</b> to handle ANSI strings. The form you use depends on your data, as shown in the following table.</p>

<p>WCHAR</p>

<p>L"string"</p>

<p><b>RtlStringCchLengthW</b></p>

<p><b>char</b></p>

<p>"string"</p>

<p><b>RtlStringCchLengthA</b></p>

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
<p>Available in Windows XP with Service Pack 1 (SP1) and later versions of Windows. </p>
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
<p><b>RtlStringCchLengthW</b> (Unicode) and <b>RtlStringCchLengthA</b> (ANSI)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlstringcblength">RtlStringCbLength</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCchLength function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

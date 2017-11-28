---
UID: NF.ntifs.RtlAppendStringToString
title: RtlAppendStringToString
author: windows-driver-content
description: The RtlAppendStringToString routine concatenates two counted strings. It copies bytes from the source up to the length of the destination buffer.
old-location: ifsk\rtlappendstringtostring.htm
old-project: ifsk
ms.assetid: 8cd94502-c11a-4e6a-87f6-0c6034b6ac09
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlAppendStringToString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000, and later versions of all Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAppendStringToString
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
---

# RtlAppendStringToString function



## -description
<p>The <b>RtlAppendStringToString</b> routine concatenates two counted strings. It copies bytes from the source up to the length of the destination buffer.</p>


## -syntax

````
NTSTATUS RtlAppendStringToString(
  _Inout_       PSTRING Destination,
  _In_    const STRING  *Source
);
````


## -parameters
<dl>

### -param <i>Destination</i> [in, out]

<dd>
<p>A pointer to a counted string to which the string at <i>Source</i> should be appended. </p>
</dd>

### -param <i>Source</i> [in]

<dd>
<p>A pointer to a counted string to be appended to the string at <i>Destination</i>. </p>
</dd>
</dl>

## -returns
<p>The <b>RtlAppendStringToString</b> routine returns STATUS_SUCCESS if it appended the string at <i>Source</i> to the string at <i>Destination</i>. <b>RtlAppendStringToString</b> returns STATUS_BUFFER_TOO_SMALL if the <b>MaximumLength</b> of the <i>Destination</i> string is too small to allow the source string to be appended. </p>

## -remarks
<p>The sum of the <b>Length</b> members of the <i>Destination</i> and <i>Source</i> strings must be less than or equal to the <b>MaximumLength</b> of the <i>Destination</i> string.</p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

<p>The sum of the <b>Length</b> members of the <i>Destination</i> and <i>Source</i> strings must be less than or equal to the <b>MaximumLength</b> of the <i>Destination</i> string.</p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

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
<p>Available in Microsoft Windows 2000, and later versions of all Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561736">RtlAppendUnicodeStringToString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561738">RtlAppendUnicodeToString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561929">RtlInitString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAppendStringToString routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wdm.RtlAppendUnicodeToString
title: RtlAppendUnicodeToString
author: windows-driver-content
description: The RtlAppendUnicodeToString routine concatenates the supplied Unicode string to a buffered Unicode string.
old-location: kernel\rtlappendunicodetostring.htm
old-project: kernel
ms.assetid: 688f033b-1f0e-4f0a-9ccd-457ba726d728
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlAppendUnicodeToString
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
req.alt-api: RtlAppendUnicodeToString
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
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# RtlAppendUnicodeToString function



## -description
<p>The <b>RtlAppendUnicodeToString</b> routine concatenates the supplied Unicode string to a buffered Unicode string. </p>


## -syntax

````
NTSTATUS RtlAppendUnicodeToString(
  _Inout_  PUNICODE_STRING Destination,
  _In_opt_ PCWSTR          Source
);
````


## -parameters
<dl>

### -param <i>Destination</i> [in, out]

<dd>
<p>A pointer to the buffered string. </p>
</dd>

### -param <i>Source</i> [in, optional]

<dd>
<p>A pointer to the null-terminated string to append to the <i>Destination</i> string.</p>
</dd>
</dl>

## -returns
<p><b>RtlAppendUnicodeToString</b> can return one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The source string was successfully appended to the destination string, and the destination string length was updated to include the appended bytes.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The destination string buffer is too small to allow the source string to be appended, so the destination string length is not updated and the contents of the destination string buffer are not changed.</p>

<p> </p>

## -remarks
<p><b>RtlAppendUnicodeToString</b> appends the source string to the end of the destination string.</p>

<p>If the destination buffer is not large enough to contain the string that would result from concatenating the source and destination strings (not including the null character that terminates the source string), the routine returns STATUS_BUFFER_TOO_SMALL and leaves the destination string unchanged.</p>

<p>The <i>Destination</i> buffer must be resident if the caller is running at IRQL &gt;= DISPATCH_LEVEL.</p>

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
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlappendunicodestringtostring.md">RtlAppendUnicodeStringToString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlAppendUnicodeToString routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

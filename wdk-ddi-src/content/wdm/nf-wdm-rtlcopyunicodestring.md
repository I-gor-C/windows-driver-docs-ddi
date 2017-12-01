---
UID: NF.wdm.RtlCopyUnicodeString
title: RtlCopyUnicodeString
author: windows-driver-content
description: The RtlCopyUnicodeString routine copies a source string to a destination string.
old-location: kernel\rtlcopyunicodestring.htm
old-project: kernel
ms.assetid: 241801a5-4a02-46f3-a007-f571d58c7825
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlCopyUnicodeString
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
req.alt-api: RtlCopyUnicodeString
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
req.irql: Any level (See Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# RtlCopyUnicodeString function



## -description
<p>The <b>RtlCopyUnicodeString</b> routine copies a source string to a destination string.</p>


## -syntax

````
VOID RtlCopyUnicodeString(
  _Inout_  PUNICODE_STRING  DestinationString,
  _In_opt_ PCUNICODE_STRING SourceString
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [in, out]

<dd>
<p>A pointer to the destination string buffer. This parameter points to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure. </p>
</dd>

### -param <i>SourceString</i> [in, optional]

<dd>
<p>A pointer to the source string buffer. This parameter points to a <b>UNICODE_STRING</b> structure. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If <i>SourceString</i> is <b>NULL</b>, this routine sets the <b>Length</b> field of the structure pointed to by <i>DestinationString</i> to zero.</p>

<p>This routine does not modify the <b>MaximumLength</b> and <b>Buffer</b> fields of the structure pointed to by <i>DestinationString</i>.</p>

<p>The number of bytes copied from the source string is either the source string length (specified by the <b>Length</b> member of the structure pointed to by <i>SourceString</i>) or the maximum length of the destination string (specified by the <b>MaximumLength</b> member of the structure pointed to by <i>DestinationString</i>), whichever is smaller.</p>

<p>The caller must properly initialize all members of the structure pointed to by <i>DestinationString</i> before calling <b>RtlCopyUnicodeString</b>. Failure to initialize the <b>Length</b> or the <b>MaximumLength</b> member before calling this routine can cause a buffer overrun.</p>

<p>The <i>DestinationString</i> and <i>SourceString</i> buffers must be resident if the caller is running at IRQL &gt;= DISPATCH_LEVEL.</p>

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
<p>Any level (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-rtlcopystring.md">RtlCopyString</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlCopyUnicodeString routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

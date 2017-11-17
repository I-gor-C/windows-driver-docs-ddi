---
UID: NF.ntddk.RtlUpcaseUnicodeString
title: RtlUpcaseUnicodeString
author: windows-driver-content
description: The RtlUpcaseUnicodeString routine converts a copy of the source string to uppercase and writes the converted string in the destination buffer.
old-location: kernel\rtlupcaseunicodestring.htm
ms.assetid: fe3c6010-532b-4f3d-b3d3-a1c27d4a05f1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlUpcaseUnicodeString
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); 
Ntdll.dll (user mode)
req.irql: <= APC_LEVEL
ms.keywords: RtlUpcaseUnicodeString
req.iface: 
---

# RtlUpcaseUnicodeString function



## -description
<p>The <b>RtlUpcaseUnicodeString</b> routine converts a copy of the source string to uppercase and writes the converted string in the destination buffer.</p>


## -syntax

````
NTSTATUS RtlUpcaseUnicodeString(
  _Inout_ PUNICODE_STRING  DestinationString,
  _In_    PCUNICODE_STRING SourceString,
  _In_    BOOLEAN          AllocateDestinationString
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [in, out]

<dd>
<p>Pointer to a caller-allocated buffer for the converted Unicode string.</p>
</dd>

### -param <i>SourceString</i> [in]

<dd>
<p>Pointer to the source Unicode string to be converted to uppercase.</p>
</dd>

### -param <i>AllocateDestinationString</i> [in]

<dd>
<p>Specifies if <b>RtlUpcaseUnicodeString</b> is to allocate the buffer space for the <i>DestinationString</i>. If it does, the buffer must be deallocated by calling <b>RtlFreeUnicodeString</b>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>RtlUpcaseUnicodeString</b> returns STATUS_SUCCESS. Otherwise, no storage was allocated, and no conversion was done.</p>

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561903">RtlFreeUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563003">RtlUpcaseUnicodeChar</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlUpcaseUnicodeString routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wdm.RtlAnsiStringToUnicodeString
title: RtlAnsiStringToUnicodeString function
author: windows-driver-content
description: RtlAnsiStringToUnicodeString converts the given ANSI source string into a Unicode string.
old-location: kernel\rtlansistringtounicodestring.htm
old-project: kernel
ms.assetid: 926d8919-42de-4e24-a223-ffbf412edf6d
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlAnsiStringToUnicodeString
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
req.alt-api: RtlAnsiStringToUnicodeString
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
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# RtlAnsiStringToUnicodeString function



## -description
<b>RtlAnsiStringToUnicodeString</b> converts the given ANSI source string into a Unicode string.


## -syntax

````
NTSTATUS RtlAnsiStringToUnicodeString(
  _Inout_ PUNICODE_STRING DestinationString,
  _In_    PCANSI_STRING   SourceString,
  _In_    BOOLEAN         AllocateDestinationString
);
````


## -parameters

### -param DestinationString [in, out]

Pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure to hold the converted Unicode string. If <i>AllocateDestinationString</i> is <b>TRUE</b>, the routine allocates a new buffer to hold the string data, and updates the <b>Buffer</b> member of <i>DestinationString</i> to point to the new buffer. Otherwise, the routine uses the currently-specified buffer to hold the string.

### -param SourceString [in]

Pointer to the ANSI string to be converted to Unicode.

### -param AllocateDestinationString [in]

Specifies if this routine should allocate the buffer space for the destination string. If it does, the caller must deallocate the buffer by calling <a href="kernel.rtlfreeunicodestring">RtlFreeUnicodeString</a>.

## -returns
If the conversion succeeds, <b>RtlAnsiStringToUnicodeString</b> returns STATUS_SUCCESS. On failure, the routine does not allocate any memory.

## -remarks
The translation conforms to the current system locale information.

If caller sets <i>AllocateDestinationString</i> to <b>TRUE</b>, the routine replaces the <b>Buffer</b> member of <i>DestinationString</i> with a pointer to the buffer it allocates. The old value can be overwritten even when the routine returns an error status code.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows 2000.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ansi_string">ANSI_STRING</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="kernel.rtlansistringtounicodesize">RtlAnsiStringToUnicodeSize</a>
</dt>
<dt>
<a href="kernel.rtlfreeunicodestring">RtlFreeUnicodeString</a>
</dt>
<dt>
<a href="kernel.rtlinitansistring">RtlInitAnsiString</a>
</dt>
<dt>
<a href="kernel.rtlunicodestringtoansistring">RtlUnicodeStringToAnsiString</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlAnsiStringToUnicodeString function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

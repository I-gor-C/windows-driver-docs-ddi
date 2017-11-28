---
UID: NF.ntifs.RtlUpcaseUnicodeToOemN
title: RtlUpcaseUnicodeToOemN
author: windows-driver-content
description: The RtlUpcaseUnicodeToOemN routine translates a given Unicode string into an uppercase OEM string, using the current system OEM code page.
old-location: ifsk\rtlupcaseunicodetooemn.htm
old-project: ifsk
ms.assetid: d4d802c1-66e9-4342-ba7d-d9e5a464362e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlUpcaseUnicodeToOemN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlUpcaseUnicodeToOemN
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
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# RtlUpcaseUnicodeToOemN function



## -description
<p>The <b>RtlUpcaseUnicodeToOemN</b> routine translates a given Unicode string into an uppercase OEM string, using the current system OEM code page. </p>


## -syntax

````
NTSTATUS RtlUpcaseUnicodeToOemN(
  _Out_     PCHAR  OemString,
  _In_      ULONG  MaxBytesInOemString,
  _Out_opt_ PULONG BytesInOemString,
  _In_      PCWCH  UnicodeString,
  _In_      ULONG  BytesInUnicodeString
);
````


## -parameters
<dl>

### -param <i>OemString</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer to receive the translated string. </p>
</dd>

### -param <i>MaxBytesInOemString</i> [in]

<dd>
<p>Maximum number of bytes to be written to <i>OemString</i>. </p>
</dd>

### -param <i>BytesInOemString</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes in the translated string. This parameter can be <b>NULL</b>. </p>
</dd>

### -param <i>UnicodeString</i> [in]

<dd>
<p>Pointer to the Unicode source string to be translated. </p>
</dd>

### -param <i>BytesInUnicodeString</i> [in]

<dd>
<p>Size, in bytes, of the string at <i>UnicodeString</i>. </p>
</dd>
</dl>

## -returns
<p><b>RtlUnicodeToOemN</b> returns STATUS_SUCCESS if the full string at <i>UnicodeString</i> was successfully translated, converted to uppercase, and returned at <i>OemString</i>. Otherwise, it can return STATUS_BUFFER_OVERFLOW if the destination string must be truncated to fit the given <i>MaxBytesInOemString</i>. </p>

## -remarks
<p>For the return value STATUS_BUFFER_OVERFLOW, the truncated string at <i>OemString</i> was translated without error. </p>

<p>For the return value STATUS_SUCCESS, the value at <i>BytesInOemString</i>, if any, indicates the length of the returned string, rather than the given <i>MaxBytesInOemString</i>. </p>

<p>This routine does not modify the source string. It returns a null-terminated OEM string if the given <i>BytesInUnicodeString</i> included a NULL terminator and if the given <i>MaxBytesInOemString</i> did not cause truncation.</p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

<p>For the return value STATUS_BUFFER_OVERFLOW, the truncated string at <i>OemString</i> was translated without error. </p>

<p>For the return value STATUS_SUCCESS, the value at <i>BytesInOemString</i>, if any, indicates the length of the returned string, rather than the given <i>MaxBytesInOemString</i>. </p>

<p>This routine does not modify the source string. It returns a null-terminated OEM string if the given <i>BytesInUnicodeString</i> included a NULL terminator and if the given <i>MaxBytesInOemString</i> did not cause truncation.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553254">RtlUnicodeStringToOemSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553272">RtlUnicodeToOemN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553277">RtlUpcaseUnicodeStringToCountedOemString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553282">RtlUpcaseUnicodeStringToOemString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlUpcaseUnicodeToOemN routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

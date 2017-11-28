---
UID: NF.ntddk.RtlUpperChar
title: RtlUpperChar
author: windows-driver-content
description: The RtlUpperChar routine converts the specified character to uppercase.
old-location: kernel\rtlupperchar.htm
old-project: kernel
ms.assetid: a87e9f52-a136-492e-bfb3-dfbbea8b79e0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlUpperChar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlUpperChar
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
req.irql: <=APC_LEVEL
req.iface: 
---

# RtlUpperChar function



## -description
<p>The <b>RtlUpperChar</b> routine converts the specified character to uppercase.</p>


## -syntax

````
CHAR RtlUpperChar(
  _In_ CHAR Character
);
````


## -parameters
<dl>

### -param <i>Character</i> [in]

<dd>
<p>Specifies the character to convert. </p>
</dd>
</dl>

## -returns
<p><b>RtlUpperChar</b> returns the uppercase version of the specified character or returns the value specified by the caller for <i>Character</i> if the specified character cannot be converted.</p>

## -remarks
<p><b>RtlUpperChar</b> returns the input <i>Character</i> unconverted if it is the lead byte of a multibyte character or if the uppercase equivalent of <i>Character</i> is a double-byte character. To convert such characters, use <b>RtlUpcaseUnicodeChar</b>. </p>

<p><b>RtlUpperChar</b> returns the input <i>Character</i> unconverted if it is the lead byte of a multibyte character or if the uppercase equivalent of <i>Character</i> is a double-byte character. To convert such characters, use <b>RtlUpcaseUnicodeChar</b>. </p>

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
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563003">RtlUpcaseUnicodeChar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563013">RtlUpperString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlUpperChar routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

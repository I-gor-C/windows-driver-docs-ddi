---
UID: NF.wdm.RtlAnsiStringToUnicodeSize
title: RtlAnsiStringToUnicodeSize
author: windows-driver-content
description: The RtlAnsiStringToUnicodeSize routine returns the number of bytes required to hold an ANSI string converted into a Unicode string.
old-location: kernel\rtlansistringtounicodesize.htm
old-project: kernel
ms.assetid: 32687aa7-4e14-40cb-baa3-4a97d834bf86
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlAnsiStringToUnicodeSize
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
req.alt-api: RtlAnsiStringToUnicodeSize
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
req.iface: 
req.product: Windows 10 or later.
---

# RtlAnsiStringToUnicodeSize function



## -description
<p>The <b>RtlAnsiStringToUnicodeSize</b> routine returns the number of bytes required to hold an ANSI string converted into a Unicode string. </p>


## -syntax

````
ULONG RtlAnsiStringToUnicodeSize(
  _In_ PANSI_STRING AnsiString
);
````


## -parameters
<dl>

### -param <i>AnsiString</i> [in]

<dd>
<p>Pointer to a buffer containing the ANSI string. </p>
</dd>
</dl>

## -returns
<p><b>RtlAnsiStringToUnicodeSize</b> returns the necessary size in bytes for a Unicode string buffer.</p>

## -remarks
<p>Callers of <b>RtlAnsiStringToUnicodeSize</b> must be running at IRQL = PASSIVE_LEVEL.</p>

<p>Callers of <b>RtlAnsiStringToUnicodeSize</b> must be running at IRQL = PASSIVE_LEVEL.</p>

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
<dt>NtosKrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561729">RtlAnsiStringToUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563601">RtlxAnsiStringToUnicodeSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlAnsiStringToUnicodeSize routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

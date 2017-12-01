---
UID: NF.ntddk.RtlEqualString
title: RtlEqualString
author: windows-driver-content
description: The RtlEqualString routine compares two counted strings to determine whether they are equal.
old-location: kernel\rtlequalstring.htm
old-project: kernel
ms.assetid: f8244276-0cf6-4315-9f4a-85890194dad8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlEqualString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlEqualString
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
---

# RtlEqualString function



## -description
<p>The <b>RtlEqualString</b> routine compares two counted strings to determine whether they are equal.</p>


## -syntax

````
BOOLEAN RtlEqualString(
  _In_ const STRING  *String1,
  _In_ const STRING  *String2,
  _In_       BOOLEAN CaseInSensitive
);
````


## -parameters
<dl>

### -param <i>String1</i> [in]

<dd>
<p>Pointer to the first string.</p>
</dd>

### -param <i>String2</i> [in]

<dd>
<p>Pointer to the second string.</p>
</dd>

### -param <i>CaseInSensitive</i> [in]

<dd>
<p>If <b>TRUE</b>, case should be ignored when doing the comparison. </p>
</dd>
</dl>

## -returns
<p><b>RtlEqualString</b> returns <b>TRUE</b> if the two strings are equal, otherwise it returns <b>FALSE</b>.</p>

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
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
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
<a href="..\wdm\nf-wdm-rtlequalunicodestring.md">RtlEqualUnicodeString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlEqualString routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

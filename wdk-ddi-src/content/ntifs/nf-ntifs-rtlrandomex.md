---
UID: NF.ntifs.RtlRandomEx
title: RtlRandomEx
author: windows-driver-content
description: The RtlRandomEx routine returns a random number that was generated from a given seed value.
old-location: ifsk\rtlrandomex.htm
old-project: ifsk
ms.assetid: 2a5c70da-69dc-431c-9ce9-908633045372
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlRandomEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlRandomEx
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

# RtlRandomEx function



## -description
<p>The <b>RtlRandomEx</b> routine returns a random number that was generated from a given seed value. </p>


## -syntax

````
ULONG RtlRandomEx(
  _Inout_ PULONG Seed
);
````


## -parameters
<dl>

### -param <i>Seed</i> [in, out]

<dd>
<p>Unsigned long value from which to generate a random number. </p>
</dd>
</dl>

## -returns
<p><b>RtlRandomEx</b> returns a random number in the range [0..MAXLONG-1]. </p>

## -remarks
<p><b>RtlRandomEx</b> returns values that are uniformly distributed over the range from zero to the maximum possible LONG value less 1 if it is called repeatedly with the same <i>Seed</i>.</p>

<p>The <b>RtlRandomEx</b> function is an improved version of the <b>RtlRandom</b> function. Compared with the <b>RtlRandom</b> function, <b>RtlRandomEx</b> is twice as fast and produces better random numbers since the period of the random numbers generated is comparatively higher. </p>

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
<p>Available in Microsoft Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
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
<a href="..\ntifs\nf-ntifs-rtlrandom.md">RtlRandom</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlRandomEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

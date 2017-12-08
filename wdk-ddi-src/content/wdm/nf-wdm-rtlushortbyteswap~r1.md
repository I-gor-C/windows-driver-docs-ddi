---
UID: NF.wdm.RtlUshortByteSwap~r1
title: RtlUshortByteSwap
author: windows-driver-content
description: The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value.
old-location: kernel\rtlushortbyteswap.htm
old-project: kernel
ms.assetid: 83f6a599-0b35-4a02-b20f-80abcc6eae4f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUshortByteSwap
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
req.alt-api: RtlUshortByteSwap
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
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# RtlUshortByteSwap function



## -description
<p>The <b>RtlUshortByteSwap</b> routine reverses the ordering of the two bytes in a 16-bit unsigned integer value.</p>


## -syntax

````
USHORT RtlUshortByteSwap(
  _In_ USHORT Source
);
````


## -parameters
<dl>

### -param Source [in]

<dd>
<p>A USHORT value to convert to a byte-swapped version.</p>
</dd>
</dl>

## -returns
<p>The byte-swapped version of the <i>Source</i> input parameter value.</p>

## -remarks
<p>For example, if the <i>Source</i> parameter value is 0x1234, the routine returns 0x3412.</p>

<p>A typical use of this routine is to convert a USHORT value from little-endian byte format to big-endian byte format, and vice versa.</p>

<p>Use this routine instead of <b>ntohs</b> or <b>htons</b>.</p>

<p>To reverse the ordering of bytes in a ULONG value, use the <a href="..\wdm\nf-wdm-rtlulongbyteswap.md">RtlUlongByteSwap</a> routine. To reverse ordering of bytes in a ULONGLONG value, use the <a href="..\wdm\nf-wdm-rtlulonglongbyteswap.md">RtlUlonglongByteSwap</a> routine.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlulongbyteswap.md">RtlUlongByteSwap</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlulonglongbyteswap.md">RtlUlonglongByteSwap</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlUshortByteSwap routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

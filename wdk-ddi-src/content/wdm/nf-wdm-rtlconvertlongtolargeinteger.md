---
UID: NF.wdm.RtlConvertLongToLargeInteger
title: RtlConvertLongToLargeInteger
author: windows-driver-content
description: The RtlConvertLongToLargeInteger routine converts the input signed integer to a signed large integer.
old-location: kernel\rtlconvertlongtolargeinteger.htm
old-project: kernel
ms.assetid: 8c1f6cd3-f54b-4104-bd14-63d2c284946c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlConvertLongToLargeInteger
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
req.alt-api: RtlConvertLongToLargeInteger
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

# RtlConvertLongToLargeInteger function



## -description
<p>The <b>RtlConvertLongToLargeInteger</b> routine converts the input signed integer to a signed large integer.</p>


## -syntax

````
LARGE_INTEGER RtlConvertLongToLargeInteger(
  _In_ LONG SignedInteger
);
````


## -parameters
<dl>

### -param <i>SignedInteger</i> [in]

<dd>
<p>Specifies an integer of type LONG.</p>
</dd>
</dl>

## -returns
<p><b>RtlConvertLongToLargeInteger</b> returns the large integer result.</p>

## -remarks
<p>This routine is not supported in Windows XP. Use native support for <b>__int64</b> instead. </p>

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
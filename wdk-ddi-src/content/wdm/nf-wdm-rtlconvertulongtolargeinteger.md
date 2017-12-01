---
UID: NF.wdm.RtlConvertUlongToLargeInteger
title: RtlConvertUlongToLargeInteger
author: windows-driver-content
description: The RtlConvertUlongToLargeInteger routine converts the input unsigned integer to a signed large integer. For Windows XP and later versions of Windows, do not use this routine; use the native support for __int64.
old-location: kernel\rtlconvertulongtolargeinteger.htm
old-project: kernel
ms.assetid: 9e0b8d36-0191-4f78-91dd-874346a69072
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlConvertUlongToLargeInteger
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
req.alt-api: RtlConvertUlongToLargeInteger
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

# RtlConvertUlongToLargeInteger function



## -description
<p>The <b>RtlConvertUlongToLargeInteger</b> routine converts the input unsigned integer to a signed large integer. For Windows XP and later versions of Windows, do not use this routine; use the native support for <b>__int64</b>. </p>


## -syntax

````
LARGE_INTEGER RtlConvertUlongToLargeInteger(
  _In_ ULONG UnsignedInteger
);
````


## -parameters
<dl>

### -param <i>UnsignedInteger</i> [in]

<dd>
<p>Specifies a value of type ULONG.</p>
</dd>
</dl>

## -returns
<p><b>RtlConvertUlongToLargeInteger</b> returns the converted large integer. </p>

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
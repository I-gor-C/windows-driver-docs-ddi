---
UID: NF.ntintsafe.RtlULongLongToLongLong
title: RtlULongLongToLongLong
author: windows-driver-content
description: Converts a value of type ULONGLONG to a value of type LONGLONG.
old-location: kernel\rtlulonglongtolonglong.htm
ms.assetid: 7F91DDA1-AF01-4DA9-AB3B-AA5CA87C5FD6
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntintsafe.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlULongLongToLongLong
req.alt-loc: Ntintsafe.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: RtlULongLongToLongLong
req.iface: 
---

# RtlULongLongToLongLong function



## -description
<p>Converts a value of type <b>ULONGLONG</b> to a value of type <b>LONGLONG</b>.</p>


## -syntax

````
NTSTATUS RtlULongLongToLongLong(
  _In_  ULONGLONG ullOperand,
  _Out_ LONGLONG  *pllResult
);
````


## -parameters
<dl>

### -param <i>ullOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>pllResult</i> [out]

<dd>
<p>A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.</p>

<p>This function uses the following alternate name:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntintsafe.h</dt>
</dl>
</td>
</tr>
</table>
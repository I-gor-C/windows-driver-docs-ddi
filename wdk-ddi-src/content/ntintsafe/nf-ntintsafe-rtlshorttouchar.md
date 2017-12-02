---
UID: NF.ntintsafe.RtlShortToUChar
title: RtlShortToUChar
author: windows-driver-content
description: Converts a value of type SHORT to a value of type UCHAR.
old-location: kernel\rtlshorttouchar.htm
old-project: kernel
ms.assetid: 6DA0F939-F4B3-4E66-A90C-5112AE6FEC8D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlShortToUChar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntintsafe.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlShortToUChar
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
req.iface: 
---

# RtlShortToUChar function



## -description
<p>Converts a value of type <b>SHORT</b> to a value of type <b>UCHAR</b>.</p>


## -syntax

````
NTSTATUS RtlShortToUChar(
  _In_  SHORT sOperand,
  _Out_ UCHAR *pch
);
````


## -parameters
<dl>

### -param sOperand [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param pch [out]

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
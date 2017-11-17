---
UID: NF.ntintsafe.RtlUInt8ToChar
title: RtlUInt8ToChar
author: windows-driver-content
description: Converts a value of type UINT8 to a value of type CHAR.
old-location: kernel\rtluint8tochar.htm
ms.assetid: 78EAB56F-8E6D-4048-83DC-1B9BC75E08B5
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
req.alt-api: RtlUInt8ToChar
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
ms.keywords: RtlUInt8ToChar
req.iface: 
---

# RtlUInt8ToChar function



## -description
<p>Converts a value of type <b>UINT8</b> to a value of type <b>CHAR</b>.</p>


## -syntax

````
NTSTATUS RtlUInt8ToChar(
  _In_  UINT8 u8Operand,
  _Out_ CHAR  *pch
);
````


## -parameters
<dl>

### -param <i>u8Operand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>pch</i> [out]

<dd>
<p>A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.</p>

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
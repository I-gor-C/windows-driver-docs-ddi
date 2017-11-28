---
UID: NF.ntintsafe.RtlUInt8Mult
title: RtlUInt8Mult
author: windows-driver-content
description: Multiplies one value of type UINT8 by another.
old-location: kernel\rtluint8mult.htm
old-project: kernel
ms.assetid: 3F9E47F5-1DE3-4949-BE92-8C8F571BFD3D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlUInt8Mult
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
req.alt-api: RtlUInt8Mult
req.alt-loc: ntintsafe.h
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

# RtlUInt8Mult function



## -description
<p>Multiplies one value of type <b>UINT8</b> by another.</p>


## -syntax

````
NTSTATUS RtlUInt8Mult(
  _In_  UINT8 u8Multiplicand,
  _In_  UINT8 u8Multiplier,
  _Out_ UINT8 *pu8Result
);
````


## -parameters
<dl>

### -param <i>u8Multiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>u8Multiplier</i>.</p>
</dd>

### -param <i>u8Multiplier</i> [in]

<dd>
<p>The value by which to multiply <i>u8Multiplicand</i>.</p>
</dd>

### -param <i>pu8Result</i> [out]

<dd>
<p>A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.</p>

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
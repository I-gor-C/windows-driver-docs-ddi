---
UID: NF.ntintsafe.RtlUShortMult
title: RtlUShortMult
author: windows-driver-content
description: Multiplies one value of type USHORT by another.
old-location: kernel\rtlushortmult.htm
old-project: kernel
ms.assetid: 1727AD96-FC0B-4B52-92C5-5E7502433021
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUShortMult
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
req.alt-api: RtlUShortMult
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

# RtlUShortMult function



## -description
<p>Multiplies one value of type <b>USHORT</b> by another.</p>


## -syntax

````
NTSTATUS RtlUShortMult(
  _In_  USHORT usMultiplicand,
  _In_  USHORT usMultiplier,
  _Out_ USHORT *pusResult
);
````


## -parameters
<dl>

### -param usMultiplicand [in]

<dd>
<p>The value to be multiplied by <i>usMultiplier</i>.</p>
</dd>

### -param usMultiplier [in]

<dd>
<p>The value by which to multiply <i>usMultiplicand</i>.</p>
</dd>

### -param pusResult [out]

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
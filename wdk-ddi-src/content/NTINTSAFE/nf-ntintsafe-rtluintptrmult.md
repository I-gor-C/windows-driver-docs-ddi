---
UID: NF.ntintsafe.RtlUIntPtrMult
title: RtlUIntPtrMult
author: windows-driver-content
description: Multiplies one value of type UINT_PTR by another.
old-location: kernel\rtluintptrmult.htm
ms.assetid: E484AB83-DEA6-4FC7-9896-26984D998661
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
req.alt-api: RtlUIntPtrMult
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
ms.keywords: RtlUIntPtrMult
req.iface: 
---

# RtlUIntPtrMult function



## -description
<p>Multiplies one value of type <b>UINT_PTR</b> by another.</p>


## -syntax

````
NTSTATUS RtlUIntPtrMult(
  _In_  UINT_PTR uMultiplicand,
  _In_  UINT_PTR uMultiplier,
  _Out_ UINT_PTR *puResult
);
````


## -parameters
<dl>

### -param <i>uMultiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>uMultiplier</i>.</p>
</dd>

### -param <i>uMultiplier</i> [in]

<dd>
<p>The value by which to multiply <i>uMultiplicand</i>.</p>
</dd>

### -param <i>puResult</i> [out]

<dd>
<p>A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.</p>

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
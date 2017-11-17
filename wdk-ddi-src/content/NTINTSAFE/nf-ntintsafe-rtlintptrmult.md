---
UID: NF.ntintsafe.RtlIntPtrMult
title: RtlIntPtrMult
author: windows-driver-content
description: Multiplies one value of type INT_PTR by another.
old-location: kernel\rtlintptrmult.htm
ms.assetid: F40C5DBB-8E52-471E-B010-A5EDFACDF773
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
req.alt-api: RtlIntPtrMult
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
ms.keywords: RtlIntPtrMult
req.iface: 
---

# RtlIntPtrMult function



## -description
<p>Multiplies one value of type <b>INT_PTR</b> by another.</p>


## -syntax

````
NTSTATUS RtlIntPtrMult(
  _In_  INT_PTR iMultiplicand,
  _In_  INT_PTR iMultiplier,
  _Out_ INT_PTR *piResult
);
````


## -parameters
<dl>

### -param <i>iMultiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>iMultiplier</i>.</p>
</dd>

### -param <i>iMultiplier</i> [in]

<dd>
<p>The value by which to multiply <i>iMultiplicand</i>.</p>
</dd>

### -param <i>piResult</i> [out]

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
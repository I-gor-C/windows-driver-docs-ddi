---
UID: NF.ntintsafe.RtlSizeTMult
title: RtlSizeTMult
author: windows-driver-content
description: Multiplies one value of type SIZE_T by another.
old-location: kernel\rtlsizetmult.htm
old-project: kernel
ms.assetid: 3EC72857-2880-4F03-8CC3-9B9A80F19273
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlSizeTMult
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
req.alt-api: RtlSizeTMult
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

# RtlSizeTMult function



## -description
<p>Multiplies one value of type <b>SIZE_T</b> by another.</p>


## -syntax

````
NTSTATUS RtlSizeTMult(
  _In_  SIZE_T Multiplicand,
  _In_  SIZE_T Multiplier,
  _Out_ SIZE_T *pResult
);
````


## -parameters
<dl>

### -param <i>Multiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>Multiplier</i>.</p>
</dd>

### -param <i>Multiplier</i> [in]

<dd>
<p>The value by which to multiply <i>Multiplicand</i>.</p>
</dd>

### -param <i>pResult</i> [out]

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
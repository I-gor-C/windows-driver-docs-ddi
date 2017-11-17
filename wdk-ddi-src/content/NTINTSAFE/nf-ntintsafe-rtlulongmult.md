---
UID: NF.ntintsafe.RtlULongMult
title: RtlULongMult
author: windows-driver-content
description: Multiplies one value of type ULONG by another.
old-location: kernel\rtlulongmult.htm
ms.assetid: 2D5DA884-1746-4DBC-8ABC-2D307181CCAE
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
req.alt-api: RtlULongMult
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
ms.keywords: RtlULongMult
req.iface: 
---

# RtlULongMult function



## -description
<p>Multiplies one value of type <b>ULONG</b> by another.</p>


## -syntax

````
NTSTATUS RtlULongMult(
  _In_  ULONG ulMultiplicand,
  _In_  ULONG ulMultiplier,
  _Out_ ULONG *pulResult
);
````


## -parameters
<dl>

### -param <i>ulMultiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>ulMultiplier</i>.</p>
</dd>

### -param <i>ulMultiplier</i> [in]

<dd>
<p>The value by which to multiply <i>ulMultiplicand</i>.</p>
</dd>

### -param <i>pulResult</i> [out]

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
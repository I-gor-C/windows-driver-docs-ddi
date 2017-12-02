---
UID: NF.ntintsafe.RtlULongPtrMult
title: RtlULongPtrMult
author: windows-driver-content
description: Multiplies one value of type ULONG_PTR by another.
old-location: kernel\rtlulongptrmult.htm
old-project: kernel
ms.assetid: 6E66CD0B-7CAD-4BF1-A6DD-56C5029A929E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongPtrMult
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
req.alt-api: RtlULongPtrMult
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

# RtlULongPtrMult function



## -description
<p>Multiplies one value of type <b>ULONG_PTR</b> by another.</p>


## -syntax

````
NTSTATUS RtlULongPtrMult(
  _In_  ULONG_PTR Multiplicand,
  _In_  ULONG_PTR Multiplier,
  _Out_ ULONG_PTR *pResult
);
````


## -parameters
<dl>

### -param Multiplicand [in]

<dd>
<p>The value to be multiplied by <i>Multiplier</i>.</p>
</dd>

### -param Multiplier [in]

<dd>
<p>The value by which to multiply <i>Multiplicand</i>.</p>
</dd>

### -param pResult [out]

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
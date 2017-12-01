---
UID: NF.ntintsafe.RtlDWordPtrMult
title: RtlDWordPtrMult
author: windows-driver-content
description: Multiplies one value of type DWORD_PTR by another.
old-location: kernel\rtldwordptrmult.htm
old-project: kernel
ms.assetid: E7EEE6D7-19C8-481F-BAEF-15998819D2D0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlDWordPtrMult
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
req.alt-api: RtlDWordPtrMult
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

# RtlDWordPtrMult function



## -description
<p>Multiplies one value of type <b>DWORD_PTR</b> by another.</p>


## -syntax

````
NTSTATUS RtlDWordPtrMult(
  _In_  DWORD_PTR dwMultiplicand,
  _In_  DWORD_PTR dwMultiplier,
  _Out_ DWORD_PTR *pdwResult
);
````


## -parameters
<dl>

### -param <i>dwMultiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>dwMultiplier</i>.</p>
</dd>

### -param <i>dwMultiplier</i> [in]

<dd>
<p>The value by which to multiply <i>dwMultiplicand</i>.</p>
</dd>

### -param <i>pdwResult</i> [out]

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
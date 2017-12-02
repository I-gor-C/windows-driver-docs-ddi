---
UID: NF.ntintsafe.RtlULongLongMult
title: RtlULongLongMult
author: windows-driver-content
description: Multiplies one value of type ULONGLONG by another.
old-location: kernel\rtlulonglongmult.htm
old-project: kernel
ms.assetid: 9865C8D1-DA20-4733-8862-7CA38069A93F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongLongMult
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
req.alt-api: RtlULongLongMult
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

# RtlULongLongMult function



## -description
<p>Multiplies one value of type <b>ULONGLONG</b> by another.</p>


## -syntax

````
NTSTATUS RtlULongLongMult(
  _In_  ULONGLONG ullMultiplicand,
  _In_  ULONGLONG ullMultiplier,
  _Out_ ULONGLONG *pullResult
);
````


## -parameters
<dl>

### -param ullMultiplicand [in]

<dd>
<p>The value to be multiplied by <i>ullMultiplier</i>.</p>
</dd>

### -param ullMultiplier [in]

<dd>
<p>The value by which to multiply <i>ullMultiplicand</i>.</p>
</dd>

### -param pullResult [out]

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
---
UID: NF.ntintsafe.RtlShortMult
title: RtlShortMult
author: windows-driver-content
description: Multiplies one value of type SHORT by another.
old-location: kernel\rtlshortmult.htm
ms.assetid: 15DCCCF1-72B1-4944-9BF0-ACAF1DEB9243
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
req.alt-api: RtlShortMult
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
ms.keywords: RtlShortMult
req.iface: 
---

# RtlShortMult function



## -description
<p>Multiplies one value of type <b>SHORT</b> by another.</p>


## -syntax

````
NTSTATUS RtlShortMult(
  _In_  SHORT sMultiplicand,
  _In_  SHORT sMultiplier,
  _Out_ SHORT *psResult
);
````


## -parameters
<dl>

### -param <i>sMultiplicand</i> [in]

<dd>
<p>The value to be multiplied by <i>sMultiplier</i>.</p>
</dd>

### -param <i>sMultiplier</i> [in]

<dd>
<p>The value by which to multiply <i>sMultiplicand</i>.</p>
</dd>

### -param <i>psResult</i> [out]

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
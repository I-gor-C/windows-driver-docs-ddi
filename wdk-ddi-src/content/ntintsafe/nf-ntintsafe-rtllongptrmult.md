---
UID: NF.ntintsafe.RtlLongPtrMult
title: RtlLongPtrMult
author: windows-driver-content
description: Multiplies one value of type LONG_PTR by another.
old-location: kernel\rtllongptrmult.htm
old-project: kernel
ms.assetid: AF602DBE-E106-4105-B56B-DE9EE7691A05
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlLongPtrMult
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
req.alt-api: RtlLongPtrMult
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

# RtlLongPtrMult function



## -description
<p>Multiplies one value of type <b>LONG_PTR</b> by another.</p>


## -syntax

````
NTSTATUS RtlLongPtrMult(
  _In_  LONG_PTR lMultiplicand,
  _In_  LONG_PTR lMultiplier,
  _Out_ LONG_PTR *plResult
);
````


## -parameters
<dl>

### -param lMultiplicand [in]

<dd>
<p>The value to be multiplied by <i>lMultiplier</i>.</p>
</dd>

### -param lMultiplier [in]

<dd>
<p>The value by which to multiply <i>lMultiplicand</i>.</p>
</dd>

### -param plResult [out]

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
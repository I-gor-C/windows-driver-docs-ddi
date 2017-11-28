---
UID: NF.ntintsafe.RtlSSIZETSub
title: RtlSSIZETSub
author: windows-driver-content
description: Subtracts one value of type SSIZE_T from another.
old-location: kernel\rtlssizetsub.htm
old-project: kernel
ms.assetid: 6EFDD7BF-B347-4E02-905E-01F0F155DB6F
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlSSIZETSub
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
req.alt-api: RtlSSIZETSub
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

# RtlSSIZETSub function



## -description
<p>Subtracts one value of type <b>SSIZE_T</b> from another.</p>


## -syntax

````
NTSTATUS RtlSSIZETSub(
  _In_  SSIZE_T Minuend,
  _In_  SSIZE_T Subtrahend,
  _Out_ SSIZE_T *pResult
);
````


## -parameters
<dl>

### -param <i>Minuend</i> [in]

<dd>
<p>The value from which <i>Subtrahend</i> is subtracted.</p>
</dd>

### -param <i>Subtrahend</i> [in]

<dd>
<p>The value to subtract from <i>Minuend</i>.</p>
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
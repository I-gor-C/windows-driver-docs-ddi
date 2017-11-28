---
UID: NF.ntintsafe.RtlSSIZETAdd
title: RtlSSIZETAdd
author: windows-driver-content
description: Adds two values of type SSIZE_T.
old-location: kernel\rtlssizetadd.htm
old-project: kernel
ms.assetid: 1CBB3CDF-E7DD-4686-8EF6-FBCADE978A16
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlSSIZETAdd
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
req.alt-api: RtlSSIZETAdd
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

# RtlSSIZETAdd function



## -description
<p>Adds two values of type <b>SSIZE_T</b>.</p>


## -syntax

````
NTSTATUS RtlSSIZETAdd(
  _In_  SSIZE_T Augend,
  _In_  SSIZE_T Addend,
  _Out_ SSIZE_T *pResult
);
````


## -parameters
<dl>

### -param <i>Augend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>Addend</i> [in]

<dd>
<p>The value to add to <i>Augend</i>.</p>
</dd>

### -param <i>pResult</i> [out]

<dd>
<p>A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
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
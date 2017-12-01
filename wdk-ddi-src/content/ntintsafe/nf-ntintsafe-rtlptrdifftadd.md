---
UID: NF.ntintsafe.RtlPtrdiffTAdd
title: RtlPtrdiffTAdd
author: windows-driver-content
description: Adds two values of type PTRDIFF_T.
old-location: kernel\rtlptrdifftadd.htm
old-project: kernel
ms.assetid: 3B4C0CF0-8153-446E-A834-C1FE28651718
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlPtrdiffTAdd
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
req.alt-api: RtlPtrdiffTAdd
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

# RtlPtrdiffTAdd function



## -description
<p>Adds two values of type <b>PTRDIFF_T</b>.</p>


## -syntax

````
NTSTATUS RtlPtrdiffTAdd(
  _In_  PTRDIFF_T Augend,
  _In_  PTRDIFF_T Addend,
  _Out_ PTRDIFF_T *pResult
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
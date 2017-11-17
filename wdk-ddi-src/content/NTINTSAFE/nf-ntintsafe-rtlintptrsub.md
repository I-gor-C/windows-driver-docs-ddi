---
UID: NF.ntintsafe.RtlIntPtrSub
title: RtlIntPtrSub
author: windows-driver-content
description: Subtracts one value of type INT_PTR from another.
old-location: kernel\rtlintptrsub.htm
ms.assetid: 72352FD3-4855-4630-AF42-368FF3A6B2BB
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
req.alt-api: RtlIntPtrSub
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
ms.keywords: RtlIntPtrSub
req.iface: 
---

# RtlIntPtrSub function



## -description
<p>Subtracts one value of type <b>INT_PTR</b> from another.</p>


## -syntax

````
NTSTATUS RtlIntPtrSub(
  _In_  INT_PTR iMinuend,
  _In_  INT_PTR iSubtrahend,
  _Out_ INT_PTR *piResult
);
````


## -parameters
<dl>

### -param <i>iMinuend</i> [in]

<dd>
<p>The value from which <i>iSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>iSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>iMinuend</i>.</p>
</dd>

### -param <i>piResult</i> [out]

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
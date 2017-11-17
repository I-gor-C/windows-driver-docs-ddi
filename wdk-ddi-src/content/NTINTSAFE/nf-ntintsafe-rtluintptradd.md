---
UID: NF.ntintsafe.RtlUIntPtrAdd
title: RtlUIntPtrAdd
author: windows-driver-content
description: Adds two values of type UINT_PTR.
old-location: kernel\rtluintptradd.htm
ms.assetid: 9106CE96-A26F-4358-9668-2C0E331BB793
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
req.alt-api: RtlUIntPtrAdd
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
ms.keywords: RtlUIntPtrAdd
req.iface: 
---

# RtlUIntPtrAdd function



## -description
<p>Adds two values of type <b>UINT_PTR</b>.</p>


## -syntax

````
NTSTATUS RtlUIntPtrAdd(
  _In_  UINT_PTR uAugend,
  _In_  UINT_PTR uAddend,
  _Out_ UINT_PTR *puResult
);
````


## -parameters
<dl>

### -param <i>uAugend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>uAddend</i> [in]

<dd>
<p>The value to add to <i>uAugend</i>.</p>
</dd>

### -param <i>puResult</i> [out]

<dd>
<p>A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
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
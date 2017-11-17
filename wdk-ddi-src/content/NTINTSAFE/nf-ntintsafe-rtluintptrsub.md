---
UID: NF.ntintsafe.RtlUIntPtrSub
title: RtlUIntPtrSub
author: windows-driver-content
description: Subtracts one value of type UINT_PTR from another.
old-location: kernel\rtluintptrsub.htm
ms.assetid: D0E23A94-515B-4225-A8AC-390CDD3BEA60
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
req.alt-api: RtlUIntPtrSub
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
ms.keywords: RtlUIntPtrSub
req.iface: 
---

# RtlUIntPtrSub function



## -description
<p>Subtracts one value of type <b>UINT_PTR</b> from another.</p>


## -syntax

````
NTSTATUS RtlUIntPtrSub(
  _In_  UINT_PTR uMinuend,
  _In_  UINT_PTR uSubtrahend,
  _Out_ UINT_PTR *puResult
);
````


## -parameters
<dl>

### -param <i>uMinuend</i> [in]

<dd>
<p>The value from which <i>uSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>uSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>uMinuend</i>.</p>
</dd>

### -param <i>puResult</i> [out]

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
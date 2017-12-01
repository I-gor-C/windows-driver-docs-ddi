---
UID: NF.ntintsafe.RtlDWordPtrSub
title: RtlDWordPtrSub
author: windows-driver-content
description: Subtracts one value of type DWORD_PTR from another.
old-location: kernel\rtldwordptrsub.htm
old-project: kernel
ms.assetid: B3268640-F256-4B64-AE95-8D30A6A7BF6C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlDWordPtrSub
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
req.alt-api: RtlDWordPtrSub
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

# RtlDWordPtrSub function



## -description
<p>Subtracts one value of type <b>DWORD_PTR</b> from another.</p>


## -syntax

````
NTSTATUS RtlDWordPtrSub(
  _In_  DWORD_PTR dwMinuend,
  _In_  DWORD_PTR dwSubtrahend,
  _Out_ DWORD_PTR *pdwResult
);
````


## -parameters
<dl>

### -param <i>dwMinuend</i> [in]

<dd>
<p>The value from which <i>dwSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>dwSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>dwMinuend</i>.</p>
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
---
UID: NF.ntintsafe.RtlULongPtrSub
title: RtlULongPtrSub
author: windows-driver-content
description: Subtracts one value of type ULONG_PTR from another.
old-location: kernel\rtlulongptrsub.htm
old-project: kernel
ms.assetid: E8F9A1B0-5E87-4CB0-8C9E-5C2494F07C39
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongPtrSub
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
req.alt-api: RtlULongPtrSub
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

# RtlULongPtrSub function



## -description
<p>Subtracts one value of type <b>ULONG_PTR</b> from another.</p>


## -syntax

````
NTSTATUS RtlULongPtrSub(
  _In_  ULONG_PTR ulMinuend,
  _In_  ULONG_PTR ulSubtrahend,
  _Out_ ULONG_PTR *pulResult
);
````


## -parameters
<dl>

### -param <i>ulMinuend</i> [in]

<dd>
<p>The value from which <i>ulSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>ulSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>ulMinuend</i>.</p>
</dd>

### -param <i>pulResult</i> [out]

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
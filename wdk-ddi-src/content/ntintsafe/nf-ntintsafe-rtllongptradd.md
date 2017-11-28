---
UID: NF.ntintsafe.RtlLongPtrAdd
title: RtlLongPtrAdd
author: windows-driver-content
description: Adds two values of type LONG_PTR.
old-location: kernel\rtllongptradd.htm
old-project: kernel
ms.assetid: D0036070-A23D-4525-AE80-E10B20330F97
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlLongPtrAdd
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
req.alt-api: RtlLongPtrAdd
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

# RtlLongPtrAdd function



## -description
<p>Adds two values of type <b>LONG_PTR</b>.</p>


## -syntax

````
NTSTATUS RtlLongPtrAdd(
  _In_  UINT8 u8Augend,
  _In_  UINT8 u8Addend,
  _Out_ UINT8 *pu8Result
);
````


## -parameters
<dl>

### -param <i>u8Augend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>u8Addend</i> [in]

<dd>
<p>The value to add to <i>u8Augend</i>.</p>
</dd>

### -param <i>pu8Result</i> [out]

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
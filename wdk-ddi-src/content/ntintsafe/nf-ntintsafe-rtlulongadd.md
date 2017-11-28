---
UID: NF.ntintsafe.RtlULongAdd
title: RtlULongAdd
author: windows-driver-content
description: Adds two values of type ULONG.
old-location: kernel\rtlulongadd.htm
old-project: kernel
ms.assetid: 03E5C0DB-E245-43E2-80C0-0C1D67673038
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlULongAdd
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
req.alt-api: RtlULongAdd
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

# RtlULongAdd function



## -description
<p>Adds two values of type <b>ULONG</b>.</p>


## -syntax

````
NTSTATUS RtlULongAdd(
  _In_  ULONG ulAugend,
  _In_  ULONG ulAddend,
  _Out_ ULONG *pulResult
);
````


## -parameters
<dl>

### -param <i>ulAugend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>ulAddend</i> [in]

<dd>
<p>The value to add to <i>ulAugend</i>.</p>
</dd>

### -param <i>pulResult</i> [out]

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
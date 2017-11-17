---
UID: NF.ntintsafe.RtlLongAdd
title: RtlLongAdd
author: windows-driver-content
description: Adds two values of type LONG.
old-location: kernel\rtllongadd.htm
ms.assetid: E8CF5E74-2EDA-4B27-A9C0-053930FF741D
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
req.alt-api: RtlLongAdd
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
ms.keywords: RtlLongAdd
req.iface: 
---

# RtlLongAdd function



## -description
<p>Adds two values of type <b>LONG</b>.</p>


## -syntax

````
NTSTATUS RtlLongAdd(
  _In_  LONG lAugend,
  _In_  LONG lAddend,
  _Out_ LONG *plResult
);
````


## -parameters
<dl>

### -param <i>lAugend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>lAddend</i> [in]

<dd>
<p>The value to add to <i>lAugend</i>.</p>
</dd>

### -param <i>plResult</i> [out]

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